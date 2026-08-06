"""Sidebar component for AI Legal Consultant.

Renders navigation links, API configuration controls, model selectors, and sample document triggers.
"""

import streamlit as st
from config import LOGO_PATH, GROQ_API_KEY, AVAILABLE_MODELS, DEFAULT_MODEL


def render_sidebar() -> dict:
    """Renders the collapsible sidebar navigation and settings controls.

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
                    ⚖️ <b style="background: linear-gradient(135deg, #FF9933, #D4AF37, #138808); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Indian Legal AI</b>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<p style='text-align: center; color: #D4AF37; font-size: 0.85rem; margin-top: -0.5rem;'>Constitution & Law Explorer</p>", unsafe_allow_html=True)
        st.divider()

        # Navigation Options
        st.markdown("<div style='font-size: 0.85rem; font-weight: 700; color: #E2E8F0; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;'>Navigation</div>", unsafe_allow_html=True)
        
        mode_options = {
            "home": "🏛️ Home",
            "preamble": "📜 Preamble",
            "constitution": "📖 Constitution",
            "rights": "⚖️ Rights",
            "duties": "🛡️ Duties",
            "judiciary": "🏛️ Judiciary",
            "laws": "📚 Laws",
            "ai_assistant": "🤖 AI Assistant",
            "summarize_document": "📄 Summarize Document",
            "about": "ℹ️ About"
        }

        # Session state for current mode
        if "navigation_mode" not in st.session_state:
            st.session_state.navigation_mode = "home"

        current_mode = st.radio(
            label="Select Operational Mode",
            options=list(mode_options.keys()),
            format_func=lambda x: mode_options[x],
            index=list(mode_options.keys()).index(st.session_state.navigation_mode),
            label_visibility="collapsed"
        )
        st.session_state.navigation_mode = current_mode

        st.divider()

        # Groq API Configuration Section
        st.markdown("<div style='font-size: 0.85rem; font-weight: 700; color: #94A3B8; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;'>Groq Engine Config</div>", unsafe_allow_html=True)

        user_api_key = st.text_input(
            label="Groq API Key",
            value=st.session_state.get("user_api_key", GROQ_API_KEY),
            type="password",
            placeholder="gsk_...",
            help="Enter your Groq API key. If left blank, mock legal engine will run."
        )
        st.session_state.user_api_key = user_api_key

        # API Key Status Badge
        if user_api_key and user_api_key != "your_groq_api_key_here":
            st.markdown("<span style='color: #10B981; font-size: 0.85rem; font-weight: 600;'>🟢 Groq API Connected</span>", unsafe_allow_html=True)
        else:
            st.markdown("<span style='color: #F59E0B; font-size: 0.85rem; font-weight: 600;'>🟡 Built-in Mock Engine Active</span>", unsafe_allow_html=True)

        # Model Selector
        selected_model = st.selectbox(
            label="Target Model",
            options=AVAILABLE_MODELS,
            index=0 if DEFAULT_MODEL not in AVAILABLE_MODELS else AVAILABLE_MODELS.index(DEFAULT_MODEL)
        )

        st.divider()

        # Session reset button
        if st.button("🔄 Reset App State", use_container_width=True):
            st.session_state.clear()
            st.rerun()

        return {
            "mode": current_mode,
            "api_key": user_api_key,
            "selected_model": selected_model
        }
