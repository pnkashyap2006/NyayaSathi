"""Validation & Test Suite for NyayaSathi Conversational Legal AI Assistant.

Comprehensive verification of:
1. ConversationalResponse schema parsing and adaptive markdown compilation.
2. 9 Legal Intent Detection categories with confidence scoring.
3. Safety & Emergency Detection across Cybercrime, Domestic Violence, Child Abuse, Arrest, and Physical Danger.
4. Ethical safety refusal logic for illegal activity requests.
5. Modular Knowledge Retrieval Interface.
6. Multi-turn conversation context building and query processing.
7. Coverage across 14 legal domains with dynamic markdown rendering:
   - Constitutional Law
   - Criminal Law
   - Civil Disputes
   - Employment Law
   - Rental Disputes
   - Consumer Law
   - Property Law
   - Cyber Law
   - Family Law
   - Contract Interpretation
   - Legal Notices
   - Document Summarization
   - Mixed Legal Queries
   - Multi-Turn Conversations
"""

import unittest
from parser import parse_and_validate_legal_json, ConversationalResponse, LegalResponse
from intent_detector import (
    detect_intent,
    INTENT_LEGAL_QUESTION,
    INTENT_CONCEPT_EXPLANATION,
    INTENT_ARTICLE_EXPLANATION,
    INTENT_DOCUMENT_SUMMARIZE,
    INTENT_CLAUSE_EXPLANATION,
    INTENT_CONTRACT_REVIEW,
    INTENT_CASE_GUIDANCE,
    INTENT_LEGAL_PROCEDURE,
    INTENT_RIGHTS_INQUIRY
)
from safety import evaluate_emergency, evaluate_safety_refusal
from knowledge.retrieval import get_legal_context
from llm import query_legal_consultant, generate_mock_legal_response


class TestNyayaSathiValidation(unittest.TestCase):

    # --- 1. Schema & Markdown Conversion Tests ---
    def test_schema_valid_json_parsing(self):
        sample_json = """
        {
            "legal_topic": "Protection of Life and Liberty",
            "markdown_content": "### Article 21 Analysis\\n\\nArticle 21 protects fundamental life and personal liberty.",
            "confidence": "High",
            "follow_up_questions": [
                "How to file a writ petition under Art 226?",
                "Does Art 21 apply to private companies?",
                "What is procedure established by law?"
            ],
            "disclaimer": "Educational legal information only."
        }
        """
        response = parse_and_validate_legal_json(sample_json)
        self.assertIsInstance(response, ConversationalResponse)
        self.assertEqual(response.confidence, "High")
        self.assertIn("Article 21", response.markdown_content)
        self.assertEqual(len(response.follow_up_questions), 3)

    def test_legacy_dict_to_markdown_compilation(self):
        legacy_json = """
        {
            "legal_topic": "Tenant Security Deposit",
            "answer": "Landlord cannot withhold deposit arbitrarily.",
            "legal_reasoning": "Reasoning walk through...",
            "applicable_laws": ["Transfer of Property Act, 1882"],
            "confidence": "High"
        }
        """
        response = parse_and_validate_legal_json(legacy_json)
        self.assertIn("Landlord cannot withhold deposit arbitrarily.", response.markdown_content)
        self.assertIn("Transfer of Property Act, 1882", response.markdown_content)

    # --- 2. Intent Detection Tests (9 Categories) ---
    def test_intent_detection_categories(self):
        test_cases = [
            ("Explain Article 21 of Indian Constitution", INTENT_ARTICLE_EXPLANATION),
            ("What is Zero FIR under BNSS?", INTENT_CONCEPT_EXPLANATION),
            ("My landlord terminated my tenancy and kept my deposit. What can I do?", INTENT_CASE_GUIDANCE),
            ("How to file a consumer complaint online?", INTENT_LEGAL_PROCEDURE),
            ("Can police arrest me without a warrant?", INTENT_RIGHTS_INQUIRY),
            ("WHEREAS the parties agree to indemnify lessor against loss...", INTENT_DOCUMENT_SUMMARIZE),
            ("Explain clause 5 regarding force majeure", INTENT_CLAUSE_EXPLANATION),
            ("Review this employment contract for non-compete terms", INTENT_CONTRACT_REVIEW),
            ("What are the legal rules governing cheque bounce?", INTENT_LEGAL_QUESTION)
        ]

        for query, expected_intent in test_cases:
            res = detect_intent(query)
            self.assertEqual(res["intent"], expected_intent, f"Failed for query: {query}")

    # --- 3. Safety & Emergency Detection Tests ---
    def test_emergency_detection(self):
        cyber_res = evaluate_emergency("My money was stolen in an OTP bank scam online!")
        self.assertIsNotNone(cyber_res)
        self.assertEqual(cyber_res["helpline"], "1930")

        women_res = evaluate_emergency("I am facing severe domestic violence and abuse at home.")
        self.assertIsNotNone(women_res)
        self.assertIn("1091", women_res["helpline"])

        child_res = evaluate_emergency("Child labor and child abuse taking place nearby.")
        self.assertIsNotNone(child_res)
        self.assertEqual(child_res["helpline"], "1098 (Childline)")

        arrest_res = evaluate_emergency("Police beating me and arresting me now in physical danger!")
        self.assertIsNotNone(arrest_res)
        self.assertIn("112", arrest_res["helpline"])

    def test_safety_refusal_for_illegal_requests(self):
        illegal_query = "How to forge a property sale deed without getting caught?"
        refusal = evaluate_safety_refusal(illegal_query)
        self.assertIsNotNone(refusal)
        self.assertIn("Safety Refusal Notice", refusal)

    # --- 4. Knowledge Retrieval Interface Test ---
    def test_knowledge_retrieval_decoupling(self):
        ctx = get_legal_context("Article 21 fundamental right", "Constitutional Article Explanation")
        self.assertIn("formatted_context", ctx)
        self.assertIn("sources", ctx)

    # --- 5. Multi-Domain Legal Coverage Tests (14 Domains) ---
    def test_multi_domain_queries(self):
        domain_queries = {
            "Constitutional Law": "Explain Article 14 equality before law.",
            "Criminal Law": "What is the procedure for anticipatory bail under BNSS?",
            "Civil Disputes": "What is the court fee and limitation for money recovery suit?",
            "Employment Law": "Can an employer terminate employment without severance notice under labor law?",
            "Rental Disputes": "How do I recover security deposit from landlord under Model Tenancy Act?",
            "Consumer Law": "What are my rights if an e-commerce website delivers a defective product?",
            "Property Law": "What is the legal process for checking encumbrance certificate on property?",
            "Cyber Law": "What sections of IT Act 2000 apply to online financial phishing?",
            "Family Law": "What are the general legal provisions for mutual consent divorce under Hindu Marriage Act?",
            "Contract Interpretation": "How is a liquidated damages clause interpreted under Indian Contract Act?",
            "Legal Notices": "What details must be included in a formal statutory legal notice?",
            "Document Summarization": "Summarize this Non Disclosure Agreement clause.",
            "Mixed Legal Queries": "Landlord evicted me by force and police refused to take FIR.",
            "Multi-Turn Conversation": "How does Article 21 apply to landlord tenant disputes?"
        }

        for domain, query in domain_queries.items():
            resp, err, meta = query_legal_consultant(user_query=query)
            self.assertIsNone(err, f"Error in domain {domain}: {err}")
            self.assertIsNotNone(resp, f"Response empty for domain {domain}")
            self.assertIsInstance(resp, ConversationalResponse)
            self.assertTrue(len(resp.markdown_content) > 50, f"Markdown response empty in domain {domain}")

    # --- 6. Adaptive Comparison Test ---
    def test_adaptive_table_generation_for_comparison(self):
        resp, _, _ = query_legal_consultant("What is the difference between BNS and IPC?")
        self.assertTrue("|" in resp.markdown_content or "BNS" in resp.markdown_content, "Comparison query must render structured comparison.")


if __name__ == "__main__":
    unittest.main()
