#!/usr/bin/env python3
"""Local, approval-first workflow for a remote AI job search."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).parent
PROFILE_PATH = ROOT / "config" / "profile.json"
APPLICATIONS_PATH = ROOT / "data" / "applications.json"


def read_json(path: Path, default):
    if not path.exists():
        return default
    with path.open() as file:
        return json.load(file)


def write_applications(applications):
    APPLICATIONS_PATH.parent.mkdir(exist_ok=True)
    with APPLICATIONS_PATH.open("w") as file:
        json.dump(applications, file, indent=2)
        file.write("\n")


def score(job, profile):
    title = job.get("title", "").lower()
    titles = [item.lower() for item in profile.get("target_titles", [])]
    skills = {item.lower() for item in profile.get("skills", [])}
    required = {item.lower() for item in job.get("skills", [])}
    reasons = []
    points = 0

    if job.get("remote"):
        points += 30
        reasons.append("remote")
    elif profile.get("remote_only"):
        return 0, ["excluded: not remote"]
    if any(target in title or title in target for target in titles):
        points += 35
        reasons.append("target title")
    matches = sorted(skills & required)
    points += min(30, len(matches) * 10)
    if matches:
        reasons.append("skills: " + ", ".join(matches))
    seniority = job.get("seniority", "").lower()
    if seniority in profile.get("target_tracks", []):
        points += 5
        reasons.append(seniority + " track")
    return points, reasons


def command_rank(args):
    profile = read_json(PROFILE_PATH, {})
    jobs = read_json(Path(args.jobs), [])
    ranked = []
    for job in jobs:
        points, reasons = score(job, profile)
        if points:
            ranked.append((points, job, reasons))
    for points, job, reasons in sorted(ranked, reverse=True, key=lambda item: item[0]):
        print(f"{points:>3}  {job['title']} — {job['company']} [{job.get('seniority', 'unspecified')}]")
        print(f"     {', '.join(reasons)} | {job.get('url', '')}")


def command_add_example(_args):
    applications = read_json(APPLICATIONS_PATH, [])
    next_id = max((item["id"] for item in applications), default=0) + 1
    applications.append({
        "id": next_id,
        "company": "Example Labs",
        "title": "Junior AI Engineer",
        "status": "ready_for_review",
        "approved_by_candidate": False,
        "notes": "Replace this example with an actual reviewed opening."
    })
    write_applications(applications)
    print(f"Added application {next_id} in ready_for_review.")


def find_application(application_id):
    applications = read_json(APPLICATIONS_PATH, [])
    for application in applications:
        if application["id"] == application_id:
            return applications, application
    raise SystemExit(f"No application with id {application_id}.")


def command_list(_args):
    for item in read_json(APPLICATIONS_PATH, []):
        print(f"{item['id']:>3}  {item['status']:<18} {item['title']} — {item['company']}")


def command_approve(args):
    applications, application = find_application(args.id)
    if application["status"] != "ready_for_review":
        raise SystemExit("Only an application ready for review can be approved.")
    application["status"] = "approved"
    application["approved_by_candidate"] = True
    write_applications(applications)
    print(f"Application {args.id} approved. It may now be submitted manually.")


def command_submit(args):
    applications, application = find_application(args.id)
    if application["status"] != "approved" or not application["approved_by_candidate"]:
        raise SystemExit("Submission blocked: explicit candidate approval is required.")
    application["status"] = "submitted"
    write_applications(applications)
    print(f"Application {args.id} marked submitted after manual completion.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(required=True)
    rank = subcommands.add_parser("rank", help="Rank an imported JSON job list")
    rank.add_argument("jobs")
    rank.set_defaults(func=command_rank)
    for name, function in [("add-example", command_add_example), ("list", command_list)]:
        command = subcommands.add_parser(name)
        command.set_defaults(func=function)
    for name, function in [("approve", command_approve), ("submit", command_submit)]:
        command = subcommands.add_parser(name)
        command.add_argument("id", type=int)
        command.set_defaults(func=function)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
