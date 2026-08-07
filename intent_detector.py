"""Intent Detector for NyayaSathi Indian Legal AI Assistant.

Automatically classifies user queries into 9 functional intent categories
so that the LLM system prompt and knowledge retrieval can be dynamically tailored.
"""

import re
from typing import Dict, Any

INTENT_LEGAL_QUESTION = "Legal Question"
INTENT_CONCEPT_EXPLANATION = "Legal Concept Explanation"
INTENT_ARTICLE_EXPLANATION = "Constitutional Article Explanation"
INTENT_DOCUMENT_SUMMARIZE = "Legal Document Summarization"
INTENT_CLAUSE_EXPLANATION = "Clause Explanation"
INTENT_CONTRACT_REVIEW = "Contract Review"
INTENT_CASE_GUIDANCE = "Case Guidance"
INTENT_LEGAL_PROCEDURE = "Legal Procedure"
INTENT_RIGHTS_INQUIRY = "Rights Inquiry"

ALL_INTENTS = [
    INTENT_LEGAL_QUESTION,
    INTENT_CONCEPT_EXPLANATION,
    INTENT_ARTICLE_EXPLANATION,
    INTENT_DOCUMENT_SUMMARIZE,
    INTENT_CLAUSE_EXPLANATION,
    INTENT_CONTRACT_REVIEW,
    INTENT_CASE_GUIDANCE,
    INTENT_LEGAL_PROCEDURE,
    INTENT_RIGHTS_INQUIRY
]


def detect_intent(query: str) -> Dict[str, Any]:
    """Analyzes a user query and returns its detected intent category and metadata.

    Args:
        query: User input string.

    Returns:
        Dict with 'intent' label and 'confidence' score ('High', 'Medium', 'Low').
    """
    if not query or not query.strip():
        return {"intent": INTENT_LEGAL_QUESTION, "confidence": "Low"}

    text = query.strip()
    lower_text = text.lower()

    # 1. Clause Explanation
    if "clause" in lower_text or re.search(r"\bsection\s+\d+\b", lower_text):
        if "explain" in lower_text or "meaning" in lower_text or "what does" in lower_text:
            return {"intent": INTENT_CLAUSE_EXPLANATION, "confidence": "High"}

    # 2. Contract Review & Document Summarization
    contract_terms = ["whereas", "agreement", "indemnify", "lessor", "lessee", "termination clause", "force majeure", "parties hereto"]
    if "review" in lower_text and ("contract" in lower_text or "agreement" in lower_text or "deed" in lower_text):
        return {"intent": INTENT_CONTRACT_REVIEW, "confidence": "High"}

    if len(text) > 280 or "summarize" in lower_text or any(kw in lower_text for kw in contract_terms):
        return {"intent": INTENT_DOCUMENT_SUMMARIZE, "confidence": "High"}

    # 3. Constitutional Article Explanation
    if re.search(r"\barticle\s+\d+[a-z]?\b", lower_text) or "preamble" in lower_text or "directive principles" in lower_text:
        return {"intent": INTENT_ARTICLE_EXPLANATION, "confidence": "High"}

    # 4. Legal Concept Explanation
    concept_starters = ["explain ", "what is ", "define ", "meaning of "]
    short_concepts = ["fir", "zero fir", "bail", "anticipatory bail", "rti", "nda", "posh", "bns", "bnss", "bsa", "power of attorney", "habeas corpus", "arbitration"]
    if any(lower_text.startswith(cs) for cs in concept_starters) or any(sc == lower_text or f" {sc} " in f" {lower_text} " for sc in short_concepts):
        return {"intent": INTENT_CONCEPT_EXPLANATION, "confidence": "High"}

    # 5. Rights Inquiry
    rights_triggers = ["my rights", "right to", "can police arrest", "can landlord evict", "employee rights", "consumer rights", "rights of tenant", "rights of accused"]
    if any(rt in lower_text for rt in rights_triggers) or "right" in lower_text:
        return {"intent": INTENT_RIGHTS_INQUIRY, "confidence": "High"}

    # 6. Case Guidance / Situational Scenario
    situational_triggers = [
        "my landlord", "my employer", "terminated", "evicted", "deposit refund",
        "stole", "cheated", "blackmailed", "received a notice", "what should i do", "what can i do", "facing trouble"
    ]
    if any(st in lower_text for st in situational_triggers):
        return {"intent": INTENT_CASE_GUIDANCE, "confidence": "High"}

    # 7. Legal Procedure
    procedure_triggers = ["how to file", "procedure to", "process of", "court fee", "jurisdiction", "where to complain", "draft notice", "how do i"]
    if any(pt in lower_text for pt in procedure_triggers):
        return {"intent": INTENT_LEGAL_PROCEDURE, "confidence": "High"}

    # Default fallback
    return {"intent": INTENT_LEGAL_QUESTION, "confidence": "Medium"}
