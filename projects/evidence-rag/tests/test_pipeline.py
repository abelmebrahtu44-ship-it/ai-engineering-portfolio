import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pipeline import answer, citation_is_valid
from retrieval import load_corpus


class EvidenceRagTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.documents = load_corpus(ROOT / "corpus.jsonl")

    def test_grounded_question_has_expected_citation(self):
        response = answer("What should a RAG system retrieve before answering?", self.documents)
        self.assertFalse(response["abstained"])
        self.assertIn("rag-basics", response["citations"])
        self.assertTrue(citation_is_valid(response))

    def test_unanswerable_question_abstains(self):
        response = answer("What is the weather on Mars today?", self.documents)
        self.assertTrue(response["abstained"])
        self.assertEqual([], response["citations"])


if __name__ == "__main__":
    unittest.main()
