"""Base retrieval interface for NyayaSathi Indian Legal AI Assistant.

Provides abstract data models and base class definitions for vector databases,
RAG pipelines, and official legal repository interfaces.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class DocumentSnippet(BaseModel):
    """Data model representing a retrieved legal document or statutory passage."""
    title: str = Field(..., description="Title of the statutory provision, Act, or Article.")
    content: str = Field(..., description="Text content or summary of the legal snippet.")
    source: str = Field(..., description="Authoritative source (e.g. Constitution of India, BNS 2023).")
    citation: Optional[str] = Field(None, description="Exact Section, Article, or Clause reference.")
    relevance_score: float = Field(1.0, description="Similarity or relevance score from retriever.")


class BaseRetriever(ABC):
    """Abstract Base Class for legal knowledge retrieval engines."""

    @abstractmethod
    def retrieve(self, query: str, intent: str = "Legal Question", top_k: int = 3) -> List[DocumentSnippet]:
        """Retrieves top_k relevant legal snippets for a given query and intent.

        Args:
            query: User's legal query string.
            intent: Detected intent category.
            top_k: Number of snippets to return.

        Returns:
            List[DocumentSnippet]: List of retrieved legal snippets.
        """
        pass
