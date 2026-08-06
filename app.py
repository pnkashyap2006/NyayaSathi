"""AI Legal Consultant - Main Streamlit Application Entrypoint.

A production-quality Python web application providing structured general legal information,
contract summarization, and concept explanation using the Groq API.
"""

import time
import streamlit as st

# Page Configuration MUST be the first Streamlit command
st.set_page_config(
    page_title="AI Legal Consultant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

from config import APP_NAME, APP_TAGLINE, DEFAULT_MODEL
from components.animations import inject_custom_css, render_hero_banner, render_footer
from components.sidebar import render_sidebar
from components.cards import render_response_cards, render_alert_card
from components.preamble import render_preamble
from components.constitution import render_constitution
from components.rights_duties import render_rights_duties
from components.judiciary import render_judiciary
from components.laws import render_laws
from llm import query_legal_consultant
from utils import load_sample_documents


def main():
    # Inject CSS Design Tokens & Glassmorphism Styles
    inject_custom_css()

    # Render Sidebar Navigation
    sidebar_config = render_sidebar()
    current_mode = sidebar_config["mode"]
    api_key = sidebar_config["api_key"]
    selected_model = sidebar_config["selected_model"]

    # Main Page Routing
    if current_mode == "home":
        render_home_page()
    elif current_mode == "preamble":
        render_preamble()
    elif current_mode == "constitution":
        render_constitution()
    elif current_mode == "rights" or current_mode == "duties":
        render_rights_duties()
    elif current_mode == "judiciary":
        render_judiciary()
    elif current_mode == "laws":
        render_laws()
    elif current_mode == "ai_assistant":
        render_ask_question_page(api_key, selected_model)
    elif current_mode == "summarize_document":
        render_summarize_document_page(api_key, selected_model)
    elif current_mode == "about":
        render_about_page()

    # Render Sticky Footer
    render_footer()


def render_home_page():
    """Renders the high-impact landing page with feature cards and quick starters."""
    render_hero_banner()

    st.markdown("<br>", unsafe_allow_html=True)

    # Feature Grid
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="glass-card" style="text-align: center; min-height: 250px;">
                <div style="font-size: 2.8rem; margin-bottom: 0.8rem;">📜</div>
                <div style="font-size: 1.25rem; font-weight: 700; color: #D4AF37; margin-bottom: 0.5rem;">The Constitution</div>
                <p style="color: #E2E8F0; font-size: 0.95rem; line-height: 1.6;">
                    Explore the fundamental law of India. From the Preamble to the Directive Principles.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Explore Constitution ➡", key="btn_home_const", use_container_width=True):
            st.session_state.navigation_mode = "constitution"
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class="glass-card" style="text-align: center; min-height: 250px;">
                <div style="font-size: 2.8rem; margin-bottom: 0.8rem;">⚖️</div>
                <div style="font-size: 1.25rem; font-weight: 700; color: #FF9933; margin-bottom: 0.5rem;">Legal Assistant</div>
                <p style="color: #E2E8F0; font-size: 0.95rem; line-height: 1.6;">
                    Ask questions about Bharatiya Nyaya Sanhita, Consumer Protection Act, and more.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Ask Legal Question ➡", key="btn_home_ask", use_container_width=True):
            st.session_state.navigation_mode = "ai_assistant"
            st.rerun()

    with col3:
        st.markdown(
            """
            <div class="glass-card" style="text-align: center; min-height: 250px;">
                <div style="font-size: 2.8rem; margin-bottom: 0.8rem;">📄</div>
                <div style="font-size: 1.25rem; font-weight: 700; color: #138808; margin-bottom: 0.5rem;">Summarize Documents</div>
                <p style="color: #E2E8F0; font-size: 0.95rem; line-height: 1.6;">
                    Paste contracts or legal notices to extract important clauses, risks, and related Acts.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Summarize Document ➡", key="btn_home_doc", use_container_width=True):
            st.session_state.navigation_mode = "summarize_document"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Quick Start Preset Triggers Banner
    st.markdown(
        """
        <div class="glass-card" style="border-left: 5px solid #FF9933;">
            <div class="card-header">⚡ Quick Start Examples</div>
            <p style="color: #CBD5E1; margin-bottom: 1rem;">
                Click any preset below to instantly jump into query analysis:
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    qcol1, qcol2, qcol3 = st.columns(3)

    with qcol1:
        if st.button("📜 Explain Article 21", use_container_width=True):
            st.session_state.preset_query = "Explain Article 21 of the Indian Constitution."
            st.session_state.navigation_mode = "ai_assistant"
            st.rerun()

    with qcol2:
        if st.button("⚖️ What is Zero FIR?", use_container_width=True):
            st.session_state.preset_query = "What is a Zero FIR under BNSS?"
            st.session_state.navigation_mode = "ai_assistant"
            st.rerun()

    with qcol3:
        if st.button("🛡️ Right to Information", use_container_width=True):
            st.session_state.preset_query = "How do I file an RTI?"
            st.session_state.navigation_mode = "ai_assistant"
            st.rerun()


def render_ask_question_page(api_key: str, model_name: str):
    """Renders Mode 1: Ask Legal Question Interface."""
    st.markdown("<h2 style='color: #F8FAFC;'>❓ Ask a Legal Question</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8;'>Get structured general legal information on rights, remedies, and procedures.</p>", unsafe_allow_html=True)

    # Preset selector buttons
    st.markdown("<div style='font-size: 0.9rem; font-weight: 600; color: #38BDF8; margin-bottom: 0.4rem;'>Sample Questions:</div>", unsafe_allow_html=True)
    pcol1, pcol2, pcol3 = st.columns(3)

    preset_val = st.session_state.pop("preset_query", "")

    with pcol1:
        if st.button("Explain Article 21", key="p1"):
            preset_val = "Explain Article 21 of the Indian Constitution."

    with pcol2:
        if st.button("What is Zero FIR?", key="p2"):
            preset_val = "What is a Zero FIR under BNSS?"

    with pcol3:
        if st.button("Right to Information", key="p3"):
            preset_val = "How do I file an RTI?"

    # Input Text Area
    user_input = st.text_area(
        label="Enter your legal question:",
        value=preset_val if preset_val else st.session_state.get("q_input", ""),
        height=140,
        placeholder="Type your question here (e.g. What are my rights if my employment is terminated without notice?)...",
        key="q_input_field"
    )

    if st.button("⚖️ Analyze Legal Query", use_container_width=True, key="btn_submit_q"):
        if not user_input.strip():
            render_alert_card("Empty Query Input", "Please enter a valid legal question before submitting.", alert_type="warning")
            return

        run_legal_analysis(mode="ask_question", user_query=user_input, api_key=api_key, model_name=model_name)

    # Render previous cached response if exists
    if "last_response_ask_question" in st.session_state:
        st.markdown("<br><h3 style='color: #38BDF8;'>Analysis Result</h3>", unsafe_allow_html=True)
        render_response_cards(st.session_state.last_response_ask_question)


def render_explain_concept_page(api_key: str, model_name: str):
    """Renders Mode 2: Explain Legal Concept Interface."""
    st.markdown("<h2 style='color: #F8FAFC;'>📚 Explain Legal Concept</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8;'>Deconstruct complex legal terminology, contracts, and statutory concepts.</p>", unsafe_allow_html=True)

    # Preset concept buttons
    st.markdown("<div style='font-size: 0.9rem; font-weight: 600; color: #8B5CF6; margin-bottom: 0.4rem;'>Popular Concepts:</div>", unsafe_allow_html=True)
    ccol1, ccol2, ccol3, ccol4 = st.columns(4)

    preset_concept = ""
    with ccol1:
        if st.button("Non Disclosure Agreement", key="c1"):
            preset_concept = "Non Disclosure Agreement"
    with ccol2:
        if st.button("Power of Attorney", key="c2"):
            preset_concept = "Power of Attorney"
    with ccol3:
        if st.button("Arbitration", key="c3"):
            preset_concept = "Arbitration"
    with ccol4:
        if st.button("FIR (First Info Report)", key="c4"):
            preset_concept = "FIR"

    user_concept = st.text_input(
        label="Enter legal concept or term:",
        value=preset_concept if preset_concept else st.session_state.get("c_input", ""),
        placeholder="e.g. Force Majeure, Intellectual Property, Indenture...",
        key="c_input_field"
    )

    if st.button("🔍 Explain Concept", use_container_width=True, key="btn_submit_c"):
        if not user_concept.strip():
            render_alert_card("Empty Concept Input", "Please enter a legal concept or select a preset.", alert_type="warning")
            return

        run_legal_analysis(mode="explain_concept", user_query=user_concept, api_key=api_key, model_name=model_name)

    if "last_response_explain_concept" in st.session_state:
        st.markdown("<br><h3 style='color: #8B5CF6;'>Concept Explanation Result</h3>", unsafe_allow_html=True)
        render_response_cards(st.session_state.last_response_explain_concept)


def render_summarize_document_page(api_key: str, model_name: str):
    """Renders Mode 3: Summarize Legal Document Interface."""
    st.markdown("<h2 style='color: #F8FAFC;'>📄 Summarize Legal Document</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8;'>Extract executive summary, parties, important clauses, risks, obligations, and deadlines.</p>", unsafe_allow_html=True)

    # Sample Document Selector
    sample_docs = load_sample_documents()
    selected_sample = st.selectbox(
        label="Load a Sample Document (Optional):",
        options=["-- Select a Sample Document --"] + list(sample_docs.keys())
    )

    initial_doc_text = ""
    if selected_sample and selected_sample != "-- Select a Sample Document --":
        initial_doc_text = sample_docs.get(selected_sample, "")

    user_doc = st.text_area(
        label="Paste legal text or contract snippet below:",
        value=initial_doc_text if initial_doc_text else st.session_state.get("d_input", ""),
        height=220,
        placeholder="Paste contract text, agreement clauses, or legal notice here...",
        key="d_input_field"
    )

    if st.button("⚡ Generate Structured Summary", use_container_width=True, key="btn_submit_d"):
        if not user_doc.strip():
            render_alert_card("Empty Document Input", "Please paste legal text or select a sample document.", alert_type="warning")
            return

        run_legal_analysis(mode="summarize_document", user_query=user_doc, api_key=api_key, model_name=model_name)

    if "last_response_summarize_document" in st.session_state:
        st.markdown("<br><h3 style='color: #06B6D4;'>Document Summary Breakdown</h3>", unsafe_allow_html=True)
        render_response_cards(st.session_state.last_response_summarize_document)


def render_about_page():
    """Renders the About section with architecture info and technology stack."""
    st.markdown("<h2 style='color: #F8FAFC;'>ℹ️ About AI Legal Consultant</h2>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="glass-card" style="border-left: 5px solid #38BDF8;">
            <div class="card-header">🎯 Project Mission</div>
            <p style="color: #CBD5E1; line-height: 1.7;">
                <strong>AI Legal Consultant</strong> bridges the gap between complex legal jargon and everyday user understanding.
                Powered by Groq's high-speed inference engine, Pydantic validation, and Streamlit, it provides reliable, structured, 
                and instant general legal information without the cost or friction of traditional initial research.
            </p>
        </div>

        <div class="glass-card" style="border-left: 5px solid #8B5CF6;">
            <div class="card-header">🛠️ Technology Stack</div>
            <ul class="card-list">
                <li><strong>Python 3.11+</strong>: Core application logic</li>
                <li><strong>Groq API</strong>: Ultra-fast LLM inference (Llama-3.3-70b-versatile)</li>
                <li><strong>Streamlit</strong>: Modern web client framework</li>
                <li><strong>Pydantic v2</strong>: Strict JSON schema definition & response validation</li>
                <li><strong>Rich</strong>: High-fidelity terminal logging & diagnostics</li>
                <li><strong>Vanilla CSS</strong>: Custom dark theme glassmorphic design system</li>
            </ul>
        </div>

        <div class="glass-card" style="border-left: 5px solid #EF4444; background: rgba(239, 68, 68, 0.05);">
            <div class="card-header" style="color: #F87171;">⚠️ Compliance & Legal Notice</div>
            <p style="color: #FCA5A5; line-height: 1.6;">
                This application does not provide attorney-client representation or formal legal advice.
                Outputs are generated by an artificial intelligence model for educational and informational purposes only.
                Always consult a licensed attorney in your jurisdiction prior to taking legal action or executing binding agreements.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def run_legal_analysis(mode: str, user_query: str, api_key: str, model_name: str):
    """Executes the legal query with progress indicators and saves response into session state."""
    progress_placeholder = st.empty()

    with progress_placeholder.container():
        st.markdown("<div class='shimmer-progress'></div>", unsafe_allow_html=True)
        status_box = st.info("🔄 Phase 1/3: Analyzing legal query & parsing intent...")

    time.sleep(0.4)
    with progress_placeholder.container():
        st.markdown("<div class='shimmer-progress'></div>", unsafe_allow_html=True)
        status_box = st.info("🔍 Phase 2/3: Reviewing legal concepts against statutory frameworks...")

    # Execute LLM query
    response_data, error_msg = query_legal_consultant(
        mode=mode,
        user_query=user_query,
        api_key=api_key,
        model_name=model_name
    )

    time.sleep(0.3)
    with progress_placeholder.container():
        st.markdown("<div class='shimmer-progress'></div>", unsafe_allow_html=True)
        status_box = st.info("✨ Phase 3/3: Preparing structured JSON response cards...")

    time.sleep(0.3)
    progress_placeholder.empty()

    if error_msg:
        render_alert_card(title="Engine Notice", message=error_msg, alert_type="error")
        return

    if response_data:
        # Cache response in session state according to current mode
        state_key = f"last_response_{mode}"
        st.session_state[state_key] = response_data
        st.rerun()


if __name__ == "__main__":
    main()
