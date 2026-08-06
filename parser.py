"""Parser and Pydantic schema definitions for AI Legal Consultant.

Ensures strict JSON response validation, field type checking, and robust fallback repair
for LLM responses.
"""

import json
import re
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, field_validator
from config import DEFAULT_DISCLAIMER


class LegalResponse(BaseModel):
    """Pydantic model representing the mandatory structured legal response.
    
    All fields are validated to ensure exact compliance with the required response format.
    """
    legal_topic: str = Field(
        ...,
        description="The primary legal topic or title of the query analysis."
    )
    summary: str = Field(
        ...,
        description="A concise summary explaining the concept, answering the query, or summarizing the document."
    )
    important_points: List[str] = Field(
        default_factory=list,
        description="Key takeaways, parties involved, critical clauses, or core facts."
    )
    constitutional_articles: List[str] = Field(
        default_factory=list,
        description="Relevant Constitutional Articles."
    )
    related_acts: List[str] = Field(
        default_factory=list,
        description="Relevant Indian Acts or statutes."
    )
    possible_considerations: List[str] = Field(
        default_factory=list,
        description="Risks, obligations, exceptions, or relevant legal factors to consider."
    )
    suggested_next_steps: List[str] = Field(
        default_factory=list,
        description="Actionable, general next steps (e.g. gather evidence, consult licensed attorney)."
    )
    disclaimer: str = Field(
        default=DEFAULT_DISCLAIMER,
        description="Mandatory legal disclaimer stating this is general legal information only."
    )

    @field_validator("legal_topic", "summary", mode="before")
    @classmethod
    def ensure_string_not_empty(cls, v: Any) -> str:
        """Coerce missing or empty string fields to standard defaults."""
        if not v or not isinstance(v, str):
            return "General Legal Analysis"
        return v.strip()

    @field_validator("important_points", "constitutional_articles", "related_acts", "possible_considerations", "suggested_next_steps", mode="before")
    @classmethod
    def ensure_string_list(cls, v: Any) -> List[str]:
        """Coerce single strings or lists into clean list of non-empty strings."""
        if isinstance(v, str):
            return [v.strip()]
        if isinstance(v, list):
            return [str(item).strip() for item in v if item and str(item).strip()]
        return []

    @field_validator("disclaimer", mode="before")
    @classmethod
    def validate_disclaimer(cls, v: Any) -> str:
        """Ensure legal disclaimer is always present."""
        if not v or not isinstance(v, str):
            return DEFAULT_DISCLAIMER
        return v.strip()


def parse_and_validate_legal_json(raw_text: str) -> LegalResponse:
    """Extracts, cleans, parses, and validates JSON text from LLM response.

    Args:
        raw_text: The raw output string from Groq LLM model.

    Returns:
        LegalResponse: Validated Pydantic model instance.

    Raises:
        ValueError: If JSON cannot be extracted or parsed even after repair attempts.
    """
    if not raw_text or not raw_text.strip():
        raise ValueError("LLM returned an empty response.")

    cleaned_text = raw_text.strip()

    # Step 1: Strip markdown codeblocks ```json ... ``` if present
    json_match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", cleaned_text, re.IGNORECASE)
    if json_match:
        cleaned_text = json_match.group(1).strip()
    else:
        # Fallback: Find raw outer JSON object braces { ... }
        brace_match = re.search(r"\{[\s\S]*\}", cleaned_text)
        if brace_match:
            cleaned_text = brace_match.group(0).strip()

    # Step 2: Attempt standard JSON parsing
    try:
        data = json.loads(cleaned_text)
    except json.JSONDecodeError:
        # Auto-repair: Remove trailing commas before } or ]
        repaired = re.sub(r",\s*([\]}])", r"\1", cleaned_text)
        try:
            data = json.loads(repaired)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Failed to parse LLM response as JSON: {exc}\nRaw Text: {raw_text[:200]}") from exc

    # Step 3: Validate with Pydantic
    if not isinstance(data, dict):
        raise ValueError("Parsed JSON is not a key-value object.")

    return LegalResponse(**data)
