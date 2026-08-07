"""NyayaSathi - Indian Legal AI Assistant Main Entrypoint.

Provides a modern, fluid, ChatGPT / Claude style conversational interface for Indian legal research,
constitutional law exploration, contract review, and statutory guidance.
"""

import time
import streamlit as st

# Page Configuration MUST be the first Streamlit command
st.set_page_config(
    page_title="NyayaSathi - Indian Legal AI Assistant",
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
from components.rights import render_rights_page
from components.duties import render_duties_page
from components.judiciary import render_judiciary
from components.laws import render_laws
from llm import query_legal_consultant, query_legal_consultant_stream
from utils import load_sample_documents, extract_text_from_file


def main():
    # Inject CSS Design Tokens & Glassmorphism Styles
    inject_custom_css()

    # Initialize Session State
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []
    if "pending_user_input" not in st.session_state:
        st.session_state.pending_user_input = None

    # Render Sidebar Navigation
    sidebar_config = render_sidebar()
    current_mode = sidebar_config["mode"]
    api_key = sidebar_config["api_key"]
    selected_model = sidebar_config["selected_model"]

    # Main Page Routing
    if current_mode == "home" or current_mode == "ai_assistant":
        render_chat_assistant_page(api_key, selected_model)
    elif current_mode == "preamble":
        render_preamble()
    elif current_mode == "constitution":
        render_constitution()
    elif current_mode == "rights":
        render_rights_page()
    elif current_mode == "duties":
        render_duties_page()
    elif current_mode == "judiciary":
        render_judiciary()
    elif current_mode == "laws":
        render_laws()
    elif current_mode == "summarize_document":
        render_summarize_document_page(api_key, selected_model)
    elif current_mode == "about":
        render_about_page()

    # Render Sticky Footer
    render_footer()


def render_chat_assistant_page(api_key: str, model_name: str):
    """Renders the primary ChatGPT-style Legal AI Assistant interface with fluid Markdown streaming & memory."""
    render_hero_banner()

    # Starter Preset Examples Banner
    st.markdown(
        """
        <div class="glass-card" style="border-left: 5px solid #FF9933; margin-bottom: 1.5rem;">
            <div class="card-header" style="margin-bottom: 0.4rem;">⚡ Quick Research Starters</div>
            <p style="color: #CBD5E1; margin-bottom: 0.8rem; font-size: 0.92rem;">
                Click any prompt below to experience dynamic, intent-adaptive legal reasoning:
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    qcol1, qcol2, qcol3, qcol4 = st.columns(4)

    preset_clicked = None
    with qcol1:
        if st.button("📜 Explain Article 21", use_container_width=True, key="p1_chat"):
            preset_clicked = "Explain Article 21 of the Indian Constitution."
    with qcol2:
        if st.button("⚖️ Difference: BNS vs IPC", use_container_width=True, key="p2_chat"):
            preset_clicked = "What is the difference between Bharatiya Nyaya Sanhita (BNS) and IPC?"
    with qcol3:
        if st.button("🏠 Landlord Deposit Dispute", use_container_width=True, key="p3_chat"):
            preset_clicked = "My landlord refuses to refund my security deposit after lease ended. What are my legal remedies?"
    with qcol4:
        if st.button("👮 Arrest Without Warrant", use_container_width=True, key="p4_chat"):
            preset_clicked = "Can police arrest me without a warrant under BNSS?"

    # Check pending follow-up chip clicks or preset clicks
    active_prompt = preset_clicked or st.session_state.pop("pending_user_input", None)

    # Render Chat History Thread
    st.markdown("<br>", unsafe_allow_html=True)
    if st.session_state.chat_messages:
        st.markdown("<h3 style='color: #38BDF8; font-family: Cinzel, serif;'>💬 Research Thread & Reasoning History</h3>", unsafe_allow_html=True)

        for idx, msg in enumerate(st.session_state.chat_messages):
            if msg["role"] == "user":
                st.markdown(
                    f"""
                    <div class="user-chat-bubble">
                        <strong style="color: #93C5FD;">👤 You:</strong><br>{msg["content"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif msg["role"] == "assistant":
                st.markdown("<div class='ai-chat-bubble'>", unsafe_allow_html=True)
                st.markdown("<strong style='color: #D4AF37;'>⚖️ NyayaSathi Assistant:</strong><br><br>", unsafe_allow_html=True)
                if isinstance(msg["content"], str):
                    st.markdown(msg["content"])
                else:
                    render_response_cards(msg["content"], metadata=msg.get("metadata"), key_prefix=f"msg_{idx}")
                st.markdown("</div>", unsafe_allow_html=True)

        if st.button("🗑️ Clear Conversation History", key="btn_clear_history"):
            st.session_state.chat_messages = []
            st.rerun()

    # Sticky Bottom Chat Input Box
    user_input = st.chat_input("Ask a legal question, describe a situation, or paste a document clause...") or active_prompt

    if user_input:
        user_text = user_input.strip()

        # Append User Message to Thread
        st.session_state.chat_messages.append({"role": "user", "content": user_text})

        # Process Query with Loading Indicator
        with st.spinner("⚖️ NyayaSathi is identifying legal issues & rendering adaptive analysis..."):
            history = [
                {"role": m["role"], "content": m["content"] if isinstance(m["content"], str) else m["content"].markdown_content}
                for m in st.session_state.chat_messages[:-1]
            ]

            response_data, error_msg, metadata = query_legal_consultant(
                user_query=user_text,
                api_key=api_key,
                model_name=model_name,
                history=history
            )

        if error_msg:
            st.session_state.chat_messages.append({"role": "assistant", "content": f"⚠️ {error_msg}", "metadata": metadata})
        elif response_data:
            st.session_state.chat_messages.append({"role": "assistant", "content": response_data, "metadata": metadata})

        st.rerun()


def render_summarize_document_page(api_key: str, model_name: str):
    """Renders Premium Contract Analysis & Legal Interpretation Interface (Harvey AI / Lexis+ style)."""
    # 1. Clean Hero Section
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, rgba(11, 19, 43, 0.95), rgba(20, 35, 65, 0.9)); border: 1px solid rgba(6, 182, 212, 0.35); border-radius: 12px; padding: 1.8rem; margin-bottom: 1.5rem; text-align: center;">
            <h1 style="color: #06B6D4; font-family: 'Cinzel', serif; font-size: 2.1rem; margin-bottom: 0.4rem;">
                📄 Contract Analysis & Legal Interpretation
            </h1>
            <p style="color: #CBD5E1; font-size: 1rem; max-width: 820px; margin: 0 auto; line-height: 1.5;">
                Understand contracts, identify legal risks, explain complex clauses, and receive practical legal insights in simple language.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 2. Input Options Layout (Option 1: Paste Text, Option 2: Upload File)
    tab_paste, tab_upload = st.tabs([
        "✍️ Option 1: Paste Contract Text",
        "📁 Option 2: Upload Document (PDF, DOCX, TXT)"
    ])

    user_doc = ""

    with tab_paste:
        placeholder_text = (
            "Paste your legal document here...\n\n"
            "Supported:\n"
            "• Employment Contracts\n"
            "• Rental Agreements\n"
            "• NDAs\n"
            "• Partnership Agreements\n"
            "• Service Agreements\n"
            "• Legal Notices\n"
            "• Privacy Policies"
        )
        pasted_text = st.text_area(
            label="Contract Editor",
            height=260,
            placeholder=placeholder_text,
            key="d_input_editor",
            label_visibility="collapsed"
        )
        if pasted_text:
            user_doc = pasted_text

    with tab_upload:
        st.markdown(
            """
            <div style="margin-bottom: 0.5rem; font-size: 0.95rem; color: #94A3B8;">
                Upload your agreement for instant legal risk analysis and clause breakdown:
            </div>
            """,
            unsafe_allow_html=True
        )
        uploaded_file = st.file_uploader(
            label="📁 Drag & Drop Contract Here or Click to Upload",
            type=["pdf", "docx", "txt"],
            key="contract_file_uploader"
        )
        if uploaded_file is not None:
            extracted = extract_text_from_file(uploaded_file)
            if extracted and not extracted.startswith("[Error"):
                user_doc = extracted
                st.success(f"✓ Loaded '{uploaded_file.name}' ({len(extracted)} characters extracted)")
                with st.expander("👁️ View Extracted Text Preview", expanded=False):
                    st.text(extracted[:1000] + ("..." if len(extracted) > 1000 else ""))
            elif extracted.startswith("[Error"):
                st.error(extracted)

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. CTA Button & Subtitle
    col_btn, _ = st.columns([1, 1])
    with col_btn:
        analyze_clicked = st.button("🔍 Analyze Contract", use_container_width=True, key="btn_submit_d")

    st.markdown(
        """
        <p style="color: #64748B; font-size: 0.85rem; margin-top: -0.4rem; margin-bottom: 1.5rem;">
            <i>AI-powered clause interpretation, legal risk analysis, and practical recommendations.</i>
        </p>
        """,
        unsafe_allow_html=True
    )

    if analyze_clicked:
        if not user_doc.strip():
            st.markdown(
                """
                <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); padding: 1rem; border-radius: 8px; color: #FCA5A5; margin-bottom: 1rem;">
                    <b>Document Required:</b> Please paste text or upload a PDF/DOCX/TXT contract file to analyze.
                </div>
                """,
                unsafe_allow_html=True
            )
            return

        run_legal_analysis(mode="Legal Document Summarization", user_query=user_doc, api_key=api_key, model_name=model_name)

    # 4. Results or Professional Friendly Empty State
    if "last_response_summarize_document" in st.session_state:
        st.markdown("<br><h3 style='color: #06B6D4;'>📜 Contract Analysis & Risk Interpretation</h3>", unsafe_allow_html=True)
        render_response_cards(st.session_state.last_response_summarize_document, key_prefix="doc_summary")
    else:
        st.markdown(
            """
            <div style="background: rgba(30, 41, 59, 0.5); border: 1px dashed rgba(6, 182, 212, 0.4); border-radius: 12px; padding: 2.5rem; text-align: center; margin-top: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 0.6rem;">📁</div>
                <h3 style="color: #06B6D4; margin-bottom: 0.4rem; font-family: 'Cinzel', serif;">
                    Upload or paste a legal document to begin analysis
                </h3>
                <p style="color: #94A3B8; font-size: 0.95rem; max-width: 650px; margin: 0 auto;">
                    NyayaSathi will identify important clauses, explain their meaning in simple language, highlight legal risks, and provide practical legal insights.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


def render_about_page():
    """Renders the About section with architecture info and technology stack."""
    st.markdown("<h2 style='color: #F8FAFC;'>ℹ️ About NyayaSathi</h2>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="glass-card" style="border-left: 5px solid #38BDF8;">
            <div class="card-header">🎯 Project Mission</div>
            <p style="color: #CBD5E1; line-height: 1.7;">
                <strong>NyayaSathi</strong> is a professional Indian Legal AI Assistant designed to empower citizens, students, and legal researchers with dynamic, conversational legal guidance.
                Modeled after ChatGPT, Claude, and Perplexity, it analyzes user intent to dynamically format responses with markdown tables, step-by-step numbers, blockquotes, and natural citations without rigid form-filling.
            </p>
        </div>

        <div class="glass-card" style="border-left: 5px solid #8B5CF6;">
            <div class="card-header">🛠️ Technology Stack & Adaptive Architecture</div>
            <ul class="card-list">
                <li><strong>Python 3.11+</strong>: Core application logic and async handlers</li>
                <li><strong>Groq API</strong>: Ultra-fast LLM inference engine (Llama-3.3-70b-versatile)</li>
                <li><strong>Adaptive Markdown Engine</strong>: Dynamic GFM Markdown generation tailored to query intent</li>
                <li><strong>Modular Knowledge Layer</strong>: RAG-ready retrievers supporting FAISS, ChromaDB, Pinecone, & Govt legal datasets</li>
                <li><strong>Streamlit</strong>: Modern web client with custom dark glassmorphic design</li>
            </ul>
        </div>

        <div class="glass-card" style="border-left: 5px solid #EF4444; background: rgba(239, 68, 68, 0.05);">
            <div class="card-header" style="color: #F87171;">⚠️ Legal Disclaimer & Compliance</div>
            <p style="color: #FCA5A5; line-height: 1.6;">
                NyayaSathi provides general legal information for educational and research purposes only.
                It does not constitute professional legal advice or an attorney-client relationship.
                Always consult a licensed advocate in your local jurisdiction prior to taking legal action or executing binding agreements.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def run_legal_analysis(mode: str, user_query: str, api_key: str, model_name: str):
    """Executes legal query for standalone document summarization mode."""
    progress_placeholder = st.empty()

    with progress_placeholder.container():
        st.markdown("<div class='shimmer-progress'></div>", unsafe_allow_html=True)
        status_box = st.info("🔄 Phase 1/3: Analyzing document text & identifying clauses...")

    time.sleep(0.3)
    with progress_placeholder.container():
        st.markdown("<div class='shimmer-progress'></div>", unsafe_allow_html=True)
        status_box = st.info("🔍 Phase 2/3: Evaluating statutory obligations & risk factors...")

    response_data, error_msg, metadata = query_legal_consultant(
        user_query=user_query,
        api_key=api_key,
        model_name=model_name,
        mode=mode
    )

    time.sleep(0.3)
    progress_placeholder.empty()

    if error_msg:
        render_alert_card(title="Engine Notice", message=error_msg, alert_type="error")
        return

    if response_data:
        st.session_state["last_response_summarize_document"] = response_data
        st.rerun()


if __name__ == "__main__":
    main()
