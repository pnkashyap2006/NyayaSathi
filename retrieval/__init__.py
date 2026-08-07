"""Retrieval module for NyayaSathi Indian Legal AI Assistant."""

from retrieval.base import BaseRetriever, DocumentSnippet
from retrieval.adapters import ModularKnowledgeEngine, LocalKnowledgeAdapter, VectorDBAdapter, GovtLegalDatasetAdapter

__all__ = [
    "BaseRetriever",
    "DocumentSnippet",
    "ModularKnowledgeEngine",
    "LocalKnowledgeAdapter",
    "VectorDBAdapter",
    "GovtLegalDatasetAdapter"
]
