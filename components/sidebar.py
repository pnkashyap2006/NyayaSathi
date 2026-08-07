"""Sidebar component for AI Legal Consultant.

Renders navigation links, model selection, status indicators, and session state controls.
Hides raw API keys securely from the application UI.
"""

import streamlit as st
from config import LOGO_PATH, GROQ_API_KEY, AVAILABLE_MODELS, DEFAULT_MODEL


def render_sidebar() -> dict:
    """Renders the collapsible sidebar navigation and engine status controls.

    Returns:
        dict: User selections including 'mode', 'api_key', and 'selected_model'.
    """
    with st.sidebar:
        # App Logo & Header
        if LOGO_PATH.exists():
            st.image(str(LOGO_PATH), use_container_width=True)
        else:
            st.markdown(
                """
                <div style="text-align: center; padding: 1rem 0; font-size: 2.2rem; font-family: 'Cinzel', serif;">
                    ⚖️ <b style="background: linear-gradient(135deg, #FF9933, #D4AF37, #138808); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">NyayaSathi</b>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<p style='text-align: center; color: #D4AF37; font-size: 0.85rem; margin-top: -0.5rem;'>Indian Legal AI Assistant</p>", unsafe_allow_html=True)
        st.divider()

        # Navigation Options
        st.markdown("<div style='font-size: 0.85rem; font-weight: 700; color: #E2E8F0; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;'>Navigation</div>", unsafe_allow_html=True)
        
        mode_options = {
            "home": "🏛️ Assistant Feed",
            "preamble": "📜 Preamble",
            "constitution": "📖 Constitution",
            "rights": "🛡️ Rights",
            "duties": "⚖️ Duties",
            "judiciary": "🏛️ Judiciary",
            "laws": "📚 Laws",
            "summarize_document": "📄 Summarize Document",
            "about": "ℹ️ About"
        }

        if "navigation_mode" not in st.session_state:
            st.session_state.navigation_mode = "home"

        current_mode = st.radio(
            label="Select Operational Mode",
            options=list(mode_options.keys()),
            format_func=lambda x: mode_options[x],
            index=list(mode_options.keys()).index(st.session_state.navigation_mode) if st.session_state.navigation_mode in mode_options else 0,
            label_visibility="collapsed"
        )
        st.session_state.navigation_mode = current_mode

        st.divider()

        # AI Engine Status (API Key Hidden from UI)
        st.markdown("<div style='font-size: 0.85rem; font-weight: 700; color: #94A3B8; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;'>AI Engine Status</div>", unsafe_allow_html=True)

        # Secure internal API Key check (not displayed in UI)
        effective_key = GROQ_API_KEY.strip()
        if effective_key and effective_key != "your_groq_api_key_here":
            st.markdown("<span style='color: #10B981; font-size: 0.85rem; font-weight: 600;'>🟢 Groq AI Engine Online</span>", unsafe_allow_html=True)
        else:
            st.markdown("<span style='color: #F59E0B; font-size: 0.85rem; font-weight: 600;'>🟡 Adaptive Local Engine Active</span>", unsafe_allow_html=True)

        # Model Selector
        selected_model = st.selectbox(
            label="Target Model",
            options=AVAILABLE_MODELS,
            index=0 if DEFAULT_MODEL not in AVAILABLE_MODELS else AVAILABLE_MODELS.index(DEFAULT_MODEL)
        )

        st.divider()

        # Session reset button
        if st.button("🔄 Reset Chat Session", use_container_width=True):
            st.session_state.chat_messages = []
            st.session_state.pending_user_input = None
            st.rerun()

        return {
            "mode": current_mode,
            "api_key": effective_key,
            "selected_model": selected_model
        }
