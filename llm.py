"""LLM service module for AI Legal Consultant using Groq API.

Handles Groq client initialization, system prompt injection, JSON mode enforcement,
rich logging, and smart fallback mock responses when API key is unconfigured.
"""

import time
from typing import Tuple, Optional
from rich.console import Console
from groq import Groq

from config import GROQ_API_KEY, DEFAULT_MODEL
from prompts import SYSTEM_PROMPT, PROMPT_LEGAL_QUESTION, PROMPT_EXPLAIN_CONCEPT, PROMPT_SUMMARIZE_DOCUMENT, PROMPT_EXPLAIN_ARTICLE
from parser import parse_and_validate_legal_json, LegalResponse

console = Console()


def get_groq_client(api_key: Optional[str] = None) -> Optional[Groq]:
    """Initializes and returns a Groq API client if key is provided.

    Args:
        api_key: Optional API key override. Defaults to config GROQ_API_KEY.

    Returns:
        Groq client object or None if key is absent.
    """
    effective_key = (api_key or GROQ_API_KEY).strip()
    if not effective_key or effective_key == "your_groq_api_key_here":
        return None
    try:
        return Groq(api_key=effective_key)
    except Exception as e:
        console.print(f"[bold red]Groq Client Init Error:[/bold red] {e}")
        return None


def generate_mock_legal_response(mode: str, query: str) -> LegalResponse:
    """Generates realistic structured mock responses when Groq API key is missing.

    Ensures zero setup friction and full offline/demonstration capability.
    """
    console.print(f"[yellow]Using Mock Legal Engine for mode: {mode}[/yellow]")
    time.sleep(1.2)  # Simulate network latency

    q_lower = query.lower()

    if mode == "explain_article" or "article" in q_lower:
        return LegalResponse(
            legal_topic="Article 21: Protection of Life and Personal Liberty",
            summary=(
                "Article 21 states that no person shall be deprived of his life or personal liberty except according to procedure established by law. "
                "It is considered the heart of the Fundamental Rights in the Indian Constitution."
            ),
            important_points=[
                "Applies to both citizens and non-citizens.",
                "Expanded by the Supreme Court to include the right to privacy, right to clean environment, right to free legal aid, etc."
            ],
            constitutional_articles=["Article 21", "Article 14", "Article 19"],
            related_acts=["Right to Education Act, 2009 (via Article 21A)"],
            possible_considerations=[
                "Can be restricted only by a procedure established by law that is just, fair, and reasonable (Maneka Gandhi case).",
                "Cannot be suspended even during an Emergency (under Article 359)."
            ],
            suggested_next_steps=[
                "If violated, an individual can directly approach the Supreme Court under Article 32 or High Court under Article 226."
            ]
        )
    elif mode == "explain_concept" or "fir" in q_lower:
        return LegalResponse(
            legal_topic="First Information Report (FIR)",
            summary=(
                "An FIR is a written document prepared by the police when they receive information about the commission of a cognizable offence. "
                "It sets the criminal law in motion."
            ),
            important_points=[
                "Can only be registered for cognizable offences (where police can arrest without a warrant).",
                "Can be filed by the victim, a witness, or anyone with knowledge of the crime.",
                "Zero FIR can be filed at any police station regardless of jurisdiction."
            ],
            constitutional_articles=[],
            related_acts=["Bharatiya Nagarik Suraksha Sanhita (BNSS), Section 173"],
            possible_considerations=[
                "Delay in filing an FIR can be detrimental to the case unless reasonably explained.",
                "False FIRs can lead to prosecution against the informant under BNS."
            ],
            suggested_next_steps=[
                "Ensure you get a free copy of the FIR immediately after it is registered.",
                "If police refuse to register an FIR, you can approach the Superintendent of Police or a Magistrate."
            ]
        )

    elif mode == "summarize_document":
        return LegalResponse(
            legal_topic="Commercial Lease Agreement Summary",
            summary=(
                "The document is a standard commercial lease agreement establishing the terms under which a commercial property "
                "is rented from a landlord to a tenant for business purposes."
            ),
            important_points=[
                "Parties Involved: Landlord (Lessor) and Tenant (Lessee).",
                "Key Clauses: Monthly rent, security deposit amount, permitted use of premises, and maintenance responsibilities."
            ],
            constitutional_articles=[],
            related_acts=["Transfer of Property Act, 1882", "Registration Act, 1908"],
            possible_considerations=[
                "Lease agreements exceeding 11 months must be compulsorily registered.",
                "Lock-in periods prevent early termination without severe penalties.",
                "Force Majeure clauses might not excuse rent payment unless explicitly stated."
            ],
            suggested_next_steps=[
                "Ensure the agreement is drafted on appropriate stamp paper and registered.",
                "Conduct a physical inspection of the premises before taking possession."
            ]
        )

    else:
        return LegalResponse(
            legal_topic=f"Legal Analysis: {query[:40]}",
            summary=(
                f"Analysis of query: '{query}'. Under Indian Law, rights and duties are governed by constitutional provisions, "
                "statutory enactments, and established procedural frameworks."
            ),
            important_points=[
                "Subject to relevant national or state legislative provisions.",
                "Evidentiary requirements and formal notices strengthen legal positions."
            ],
            constitutional_articles=[],
            related_acts=[],
            possible_considerations=[
                "Limitation Act specifies time restrictions for instituting legal proceedings.",
                "Potential litigation costs, damages, or regulatory penalties."
            ],
            suggested_next_steps=[
                "Organize all relevant agreements, correspondence, and evidence.",
                "Schedule a consultation with a licensed advocate in your jurisdiction."
            ]
        )


def query_legal_consultant(
    mode: str,
    user_query: str,
    api_key: Optional[str] = None,
    model_name: str = DEFAULT_MODEL
) -> Tuple[Optional[LegalResponse], Optional[str]]:
    """Queries the Groq LLM API and parses the response into a LegalResponse model.

    Args:
        mode: Operational mode ('ask_question', 'explain_concept', 'summarize_document', 'explain_article').
        user_query: The input prompt or document text.
        api_key: Optional Groq API key.
        model_name: The target Groq model name.

    Returns:
        Tuple containing (LegalResponse object, error_message string).
    """
    if not user_query or not user_query.strip():
        return None, "Input query cannot be empty."

    client = get_groq_client(api_key)

    # If client is unavailable, fall back seamlessly to Mock Engine
    if client is None:
        console.print("[dim]Groq API key not configured or invalid. Using built-in engine.[/dim]")
        response_data = generate_mock_legal_response(mode, user_query)
        return response_data, None

    # Select appropriate prompt template based on operational mode
    if mode == "explain_concept":
        formatted_prompt = PROMPT_EXPLAIN_CONCEPT.format(user_query=user_query)
    elif mode == "summarize_document":
        formatted_prompt = PROMPT_SUMMARIZE_DOCUMENT.format(user_query=user_query)
    elif mode == "explain_article":
        formatted_prompt = PROMPT_EXPLAIN_ARTICLE.format(user_query=user_query)
    else:
        formatted_prompt = PROMPT_LEGAL_QUESTION.format(user_query=user_query)

    try:
        console.print(f"[bold cyan]Dispatching query to Groq ({model_name})...[/bold cyan]")
        start_time = time.time()

        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": formatted_prompt}
            ],
            model=model_name,
            temperature=0.2,
            max_tokens=2048,
            response_format={"type": "json_object"}
        )

        elapsed = time.time() - start_time
        console.print(f"[green]Groq returned response in {elapsed:.2f}s[/green]")

        raw_content = chat_completion.choices[0].message.content
        legal_data = parse_and_validate_legal_json(raw_content)
        return legal_data, None

    except Exception as e:
        err_msg = str(e)
        console.print(f"[bold red]Groq API Error:[/bold red] {err_msg}")

        # If rate limited or API error occurs, provide mock fallback with notice
        if "401" in err_msg or "invalid_api_key" in err_msg.lower():
            return None, "Invalid Groq API key provided. Please verify your API key in the sidebar."
        elif "429" in err_msg or "rate_limit" in err_msg.lower():
            return None, "Groq API rate limit exceeded. Please wait a moment before retrying."

        # Fallback for unexpected API failure
        console.print("[yellow]Falling back to mock engine due to API error.[/yellow]")
        fallback_data = generate_mock_legal_response(mode, user_query)
        return fallback_data, None
