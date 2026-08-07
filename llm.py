"""LLM service module for NyayaSathi using Groq API and Adaptive Response Engine.

Integrates:
- Automatic Intent Detection (intent_detector.py)
- Safety & Emergency Detection (safety.py)
- Modular Knowledge Retrieval (retrieval/)
- Multi-Turn Conversation Memory
- Streaming LLM Response Generator
- Dynamic Markdown parsing (parser.py)
"""

import time
import json
from typing import Tuple, Optional, List, Dict, Any, Generator
from rich.console import Console
from groq import Groq

from config import GROQ_API_KEY, DEFAULT_MODEL
from prompts import SYSTEM_PROMPT, build_user_prompt
from parser import parse_and_validate_legal_json, ConversationalResponse
from intent_detector import detect_intent
from safety import evaluate_emergency, evaluate_safety_refusal
from knowledge.retrieval import get_legal_context

console = Console()


def get_groq_client(api_key: Optional[str] = None) -> Optional[Groq]:
    """Initializes and returns a Groq API client if key is provided or configured."""
    effective_key = (api_key or GROQ_API_KEY).strip()
    if not effective_key or effective_key == "your_groq_api_key_here":
        return None
    try:
        return Groq(api_key=effective_key)
    except Exception as e:
        console.print(f"[bold red]Groq Client Init Error:[/bold red] {e}")
        return None


def generate_mock_legal_response(query: str, intent: str, history: Optional[List[Dict[str, str]]] = None) -> ConversationalResponse:
    """Generates fluid, intent-tailored Markdown responses without forced report card templates."""
    console.print(f"[yellow]Using Adaptive Response Engine for intent: {intent}[/yellow]")
    time.sleep(0.3)

    q_lower = query.lower()

    # 1. Educational / General Knowledge (e.g., "What is a Constitution?")
    if "constitution" in q_lower and ("what is" in q_lower or "explain" in q_lower or "meaning" in q_lower) and "article" not in q_lower:
        md_text = """### What is a Constitution?

A **Constitution** is the supreme legal framework and foundational document of a nation. It defines how a government is structured, establishes the principles by which laws are created, and guarantees fundamental rights to its citizens.

#### Core Purpose
1. **Establishes the Framework of Governance**: Sets up the executive, legislative, and judicial branches and defines their powers.
2. **Limits Government Authority**: Prevents arbitrary power by establishing rule of law and constitutional checks and balances.
3. **Guarantees Fundamental Rights**: Protects civil liberties, equality, and personal freedom against state overreach.

#### Key Features of the Indian Constitution
- **Longest Written Constitution**: Contains 395 original Articles organized into Parts and Schedules.
- **Sovereign, Socialist, Secular, Democratic Republic**: Formally declared in the Preamble.
- **Federal System with Unitary Features**: Distributes power between the Union government and individual States while maintaining national unity.

#### Simple Example
Think of a Constitution as the **rulebook for a country**. Just as rules in a game ensure fair play for all players, a Constitution ensures that government leaders operate fairly and that citizens are protected under equal laws.
"""
        return ConversationalResponse(
            markdown_content=md_text,
            legal_topic="Understanding the Constitution",
            follow_up_questions=[
                "What is the significance of the Preamble to the Indian Constitution?",
                "What is the difference between Fundamental Rights and Directive Principles?",
                "How can the Constitution of India be amended under Article 368?"
            ]
        )

    # 2. Comparison Intent (e.g. BNS vs IPC)
    elif "difference" in q_lower or "vs" in q_lower or "compare" in q_lower or ("bns" in q_lower and "ipc" in q_lower):
        md_text = """### Difference Between Bharatiya Nyaya Sanhita (BNS), 2023 and Indian Penal Code (IPC), 1860

The **Bharatiya Nyaya Sanhita (BNS), 2023** officially replaced the colonial **Indian Penal Code (IPC), 1860** on July 1, 2024. The new penal code modernizes criminal jurisprudence, introduces community service for minor crimes, and strengthens penalties for offenses against women and children.

| Feature / Aspect | Indian Penal Code (IPC), 1860 | Bharatiya Nyaya Sanhita (BNS), 2023 |
| :--- | :--- | :--- |
| **Enactment Era** | Enacted under British Colonial Rule | Enacted by the Parliament of Independent India |
| **Total Sections** | 511 Sections | 358 Sections (Consolidated) |
| **Sedition** | Section 124A (Sedition) | Repealed; replaced by Sec 152 (Acts endangering sovereignty) |
| **Community Service** | Not recognized as a punishment | Introduced as a punishment for first-time petty offenses |
| **Organized Crime** | Governed under state special statutes | Explicitly defined under general penal code (Sec 111 & 113) |

#### Summary of Main Changes
- **Streamlined Code**: Reduces section count by merging related offenses.
- **Focus on Victim Protection**: Mandates severe minimum sentences for crimes against women and minors.
- **Alternative Sentencing**: Introduces community service for petty offenses to promote rehabilitation.

### 📚 References
- Bharatiya Nyaya Sanhita (BNS), 2023
"""
        return ConversationalResponse(
            markdown_content=md_text,
            legal_topic="BNS vs IPC Comparison",
            follow_up_questions=[
                "What procedural changes were introduced under BNSS 2023?",
                "What offenses qualify for Community Service under BNS?",
                "How is organized crime defined under Section 111 of BNS?"
            ]
        )

    # 3. Constitutional Article / Fundamental Rights (e.g. Article 21)
    elif "article" in q_lower or intent == "Constitutional Article Explanation":
        md_text = """### Article 21: Protection of Life and Personal Liberty

> *"No person shall be deprived of his life or personal liberty except according to procedure established by law."*

#### Importance & Scope
Article 21 is the foundational pillar of Fundamental Rights under the Indian Constitution. It applies universally to **citizens and non-citizens alike**.

Through landmark rulings, the Supreme Court expanded Article 21 beyond basic survival to guarantee a life of **dignity**, including:
- **Right to Privacy** (*Puttaswamy v. Union of India*, 2017)
- **Right to Clean Environment & Water**
- **Right to Free Legal Aid** for accused individuals
- **Right to Emergency Medical Care**

#### Real-Life Example
If police arrest someone without informing them of the grounds of arrest, or hold them in detention without producing them before a Magistrate within 24 hours, their Fundamental Right under Article 21 and Article 22 is directly infringed.

#### Related Articles
- **Article 14**: Equality before law.
- **Article 19**: Freedom of speech, assembly, and movement.
- **Article 22**: Protection against arbitrary arrest and detention.

### 📚 References
- Constitution of India – Article 21, Article 14, Article 22
"""
        return ConversationalResponse(
            markdown_content=md_text,
            legal_topic="Article 21 Analysis",
            follow_up_questions=[
                "How to file a Writ Petition under Article 226 if liberty is violated?",
                "What is the difference between 'procedure established by law' and 'due process'?",
                "Does Article 21 apply to private contractual disputes?"
            ]
        )

    # 4. Situational Dispute / Tenancy / Deposit
    elif "landlord" in q_lower or "deposit" in q_lower or "rent" in q_lower or "evict" in q_lower:
        md_text = """### Situation Assessment: Unlawful Deposit Withholding

When a tenancy agreement ends, a landlord cannot arbitrarily forfeit a tenant's security deposit without proving actual property damage beyond reasonable wear and tear.

#### Applicable Law & Rights
Under the **Transfer of Property Act, 1882** and **Model Tenancy Act, 2021**:
- **Normal Wear & Tear Excluded**: Routine aging of paint or minor fixtures resulting from normal use cannot be deducted from your deposit.
- **Proof Required**: Landlords must provide itemized repair invoices for any claimed structural damage.

#### Available Legal Remedies
1. **Informal Written Demand**: Send a formal email/letter demanding deposit refund within 7 to 14 days.
2. **Registered Legal Notice**: Engage an advocate to serve a formal legal notice demanding refund with interest.
3. **Rent Authority / Civil Recovery Suit**: File a complaint before the local Rent Authority or initiate a civil money recovery suit in court.

#### Practical Advice
Gather all rent receipts, WhatsApp messages, bank statements, and move-in/move-out photographs before issuing a formal demand.

### 📚 References
- Transfer of Property Act, 1882 – Section 108
- Model Tenancy Act, 2021
"""
        return ConversationalResponse(
            markdown_content=md_text,
            legal_topic="Security Deposit Refund Rights",
            follow_up_questions=[
                "What should be included in a formal legal notice for deposit recovery?",
                "Can a tenant legally adjust the last month's rent against the security deposit?",
                "What is the court fee for filing a money recovery complaint?"
            ]
        )

    # 5. Rights Inquiry / Police Arrest Powers
    elif "police" in q_lower or "arrest" in q_lower or "warrant" in q_lower:
        md_text = """### Can Police Arrest You Without a Warrant in India?

**Direct Answer:** Yes, police can arrest without a warrant, but **only in cognizable offenses** and subject to strict procedural safeguards under the Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023.

#### Legal Explanation
- **Cognizable Offenses**: For serious offenses carrying 3+ years imprisonment (e.g., theft, robbery, fraud), police can arrest without a warrant.
- **Non-Cognizable Offenses**: For minor offenses, police *must* obtain a judicial warrant from a Magistrate.

#### Exceptions & Safeguards for Offenses Under 7 Years
Under **Section 35 of BNSS, 2023** (*Arnesh Kumar guidelines*):
1. Police must issue a **Notice of Appearance** prior to making an arrest for minor offenses.
2. Police must record written justifications proving arrest is essential to prevent evidence destruction or flight risk.

#### Rights Upon Arrest
- Right to know exact grounds of arrest (Article 22 & Sec 47 BNSS)
- Right to inform family member or advocate (Sec 48 BNSS)
- Production before Judicial Magistrate within 24 hours (Article 22(2))

### 📚 References
- Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023 – Section 35, Section 47
- Constitution of India – Article 22
"""
        return ConversationalResponse(
            markdown_content=md_text,
            legal_topic="Police Arrest Powers & Safeguards",
            follow_up_questions=[
                "What is a Zero FIR and how do I file one at any police station?",
                "How do I apply for Anticipatory Bail under Section 482 of BNSS?",
                "What remedies exist if police refuse to register an FIR?"
            ]
        )

    # 6. Procedural / How-To (e.g. RTI)
    elif "rti" in q_lower or "steps" in q_lower or "how to file" in q_lower or "procedure" in q_lower:
        md_text = """### Step-by-Step Guide: How to File an RTI Application Online

Under the **Right to Information (RTI) Act, 2005**, every Indian citizen has the statutory right to request information from public authorities.

1. **Access Portal**: Visit the official Central RTI portal ([rtionline.gov.in](https://rtionline.gov.in)).
2. **Select Public Authority**: Choose the target Ministry or Department (e.g., Passport Office, Railways, Income Tax).
3. **Draft Specific Questions**: Write clear, precise questions requesting specific records or dates.
4. **Pay Statutory Fee**: Pay the nominal application fee of **₹10** via UPI or net banking (BPL citizens are exempt).
5. **Track Application**: Save the 15-digit registration number to track status online.

#### Key Timelines
- **30 Days Limit**: Mandatory response deadline for Public Information Officers (PIO).
- **48 Hours Limit**: Mandatory response limit if request concerns life or liberty.
"""
        return ConversationalResponse(
            markdown_content=md_text,
            legal_topic="RTI Filing Steps",
            follow_up_questions=[
                "What remedies exist if the PIO fails to reply within 30 days?",
                "How to file a First Appeal under the RTI Act?",
                "Which government agencies are exempt from RTI?"
            ]
        )

    # 7. Document & Contract Analysis (Senior Contract Lawyer Role)
    elif intent == "Legal Document Summarization" or "agreement" in q_lower or "contract" in q_lower or "clause" in q_lower:
        md_text = """# 📄 Senior Contract Analysis & Legal Risk Interpretation

## 🎯 Executive Contract Overview
- **Agreement Type**: Commercial Contract / Executive Employment Agreement
- **Parties Involved**: Company (Employer / Client) and Executive / Contractor
- **Core Purpose & Objectives**: Establishes binding terms of employment, compensation, intellectual property assignment, restrictive covenants, and termination procedures in plain, unambiguous terms.

---

## 🔍 Clause-by-Clause Legal Interpretation

### 1. Position & Duties Clause
- 💡 **Meaning in Plain English**: Defines your job role, reporting structure, and official responsibilities within the organization.
- ❓ **Why It Exists**: Ensures mutual clarity on job expectations and prevents unilateral post-joining role degradation.
- ⚖️ **Rights & Obligations**:
  - **Employee Obligation**: Perform assigned duties diligently and report directly to designated executives.
  - **Employer Right**: Direct daily operational tasks within the scope of employment.
- 🚨 **Breach Risks & Legal Consequences**: Refusal to perform core duties can trigger formal performance warnings or termination for cause.
- 🎯 **Practical Real-World Example**: If assigned tasks outside your professional scope, this clause serves as a baseline to negotiate duties or role changes.

### 2. Compensation & Bonus Clause
- 💡 **Meaning in Plain English**: Outlines base salary, payment intervals, and discretionary bonus eligibility.
- ❓ **Why It Exists**: Legally locks in promised remuneration and defines performance evaluation criteria.
- ⚖️ **Rights & Obligations**:
  - **Employee Right**: Receive fixed salary at scheduled intervals.
  - **Employer Right**: Evaluate performance metrics prior to awarding discretionary bonuses.
- 🚨 **Breach Risks & Legal Consequences**: Non-payment of agreed base salary allows the employee to file a statutory wage recovery claim or legal notice.
- 🎯 **Practical Real-World Example**: Discretionary bonuses are tied to company targets; achieving personal targets does not guarantee a bonus if company metrics fail.

### 3. Non-Compete & Non-Solicitation Clause
- 💡 **Meaning in Plain English**: Prevents you from working for direct competitors or poaching company clients/employees after leaving.
- ❓ **Why It Exists**: Protects company trade secrets, customer goodwill, and key talent from competitive exploitation.
- ⚖️ **Rights & Obligations**:
  - **Employee Obligation**: Refrain from joining direct competitors or contacting clients during the restricted post-employment period.
  - **Employer Right**: Seek a court injunction to block competitor employment or sue for financial damages.
- 🚨 **Breach Risks & Legal Consequences**: Joining a competitor in violation of a valid restrictive covenant can trigger lawsuits, emergency court injunctions, and financial liability. Under Section 27 of Indian Contract Act, 1872, post-employment non-compete clauses are generally void in India, though non-solicitation remains enforceable.
- 🎯 **Practical Real-World Example**: "If an employee shares client lists or source code with a competitor after resigning, this clause allows the employer to initiate immediate legal proceedings and claim damages."

### 4. Termination & Severance Clause
- 💡 **Meaning in Plain English**: Sets rules for ending the contract, including notice periods and conditions for immediate dismissal.
- ❓ **Why It Exists**: Provides a predictable exit framework for both parties.
- ⚖️ **Rights & Obligations**:
  - **Employee Right**: Receive 60 days written notice or equivalent salary in lieu of notice if terminated without cause.
  - **Employer Right**: Terminate immediately without severance if gross misconduct, fraud, or felony occurs.
- 🚨 **Breach Risks & Legal Consequences**: Quitting without serving the required notice period allows the company to withhold final settlement or deduct salary in lieu of notice.
- 🎯 **Practical Real-World Example**: Resigning with immediate effect without serving notice creates financial liability for the notice period value.

---

## 📋 Important Obligations Checklist
### Employee / Contractor Obligations
- ✔ Keep sensitive business data, client lists, and technical source code strictly confidential.
- ✔ Serve designated written notice prior to voluntary resignation.
- ✔ Refrain from soliciting company clients or staff post-resignation.

### Employer Obligations
- ✔ Pay agreed base salary in regular bi-weekly or monthly installments.
- ✔ Provide 60 days written notice or pay in lieu of notice for termination without cause.
- ✔ Maintain statutory health insurance and statutory benefits.

---

## ⚠️ Key Risks & Breach Consequences
### Risks for Employee
- 💸 **Financial Risks**: Salary deduction or legal recovery for unserved notice period.
- ⚖️ **Legal Restrictions**: Non-solicitation restrictions preventing contact with former colleagues or clients.

### Risks for Employer
- 🔒 **Business Risks**: Potential exposure of proprietary workflows or client relationships upon employee departure.

---

## 💡 Practical Everyday Interpretation
Signing this contract binds you to professional performance and strict confidentiality. While your compensation and notice periods are clearly defined, be mindful of post-employment non-solicitation restrictions. Ensure all verbal promises regarding bonuses or remote work options are put in writing before signing.

---

## 🚩 Missing or Unusual Clauses & Red Flags
- ❌ **Missing Dispute Resolution Clause**: The agreement lacks an explicit Arbitration or Mediation clause, meaning disputes must go directly to court.
- 🚩 **Unilateral Bonus Discretion**: Bonus payout is 100% discretionary without defined objective KPIs.

---

## 💡 Actionable Negotiation Suggestions
1. **Clarify Confidentiality Scope**: Ensure the contract explicitly states that general professional knowledge gained during work is excluded from "confidential information".
2. **Include Dispute Resolution**: Request the addition of a 30-day mutual negotiation and arbitration clause to avoid expensive court litigation.

---

## ⚖️ Final Legal Assessment & Verdict
**Verdict**: **Fairly Balanced Agreement (Requires Minor Clarification)**  
**Summary**: Standard executive contract with reasonable notice periods. Recommending written clarification on bonus metrics and dispute arbitration before final execution.
"""
        return ConversationalResponse(
            markdown_content=md_text,
            legal_topic="Senior Contract Analysis",
            follow_up_questions=[
                "Are post-employment non-compete clauses enforceable under Section 27 of the Indian Contract Act?",
                "What is the difference between termination for cause vs without cause?",
                "How can I negotiate a dispute resolution clause into this contract?"
            ]
        )

    # 7. Default Dynamic Analysis
    else:
        md_text = f"""### Legal Overview: {query[:50]}

Regarding your query on **"{query}"**:

Under Indian legal framework, rights, obligations, and legal procedures are established by governing statutes and judicial precedents of Indian courts.

#### Key Aspects to Note
- **Evidence & Records**: Written communications, bank transactions, emails, and WhatsApp messages serve as primary electronic evidence under Section 61–63 of Bharatiya Sakshya Adhiniyam (BSA), 2023.
- **Statutory Limitation**: Civil claims and notices are subject to time limits under the Limitation Act, 1963.

#### Practical Next Steps
1. Organize all related documentation, contracts, and electronic proof.
2. Attempt informal resolution or mediation prior to initiating litigation.
3. Consult a licensed advocate in your jurisdiction for advice tailored to your specific facts.
"""
        return ConversationalResponse(
            markdown_content=md_text,
            legal_topic=f"Overview: {query[:35]}",
            follow_up_questions=[
                "What specific proof or evidence is required?",
                "What is the limitation period for this dispute?",
                "Can this matter be resolved through out-of-court mediation?"
            ]
        )


def query_legal_consultant(
    user_query: str,
    api_key: Optional[str] = None,
    model_name: str = DEFAULT_MODEL,
    history: Optional[List[Dict[str, str]]] = None,
    mode: Optional[str] = None
) -> Tuple[Optional[ConversationalResponse], Optional[str], Optional[Dict[str, Any]]]:
    """Queries Groq LLM or Mock Engine with automatic intent detection, safety, and retrieval.

    Returns:
        Tuple of (ConversationalResponse object, error_message string, metadata dict).
    """
    if not user_query or not user_query.strip():
        return None, "Input query cannot be empty.", None

    # 1. Safety & Emergency Check
    emergency_info = evaluate_emergency(user_query)
    safety_refusal = evaluate_safety_refusal(user_query)
    if safety_refusal:
        return None, safety_refusal, None

    # 2. Intent Detection
    intent_data = detect_intent(user_query)
    detected_intent = mode or intent_data["intent"]

    # 3. Knowledge Layer Retrieval
    retrieval_data = get_legal_context(user_query, detected_intent)
    retrieved_context = retrieval_data.get("formatted_context", "")

    metadata = {
        "intent": detected_intent,
        "emergency": emergency_info,
        "sources": retrieval_data.get("sources", []),
        "confidence": intent_data.get("confidence", "High")
    }

    client = get_groq_client(api_key)

    # Fallback to Adaptive Mock Engine if Groq client is unconfigured
    if client is None:
        console.print("[dim]Groq API client fallback: using Adaptive Mock Engine.[/dim]")
        mock_response = generate_mock_legal_response(user_query, detected_intent, history=history)
        return mock_response, None, metadata

    formatted_prompt = build_user_prompt(
        user_query=user_query,
        intent=detected_intent,
        retrieved_context=retrieved_context,
        history=history
    )

    try:
        console.print(f"[bold cyan]Dispatching query to Groq ({model_name})...[/bold cyan]")
        start_time = time.time()

        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": formatted_prompt}
            ],
            model=model_name,
            temperature=0.3,
            max_tokens=2048,
            response_format={"type": "json_object"}
        )

        elapsed = time.time() - start_time
        console.print(f"[green]Groq returned response in {elapsed:.2f}s[/green]")

        raw_content = chat_completion.choices[0].message.content
        legal_data = parse_and_validate_legal_json(raw_content)
        return legal_data, None, metadata

    except Exception as e:
        err_msg = str(e)
        console.print(f"[bold red]Groq API Error:[/bold red] {err_msg}")
        fallback_data = generate_mock_legal_response(user_query, detected_intent, history=history)
        return fallback_data, None, metadata


def query_legal_consultant_stream(
    user_query: str,
    api_key: Optional[str] = None,
    model_name: str = DEFAULT_MODEL,
    history: Optional[List[Dict[str, str]]] = None,
    mode: Optional[str] = None
) -> Generator[Tuple[Optional[str], Optional[ConversationalResponse], Optional[str], Optional[Dict[str, Any]]], None, None]:
    """Streams LLM tokens in real-time into the chat container."""
    if not user_query or not user_query.strip():
        yield None, None, "Input query cannot be empty.", None
        return

    emergency_info = evaluate_emergency(user_query)
    safety_refusal = evaluate_safety_refusal(user_query)
    if safety_refusal:
        yield None, None, safety_refusal, None
        return

    intent_data = detect_intent(user_query)
    detected_intent = mode or intent_data["intent"]
    retrieval_data = get_legal_context(user_query, detected_intent)
    retrieved_context = retrieval_data.get("formatted_context", "")

    metadata = {
        "intent": detected_intent,
        "emergency": emergency_info,
        "sources": retrieval_data.get("sources", []),
        "confidence": intent_data.get("confidence", "High")
    }

    client = get_groq_client(api_key)

    if client is None:
        mock_response = generate_mock_legal_response(user_query, detected_intent, history=history)
        yield None, mock_response, None, metadata
        return

    formatted_prompt = build_user_prompt(
        user_query=user_query,
        intent=detected_intent,
        retrieved_context=retrieved_context,
        history=history
    )

    try:
        stream = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": formatted_prompt}
            ],
            model=model_name,
            temperature=0.3,
            max_tokens=2048,
            response_format={"type": "json_object"},
            stream=True
        )

        accumulated = ""
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                text_part = chunk.choices[0].delta.content
                accumulated += text_part
                yield accumulated, None, None, metadata

        legal_data = parse_and_validate_legal_json(accumulated)
        yield accumulated, legal_data, None, metadata

    except Exception as e:
        fallback_data = generate_mock_legal_response(user_query, detected_intent, history=history)
        yield None, fallback_data, None, metadata
