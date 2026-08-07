"""Top Navigation Bar Component for NyayaSathi AI Legal Consultant."""
# pyrefly: ignore [missing-import]
import streamlit as st
from config import AVAILABLE_MODELS, DEFAULT_MODEL, GROQ_API_KEY


def render_sidebar() -> dict:
    """Renders a pixel-perfect, fixed top navigation header across the viewport.

    Returns:
        dict: User selections including 'mode', 'api_key', and 'selected_model'.
    """

    # ── Inject Fixed Header CSS & Global Resets ──────────────────────────────
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap');

        /* ── Full Page Background: Tri-Color Purple, Dark Blue & Black Gradient ── */
        .stApp, [data-testid="stAppViewContainer"], .main, .block-container {
            background-color: #000000 !important;
            background-image: 
                radial-gradient(at 10% 20%, rgba(138, 43, 226, 0.35) 0px, transparent 50%),
                radial-gradient(at 90% 80%, rgba(10, 25, 70, 0.6) 0px, transparent 50%),
                linear-gradient(135deg, #020008 0%, #08031A 40%, #0A0F2B 75%, #000000 100%) !important;
            background-attachment: fixed !important;
        }

        /* ── Hide Streamlit Default Sidebar & Top Header Chrome ── */
        [data-testid="stSidebar"], 
        [data-testid="collapsedControl"], 
        header[data-testid="stHeader"] {
            display: none !important;
        }

        /* ── Push main content down so it does not hide behind fixed topbar ── */
        .block-container {
            padding-top: 5.5rem !important;
            padding-bottom: 2rem !important;
            max-width: 1650px !important;
        }

        /* ── Target Outermost Fixed Header Container ── */
        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            width: 100vw !important;
            height: 64px !important;
            z-index: 999999 !important;
            
            /* High-Contrast Purple, Dark Blue & Pure Black Background */
            background: linear-gradient(135deg, rgba(8, 2, 20, 0.96) 0%, rgba(15, 10, 45, 0.95) 45%, rgba(10, 22, 60, 0.95) 75%, rgba(2, 2, 8, 0.98) 100%) !important;
            background-image: 
                radial-gradient(at 10% 50%, rgba(138, 43, 226, 0.3) 0px, transparent 40%),
                radial-gradient(at 90% 50%, rgba(0, 243, 255, 0.25) 0px, transparent 40%),
                linear-gradient(90deg, #03000A 0%, #120831 40%, #0A1B42 80%, #010105 100%) !important;
            border-bottom: 1px solid rgba(192, 132, 252, 0.4) !important;
            backdrop-filter: blur(25px) !important;
            -webkit-backdrop-filter: blur(25px) !important;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.95), 0 0 25px rgba(138, 43, 226, 0.25) !important;
            
            display: flex !important;
            align-items: center !important;
            padding: 0 1rem !important;
            box-sizing: border-box !important;
            margin: 0 !important;
        }

        .nyaya-navbar-anchor {
            display: none !important;
        }

        /* ── Force Strict Flex Row Across All Columns ── */
        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) [data-testid="stHorizontalBlock"] {
            display: flex !important;
            flex-direction: row !important;
            align-items: center !important;
            justify-content: space-between !important;
            width: 100% !important;
            height: 64px !important;
            gap: 4px !important;
            margin: 0 !important;
        }

        /* Strip out Streamlit's default inner vertical padding on columns */
        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) [data-testid="stColumn"] {
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            padding: 0 !important;
            height: 64px !important;
            min-width: 0 !important;
            z-index: 1000000 !important;
        }

        /* Reset inner markdown containers in columns to prevent top offset */
        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) [data-testid="stColumn"] div[data-testid="stMarkdownContainer"],
        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) [data-testid="stColumn"] div.stElementContainer {
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            height: 100% !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        /* ── Logo Alignment ── */
        .nyaya-brand {
            display: flex !important;
            align-items: center !important;
            justify-content: flex-start !important;
            gap: 8px !important;
            white-space: nowrap !important;
            z-index: 1000001 !important;
            height: 100% !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        .nyaya-brand-icon {
            font-size: 2rem !important; 
            line-height: 1 !important;
            filter: drop-shadow(0 0 12px rgba(192, 132, 252, 0.9));
            display: flex !important;
            align-items: center !important;
        }

        .nyaya-brand-title {
            font-family: 'Cinzel', serif !important;
            font-size: 1.55rem !important; 
            font-weight: 800 !important;
            color: #FFFFFF !important;
            background: linear-gradient(120deg, #FFFFFF 0%, #C084FC 50%, #00F3FF 100%);
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            letter-spacing: 0.03em !important;
            margin: 0 !important;
            line-height: 1 !important;
            display: flex !important;
            align-items: center !important;
        }

        /* ── Nav Buttons ── */
        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) div.stButton {
            width: 100% !important;
            margin: 0 !important;
            display: flex !important;
            align-items: center !important;
            height: 100% !important;
        }

        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) div.stButton > button {
            height: 38px !important;
            min-height: 38px !important;
            max-height: 38px !important;
            background: rgba(12, 6, 32, 0.85) !important;
            border: 1px solid rgba(192, 132, 252, 0.3) !important;
            border-radius: 8px !important;
            padding: 0 4px !important;
            transition: all 0.2s ease !important;
            white-space: nowrap !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            margin: 0 !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.7) !important;
            z-index: 1000001 !important;
        }

        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) div.stButton > button p {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 0.76rem !important;
            font-weight: 600 !important;
            color: #E2E8F0 !important;
            margin: 0 !important;
            padding: 0 !important;
            line-height: 1 !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }

        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) div.stButton > button:hover {
            background: rgba(138, 43, 226, 0.3) !important;
            border-color: #C084FC !important;
            box-shadow: 0 0 14px rgba(192, 132, 252, 0.6) !important;
        }

        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) div.stButton > button:hover p {
            color: #FFFFFF !important;
        }

        .active-nav-btn div.stButton > button {
            background: linear-gradient(135deg, rgba(138, 43, 226, 0.45) 0%, rgba(10, 30, 90, 0.65) 100%) !important;
            border: 1px solid #C084FC !important;
            box-shadow: 0 0 16px rgba(192, 132, 252, 0.7) !important;
        }

        .active-nav-btn div.stButton > button p {
            color: #00F3FF !important;
            font-weight: 700 !important;
        }

        /* ── Config Popover Position & Vertical Alignment Fix ── */
        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) [data-testid="stColumn"]:has(div[data-testid="stPopover"]) {
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            height: 64px !important;
        }

        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) [data-testid="stColumn"] div.stElementContainer:has(div[data-testid="stPopover"]) {
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            height: 100% !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) div[data-testid="stPopover"] {
            width: 100% !important;
            height: 100% !important;
            display: flex !important;
            align-items: center !important;
            justify-content: flex-end !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) div[data-testid="stPopover"] > button {
            height: 38px !important;
            min-height: 38px !important;
            max-height: 38px !important;
            background: rgba(138, 43, 226, 0.35) !important;
            border: 1px solid rgba(192, 132, 252, 0.6) !important;
            border-radius: 8px !important;
            padding: 0 8px !important;
            margin: 0 !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            z-index: 1000001 !important;
            transform: none !important;
        }

        div[data-testid="stVerticalBlock"] > div:has(div.nyaya-navbar-anchor) div[data-testid="stPopover"] > button p {
            color: #00F3FF !important;
            font-weight: 700 !important;
            font-size: 0.8rem !important;
            margin: 0 !important;
            line-height: 1 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Navigation Session State
    if "navigation_mode" not in st.session_state:
        st.session_state.navigation_mode = "home"

    # Compact labels
    mode_options = {
        "home": "🏛️ Home",
        "preamble": "📜 Preamble",
        "constitution": "📖 Constitution",
        "rights": "⚖️ Rights",
        "duties": "🛡️ Duties",
        "judiciary": "🏛️ Judiciary",
        "laws": "📚 Laws",
        "ai_assistant": "🤖 AI",
        "summarize_document": "📄 Summarizer",
    }

    # ── Single Horizontal Row Layout Container ──────────────────────────────
    with st.container():
        st.markdown('<div class="nyaya-navbar-anchor"></div>', unsafe_allow_html=True)

        header_cols = st.columns([2.0, 0.8, 0.9, 1.0, 0.8, 0.8, 0.85, 0.8, 0.75, 0.85, 0.7], gap="small")

        # 1. Brand Logo
        with header_cols[0]:
            st.markdown(
                """
                <div class="nyaya-brand">
                    <span class="nyaya-brand-icon">⚖️</span>
                    <span class="nyaya-brand-title">NYAYASATHI</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # 2. Navigation Buttons
        mode_keys = list(mode_options.keys())
        for idx, mode_key in enumerate(mode_keys):
            mode_label = mode_options[mode_key]
            with header_cols[idx + 1]:
                is_active = st.session_state.navigation_mode == mode_key
                wrapper_class = "active-nav-btn" if is_active else ""

                st.markdown(f'<div class="{wrapper_class}">', unsafe_allow_html=True)
                if st.button(mode_label, key=f"nav_fixed_{mode_key}", use_container_width=True):
                    st.session_state.navigation_mode = mode_key
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

        # 3. Config Popover
        with header_cols[-1]:
            with st.popover("⚙️"):
                st.markdown("#### ⚙️ Groq Engine Config")
                user_api_key = st.text_input(
                    label="Groq API Key",
                    value=st.session_state.get("user_api_key", GROQ_API_KEY),
                    type="password",
                    placeholder="gsk_...",
                )
                st.session_state.user_api_key = user_api_key

                selected_model = st.selectbox(
                    label="Target Model",
                    options=AVAILABLE_MODELS,
                    index=0 if DEFAULT_MODEL not in AVAILABLE_MODELS else AVAILABLE_MODELS.index(DEFAULT_MODEL),
                )

                if st.button("🔄 Reset App", key="btn_reset_header_fixed", use_container_width=True):
                    st.session_state.clear()
                    st.rerun()

    return {
        "mode": st.session_state.navigation_mode,
        "api_key": st.session_state.get("user_api_key", GROQ_API_KEY),
        "selected_model": selected_model if "selected_model" in locals() else DEFAULT_MODEL,
    }