"""Base retriever interface and statutory knowledge dictionary for NyayaSathi Knowledge Layer.

Defines the abstract contract for legal context retrievers and provides a initial structured
knowledge base for local statutory search.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List

STATUTORY_KNOWLEDGE_BASE: Dict[str, Dict[str, Any]] = {
    "constitutional_rights": {
        "Article 21": {
            "act": "Constitution of India, 1950",
            "summary": "Protection of life and personal liberty.",
            "details": "No person shall be deprived of his life or personal liberty except according to procedure established by law.",
            "keywords": ["article 21", "life", "liberty", "privacy", "eviction", "habeas corpus"]
        },
        "Article 14": {
            "act": "Constitution of India, 1950",
            "summary": "Equality before law and equal protection of the laws.",
            "details": "The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India.",
            "keywords": ["article 14", "equality", "discrimination", "arbitrary"]
        }
    },
    "criminal_law": {
        "Zero FIR": {
            "act": "Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023",
            "summary": "Registration of FIR regardless of jurisdiction.",
            "details": "A Zero FIR allows a victim to file an FIR at any police station irrespective of territorial jurisdiction.",
            "keywords": ["fir", "zero fir", "bnss", "police station", "cognizable"]
        },
        "Anticipatory Bail": {
            "act": "Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023",
            "summary": "Direction for grant of bail to person apprehending arrest.",
            "details": "High Courts and Sessions Courts can grant direction for release on bail prior to arrest.",
            "keywords": ["bail", "anticipatory bail", "arrest", "apprehension"]
        }
    },
    "tenancy_and_property": {
        "Security Deposit Refund": {
            "act": "Transfer of Property Act, 1882 & Model Tenancy Act, 2021",
            "summary": "Refund of deposit post-lease conclusion.",
            "details": "Deductions from security deposit are permissible only for actual unpaid rent or structural damage beyond normal wear and tear.",
            "keywords": ["tenant", "landlord", "deposit", "rent", "eviction", "lease"]
        }
    }
}


class BaseRetriever(ABC):
    """Abstract base class for all legal knowledge retrievers."""

    @abstractmethod
    def retrieve(self, query: str, intent: str = "Legal Question", top_k: int = 3) -> Dict[str, Any]:
        """Retrieves relevant legal context for a user query."""
        pass
