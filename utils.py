"""Utility functions for NyayaSathi Indian Legal AI Assistant.

Includes document text extraction (.pdf, .docx, .txt), markdown report generation,
JSON export formatting, sample document backend loader, and logging helpers.
"""

import io
import json
from pathlib import Path
from typing import Dict, Optional, Any
from rich.console import Console

from config import SAMPLE_DOCS_DIR
from parser import ConversationalResponse

console = Console()


def extract_text_from_file(uploaded_file) -> str:
    """Extracts raw text content from uploaded PDF, DOCX, or TXT file objects.

    Args:
        uploaded_file: Streamlit UploadedFile object.

    Returns:
        str: Extracted text string.
    """
    if uploaded_file is None:
        return ""

    filename = uploaded_file.name.lower()

    # 1. TXT File Processing
    if filename.endswith(".txt"):
        try:
            return uploaded_file.read().decode("utf-8")
        except UnicodeDecodeError:
            uploaded_file.seek(0)
            return uploaded_file.read().decode("latin-1", errors="ignore")

    # 2. PDF File Processing (pypdf)
    elif filename.endswith(".pdf"):
        try:
            import pypdf
            reader = pypdf.PdfReader(io.BytesIO(uploaded_file.read()))
            text_parts = []
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text_parts.append(extracted)
            return "\n\n".join(text_parts)
        except Exception as e:
            console.print(f"[red]PDF Extraction Error ({filename}):[/red] {e}")
            return f"[Error reading PDF file '{uploaded_file.name}': {e}]"

    # 3. DOCX File Processing (python-docx)
    elif filename.endswith(".docx") or filename.endswith(".doc"):
        try:
            import docx
            doc = docx.Document(io.BytesIO(uploaded_file.read()))
            full_text = [para.text for para in doc.paragraphs if para.text.strip()]
            return "\n\n".join(full_text)
        except Exception as e:
            console.print(f"[red]DOCX Extraction Error ({filename}):[/red] {e}")
            return f"[Error reading DOCX file '{uploaded_file.name}': {e}]"

    # Fallback default read
    try:
        return uploaded_file.read().decode("utf-8", errors="ignore")
    except Exception:
        return ""


def load_sample_documents() -> Dict[str, str]:
    """Backend utility to load sample documents for testing/modular reuse.

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


def export_response_to_markdown(response: Any) -> str:
    """Formats a ConversationalResponse model into a clean Markdown export report."""
    if hasattr(response, "markdown_content"):
        content = response.markdown_content
        topic = getattr(response, "legal_topic", "Legal Research Analysis")
        disclaimer = getattr(response, "disclaimer", "")

        md_lines = [
            f"# ⚖ NyayaSathi — {topic}\n",
            content,
            "\n---",
            f"**📢 Legal Notice:** {disclaimer}"
        ]
        return "\n".join(md_lines)

    return str(response)


def export_response_to_json_str(response: Any) -> str:
    """Converts response object to formatted JSON string."""
    if hasattr(response, "model_dump"):
        return json.dumps(response.model_dump(), indent=2)
    elif hasattr(response, "__dict__"):
        return json.dumps(response.__dict__, indent=2)
    return json.dumps({"content": str(response)}, indent=2)
