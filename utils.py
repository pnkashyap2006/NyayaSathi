"""Utility functions for AI Legal Consultant.

Includes sample document loading, markdown report generation, JSON export formatting,
and logging helpers.
"""

import json
from pathlib import Path
from typing import Dict, Optional
from rich.console import Console

from config import SAMPLE_DOCS_DIR
from parser import LegalResponse

console = Console()


def load_sample_documents() -> Dict[str, str]:
    """Loads text files from sample_documents directory into a dictionary.

    Returns:
        Dict[str, str]: Map of document display titles to document content.
    """
    sample_docs = {}
    if not SAMPLE_DOCS_DIR.exists():
        SAMPLE_DOCS_DIR.mkdir(parents=True, exist_ok=True)
        return sample_docs

    for file_path in SAMPLE_DOCS_DIR.glob("*.txt"):
        try:
            doc_name = file_path.stem.replace("_", " ").title()
            content = file_path.read_text(encoding="utf-8")
            sample_docs[doc_name] = content
        except Exception as e:
            console.print(f"[red]Error reading sample file {file_path.name}:[/red] {e}")

    return sample_docs


def export_response_to_markdown(response: LegalResponse) -> str:
    """Formats a LegalResponse model into a clean, professional Markdown report.

    Args:
        response: Validated LegalResponse object.

    Returns:
        str: Formatted Markdown string.
    """
    md_lines = [
        f"# ⚖ AI Legal Consultant Analysis",
        f"### **Topic:** {response.legal_topic}\n",
        f"---",
        f"## 📝 Executive Summary",
        f"{response.summary}\n",
        f"## 📌 Important Points & Key Clauses",
    ]
    for pt in response.important_points:
        md_lines.append(f"- {pt}")

    md_lines.append("\n## ⚖ Risks & Legal Considerations")
    for cons in response.possible_considerations:
        md_lines.append(f"- {cons}")

    md_lines.append("\n## ➡ Suggested Next Steps")
    for step in response.suggested_next_steps:
        md_lines.append(f"- {step}")

    md_lines.extend([
        "\n---",
        f"**📢 Legal Disclaimer:** {response.disclaimer}"
    ])

    return "\n".join(md_lines)


def export_response_to_json_str(response: LegalResponse) -> str:
    """Converts LegalResponse object to formatted JSON string."""
    return json.dumps(response.model_dump(), indent=2)
