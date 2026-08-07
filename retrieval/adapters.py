"""Retrieval Adapters for NyayaSathi.

Provides concrete and extensible adapters for integrating Vector DBs (FAISS, ChromaDB, Pinecone),
LangChain Retrieval, and Government Legal Datasets into the modular knowledge pipeline.
"""

from typing import List, Dict, Any, Optional
from retrieval.base import BaseRetriever, DocumentSnippet


class LocalKnowledgeAdapter(BaseRetriever):
    """Adapter for retrieving curated local Indian statutory data."""

    def __init__(self):
        from knowledge.base import STATUTORY_KNOWLEDGE_BASE
        self._kb = STATUTORY_KNOWLEDGE_BASE

    def retrieve(self, query: str, intent: str = "Legal Question", top_k: int = 3) -> List[DocumentSnippet]:
        q_lower = query.lower()
        results = []

        for category, items in self._kb.items():
            for title, data in items.items():
                keywords = data.get("keywords", [])
                act = data.get("act", "")
                summary = data.get("summary", "")
                details = data.get("details", "")

                # Keyword match score
                score = 0
                if any(kw in q_lower for kw in keywords):
                    score += 2
                if title.lower() in q_lower:
                    score += 3
                if category.replace("_", " ") in q_lower:
                    score += 1

                if score > 0:
                    results.append((score, DocumentSnippet(
                        title=title,
                        content=f"{summary} | Details: {details}",
                        source=act,
                        citation=title,
                        relevance_score=float(score)
                    )))

        # Sort by relevance score descending
        results.sort(key=lambda x: x[0], reverse=True)
        return [doc for _, doc in results[:top_k]]


class VectorDBAdapter(BaseRetriever):
    """Placeholder interface adapter for FAISS / ChromaDB / Pinecone vector indexes.

    Can be enabled when a vector database index path or remote endpoint is configured.
    """

    def __init__(self, provider: str = "faiss", connection_string: Optional[str] = None):
        self.provider = provider
        self.connection_string = connection_string

    def retrieve(self, query: str, intent: str = "Legal Question", top_k: int = 3) -> List[DocumentSnippet]:
        # Ready interface for vector index lookup
        return []


class GovtLegalDatasetAdapter(BaseRetriever):
    """Adapter for official Indian Government legal datasets (IndiaCode, eCourts, Supreme Court portal)."""

    def __init__(self, api_endpoint: Optional[str] = None):
        self.api_endpoint = api_endpoint

    def retrieve(self, query: str, intent: str = "Legal Question", top_k: int = 3) -> List[DocumentSnippet]:
        # Ready interface for official statutory REST API lookup
        return []


class ModularKnowledgeEngine:
    """Unified retrieval interface manager separating knowledge datasets from the UI."""

    def __init__(self):
        self.primary_retriever = LocalKnowledgeAdapter()
        self.vector_retriever = VectorDBAdapter()
        self.govt_retriever = GovtLegalDatasetAdapter()

    def get_context(self, query: str, intent: str = "Legal Question") -> Dict[str, Any]:
        snippets = self.primary_retriever.retrieve(query, intent=intent, top_k=3)

        formatted_parts = []
        sources = []

        for snip in snippets:
            formatted_parts.append(f"• [{snip.source}] {snip.title}: {snip.content}")
            if snip.source not in sources:
                sources.append(snip.source)

        formatted_context = ""
        if formatted_parts:
            formatted_context = "RELEVANT STATUTORY KNOWLEDGE & STATUTE CONTEXT:\n" + "\n".join(formatted_parts)

        return {
            "formatted_context": formatted_context,
            "sources": sources,
            "snippets": snippets
        }
