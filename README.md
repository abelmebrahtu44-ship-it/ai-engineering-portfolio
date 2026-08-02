# Remote AI Job Assistant

A privacy-conscious, approval-first starter for a remote AI job search. It helps you keep a focused pipeline for junior and senior AI roles, rank opportunities, and record tailored application drafts.

## What it does

- Stores an editable candidate profile, including your completed Scrimba AI Engineer Path.
- Ranks imported openings against role titles, remote eligibility, skills, and seniority.
- Tracks applications from `discovered` through `submitted`.
- Refuses to mark an application as submitted unless you explicitly approve it.

It deliberately does **not** automate website logins or submit applications. A human review and final confirmation are required for every application.

## Quick start

Requires Python 3.10+ and no third-party packages.

```bash
python3 assistant.py rank examples/jobs.json
python3 assistant.py add-example
python3 assistant.py list
python3 assistant.py approve 1
python3 assistant.py submit 1
```

The commands create a local `data/applications.json` file (ignored by Git) so personal application history stays on your machine.

## Customize your search

Edit [`config/profile.json`](config/profile.json) to add your résumé-backed skills, years of experience, portfolio, compensation range, and preferred titles. Do not claim a skill or seniority you cannot support in an interview.

To search live sources, use the ranked results as a review queue: export jobs from sources you are authorized to use, place them in the JSON format shown in [`examples/jobs.json`](examples/jobs.json), then run `rank`.

## Status flow

`discovered` → `drafting` → `ready_for_review` → `approved` → `submitted`

Only the `approve` command can move a job to `approved`, and only an approved job can be marked `submitted`.

## Next integrations

- Add permitted job-board/API connectors.
- Generate résumé and cover-letter drafts from user-provided source materials.
- Add a small web dashboard and calendar follow-ups.
