"""Parser and response formatter definitions for NyayaSathi Conversational AI Assistant.

Converts structured LLM reasoning and JSON payloads into fluid, adaptive, rich Markdown responses
resembling ChatGPT, Claude, or Perplexity. Removes rigid form-filling and report-card JSON feeling.
"""

import json
import re
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, field_validator
from config import DEFAULT_DISCLAIMER


class ConversationalResponse(BaseModel):
    """Pydantic model representing a fluid, adaptive conversational legal response."""
    
    markdown_content: str = Field(
        ...,
        description="The primary, dynamically formatted rich Markdown response."
    )
    follow_up_questions: List[str] = Field(
        default_factory=list,
        description="3 to 5 relevant suggested follow-up question chips."
    )
    confidence: str = Field(
        default="High",
        description="Confidence level: High, Medium, or Low."
    )
    disclaimer: str = Field(
        default=DEFAULT_DISCLAIMER,
        description="Mandatory non-lawyer general legal information disclaimer."
    )
    legal_topic: str = Field(
        default="Legal Research Analysis",
        description="Short title or topic summary."
    )
    references: List[str] = Field(
        default_factory=list,
        description="Authoritative legal references cited naturally."
    )

    @field_validator("markdown_content", mode="before")
    @classmethod
    def ensure_markdown_str(cls, v: Any) -> str:
        if not v or not isinstance(v, str):
            return "Analysis complete."
        return v.strip()

    @field_validator("confidence", mode="before")
    @classmethod
    def validate_confidence(cls, v: Any) -> str:
        if isinstance(v, str):
            cleaned = v.strip().capitalize()
            if cleaned in ["High", "Medium", "Low"]:
                return cleaned
        return "High"

    @field_validator("follow_up_questions", "references", mode="before")
    @classmethod
    def ensure_string_list(cls, v: Any) -> List[str]:
        if isinstance(v, str):
            return [v.strip()]
        if isinstance(v, list):
            return [str(item).strip() for item in v if item and str(item).strip()]
        return []

    @property
    def answer(self) -> str:
        """Backward compatibility helper property."""
        return self.markdown_content

    @property
    def legal_reasoning(self) -> str:
        return self.markdown_content


# Alias LegalResponse to ConversationalResponse for full backward compatibility
LegalResponse = ConversationalResponse


def parse_and_validate_legal_json(raw_text: str) -> ConversationalResponse:
    """Extracts, cleans, parses, and validates LLM output into a fluid ConversationalResponse.

    If the LLM returns raw Markdown or JSON with 'markdown_content', 'answer', or legacy keys,
    it automatically formats the content into rich, natural Markdown.
    """
    if not raw_text or not raw_text.strip():
        raise ValueError("LLM returned an empty response.")

    cleaned_text = raw_text.strip()

    # Step 1: Check if output is raw markdown text (not JSON enclosed)
    if not (cleaned_text.startswith("{") or "```json" in cleaned_text.lower()):
        return ConversationalResponse(
            markdown_content=cleaned_text,
            follow_up_questions=[
                "What specific documents do I need for proof?",
                "What is the statutory limitation period under Indian law?",
                "Can this issue be resolved out-of-court via mediation?"
            ]
        )

    # Step 2: Strip markdown codeblocks ```json ... ``` if present
    json_match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", cleaned_text, re.IGNORECASE)
    if json_match:
        cleaned_text = json_match.group(1).strip()
    else:
        brace_match = re.search(r"\{[\s\S]*\}", cleaned_text)
        if brace_match:
            cleaned_text = brace_match.group(0).strip()

    # Step 3: Attempt JSON parsing
    try:
        data = json.loads(cleaned_text)
    except json.JSONDecodeError:
        repaired = re.sub(r",\s*([\]}])", r"\1", cleaned_text)
        try:
            data = json.loads(repaired)
        except json.JSONDecodeError:
            # Fallback: treat as raw text markdown if JSON repair fails
            return ConversationalResponse(
                markdown_content=raw_text.strip(),
                follow_up_questions=[
                    "What evidence should I gather?",
                    "What is the procedure under BNSS / Contract Act?",
                    "How to approach the local authority or advocate?"
                ]
            )

    if not isinstance(data, dict):
        return ConversationalResponse(markdown_content=str(data))

    # Step 4: Extract or compile rich markdown content
    markdown_content = ""

    if "markdown_content" in data and data["markdown_content"]:
        markdown_content = data["markdown_content"]
    elif "markdown_response" in data and data["markdown_response"]:
        markdown_content = data["markdown_response"]
    else:
        # Convert legacy or structured dict fields into natural conversational markdown
        parts = []
        if data.get("legal_topic"):
            parts.append(f"### 📌 {data['legal_topic']}\n")

        if data.get("answer"):
            parts.append(f"{data['answer']}\n")
        elif data.get("summary"):
            parts.append(f"{data['summary']}\n")

        if data.get("issue_identified"):
            parts.append(f"**Issue Identified:** {data['issue_identified']}\n")

        if data.get("legal_reasoning"):
            parts.append(f"### 🧠 Legal Analysis & Reasoning\n{data['legal_reasoning']}\n")

        if data.get("important_points"):
            pts = data["important_points"]
            if isinstance(pts, list) and pts:
                parts.append("### 🔑 Key Considerations & Takeaways\n" + "\n".join([f"- {p}" for p in pts]) + "\n")

        if data.get("recommended_next_steps"):
            steps = data["recommended_next_steps"]
            if isinstance(steps, list) and steps:
                parts.append("### ➡ Recommended Next Steps\n" + "\n".join([f"1. {s}" for i, s in enumerate(steps)]) + "\n")

        # Natural legal references section at end
        articles = data.get("constitutional_articles", [])
        laws = data.get("applicable_laws", []) or data.get("related_acts", [])
        all_refs = []
        if isinstance(articles, list):
            all_refs.extend(articles)
        if isinstance(laws, list):
            all_refs.extend(laws)

        if all_refs:
            parts.append("### 📚 Authoritative Legal References\n" + "\n".join([f"- **{r}**" for r in all_refs]) + "\n")

        markdown_content = "\n".join(parts) if parts else raw_text.strip()

    follow_ups = data.get("follow_up_questions", [])
    if not isinstance(follow_ups, list) or not follow_ups:
        follow_ups = [
            "What specific documents should I preserve?",
            "What is the limitation period for this dispute under Indian law?",
            "How do I consult a licensed advocate for court filing?"
        ]

    topic = data.get("legal_topic", "Legal Research Analysis")
    confidence = data.get("confidence", "High")
    disclaimer = data.get("disclaimer", DEFAULT_DISCLAIMER)

    # Collect list of references
    articles = data.get("constitutional_articles", [])
    laws = data.get("applicable_laws", []) or data.get("related_acts", [])
    refs = []
    if isinstance(articles, list):
        refs.extend(articles)
    if isinstance(laws, list):
        refs.extend(laws)

    return ConversationalResponse(
        markdown_content=markdown_content,
        follow_up_questions=follow_ups,
        confidence=confidence,
        disclaimer=disclaimer,
        legal_topic=topic,
        references=refs
    )
