"""Legal Context Retriever implementation for NyayaSathi.

Bridges local statutory databases (Constitution, BNS, BNSS, BSA, Consumer Protection, IT Act, POSH, RERA, etc.)
with the modular retrieval adapter interface (retrieval.adapters.ModularKnowledgeEngine).
"""

from typing import Dict, Any, List
from data.constitution import FUNDAMENTAL_RIGHTS
from data.landmark_acts import MAJOR_LAWS
from retrieval.adapters import ModularKnowledgeEngine


class LegalContextRetriever:
    """Retrieves authoritative context from Indian law datasets."""

    def __init__(self):
        self.rights = FUNDAMENTAL_RIGHTS
        self.acts = MAJOR_LAWS
        self.act_details = {}
        self.modular_engine = ModularKnowledgeEngine()

    def retrieve(self, query: str, intent: str = "Legal Question", top_k: int = 3) -> Dict[str, Any]:
        """Queries local legal databases and modular adapters to format context string for prompt builder."""
        if not query or not query.strip():
            return {"formatted_context": "", "sources": []}

        lower_query = query.lower()
        matched_sources = []
        context_chunks = []

        # 1. Search Fundamental Rights & Articles
        for right in self.rights:
            art_str = right.get("articles_range", right.get("articles", ""))
            desc_str = right.get("overview", right.get("description", ""))
            ex_str = right.get("simple_meaning", right.get("example", ""))
            if any(kw in lower_query for kw in right["title"].lower().split() if len(kw) > 3) or (art_str and any(art in lower_query for art in art_str.lower().split())):
                matched_sources.append(f"Constitution of India: {right['title']} ({art_str})")
                context_chunks.append(f"PROVISION: {right['title']} ({art_str})\nDESCRIPTION: {desc_str}\nEXAMPLE: {ex_str}")

        # 2. Search Landmark Acts (BNS, BNSS, BSA, Consumer Protection, IT Act, etc.)
        for act in self.acts:
            act_title = act["title"].lower()
            if act_title in lower_query or any(kw in lower_query for kw in act["title"].lower().split() if len(kw) > 3):
                matched_sources.append(f"Statute: {act['title']}")
                context_chunks.append(f"ACT: {act['title']}\nOVERVIEW: {act['overview']}")

        # 3. Search Detailed Act Sections
        for act_name, detail in self.act_details.items():
            if act_name.lower() in lower_query or any(kw in lower_query for kw in act_name.lower().split() if len(kw) > 3):
                key_provisions = detail.get("key_provisions", [])
                prov_str = "\n".join([f"- {p['section']}: {p['desc']}" for p in key_provisions])
                context_chunks.append(f"STATUTORY PROVISIONS ({act_name}):\n{prov_str}")
                matched_sources.append(f"Statute Provisions: {act_name}")

        # 4. Integrate Modular Knowledge Engine (retrieval layer)
        adapter_res = self.modular_engine.get_context(query, intent)
        if adapter_res.get("sources"):
            for src in adapter_res["sources"]:
                if src not in matched_sources:
                    matched_sources.append(src)

        # Limit to top_k chunks
        context_chunks = context_chunks[:top_k]
        matched_sources = matched_sources[:top_k]

        formatted_context = ""
        if context_chunks:
            formatted_context = "VERIFIED LEGAL STATUTORY CONTEXT:\n" + "\n---\n".join(context_chunks)
        elif adapter_res.get("formatted_context"):
            formatted_context = adapter_res["formatted_context"]

        return {
            "formatted_context": formatted_context,
            "sources": matched_sources
        }


# Global instance helper
_retriever_instance = LegalContextRetriever()


def get_legal_context(query: str, intent: str = "Legal Question") -> Dict[str, Any]:
    """Helper function to retrieve legal context for prompt builder."""
    return _retriever_instance.retrieve(query, intent)
