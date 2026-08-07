"""Fluid ChatGPT-Style Response Renderer for NyayaSathi Indian Legal AI Assistant.

Completely replaces fixed report cards and JSON viewer UI with an elegant, dynamic,
conversational response interface supporting rich GFM Markdown, tables, lists, codeblocks,
expandable references, and interactive follow-up question chips.
"""

import streamlit as st
from typing import Optional, Dict, Any
from parser import ConversationalResponse
from utils import export_response_to_markdown, export_response_to_json_str


def render_response_cards(response: ConversationalResponse, metadata: Optional[Dict[str, Any]] = None, key_prefix: str = ""):
    """Renders a single fluid, dynamic ChatGPT-style assistant response.

    Args:
        response: ConversationalResponse Pydantic object.
        metadata: Optional metadata dictionary containing emergency info, intent, sources.
        key_prefix: Unique key prefix for Streamlit widgets.
    """
    if not response:
        return

    prefix = f"{key_prefix}_" if key_prefix else ""

    # 1. Emergency Helpline Alert Banner (if high-risk emergency situation detected)
    if metadata and metadata.get("emergency"):
        em = metadata["emergency"]
        st.markdown(
            f"""
            <div class="emergency-banner">
                <div class="emergency-title">{em['title']}</div>
                <div style="color: #FEE2E2; font-size: 0.95rem; line-height: 1.6;">
                    {em['message']}
                </div>
                <div style="margin-top: 0.8rem;">
                    <span style="color: #F87171; font-weight: 600;">Official Helpline: </span>
                    <span class="emergency-helpline">📞 {em['helpline']}</span>
                    <span style="margin-left: 1rem; color: #CBD5E1; font-size: 0.85rem;">
                        Portal: <a href="{em['website']}" target="_blank" style="color: #38BDF8; text-decoration: underline;">{em['website']}</a>
                    </span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 2. Main Fluid Response Container (Rich Markdown Output)
    markdown_text = response.markdown_content
    st.markdown(markdown_text)

    # 3. Expandable Authoritative References (if relevant references exist)
    refs = response.references or (metadata.get("sources") if metadata else [])
    if refs:
        refs_html = "".join([f'<span class="badge-ref-law">✓ {r}</span>' for r in refs])
        st.markdown(
            f"""
            <div class="reasoning-card" style="margin-top: 1rem; padding: 0.8rem 1.2rem;">
                <details>
                    <summary style="font-size: 0.9rem; color: #94A3B8;">📚 View Authoritative Legal References ({len(refs)})</summary>
                    <div style="margin-top: 0.6rem;">
                        {refs_html}
                    </div>
                </details>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 4. Interactive Suggested Follow-Up Question Chips
    if response.follow_up_questions:
        st.markdown(
            """
            <div style="margin-top: 1.2rem; margin-bottom: 0.5rem; font-weight: 600; color: #D4AF37; font-size: 0.9rem;">
                💡 Suggested Follow-Up Questions:
            </div>
            """,
            unsafe_allow_html=True
        )
        cols = st.columns(min(len(response.follow_up_questions), 3))
        for idx, q_text in enumerate(response.follow_up_questions):
            col_idx = idx % len(cols)
            with cols[col_idx]:
                if st.button(f"🔍 {q_text}", key=f"{prefix}btn_followup_{idx}_{abs(hash(q_text))}", use_container_width=True):
                    st.session_state.pending_user_input = q_text
                    st.rerun()

    # 5. Mandatory Legal Safety Disclaimer
    st.markdown(
        f"""
        <div style="margin-top: 1rem; padding: 0.6rem 1rem; border-left: 3px solid #EF4444; background: rgba(239, 68, 68, 0.05); border-radius: 6px; font-size: 0.8rem; color: #FCA5A5;">
            ⚠️ <strong>Legal Notice:</strong> {response.disclaimer}
        </div>
        """,
        unsafe_allow_html=True
    )

    # 6. Action & Export Toolbar
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        md_text = export_response_to_markdown(response)
        st.download_button(
            label="📥 Export Markdown",
            data=md_text,
            file_name=f"{response.legal_topic.lower().replace(' ', '_')}_analysis.md",
            mime="text/markdown",
            use_container_width=True,
            key=f"{prefix}dl_md_{abs(hash(response.legal_topic))}"
        )

    with col2:
        json_text = export_response_to_json_str(response)
        st.download_button(
            label="📄 Export Raw JSON",
            data=json_text,
            file_name=f"{response.legal_topic.lower().replace(' ', '_')}_schema.json",
            mime="application/json",
            use_container_width=True,
            key=f"{prefix}dl_json_{abs(hash(response.legal_topic))}"
        )


def render_alert_card(title: str, message: str, alert_type: str = "warning"):
    """Renders a styled error or warning alert card."""
    color_map = {
        "error": {"border": "#EF4444", "bg": "rgba(239, 68, 68, 0.1)", "icon": "❌"},
        "warning": {"border": "#F59E0B", "bg": "rgba(245, 158, 11, 0.1)", "icon": "⚠️"},
        "info": {"border": "#3B82F6", "bg": "rgba(59, 130, 246, 0.1)", "icon": "ℹ️"},
    }
    cfg = color_map.get(alert_type, color_map["warning"])

    st.markdown(
        f"""
        <div class="glass-card" style="border-left: 5px solid {cfg['border']}; background: {cfg['bg']};">
            <div class="card-header" style="margin-bottom: 0.4rem;">
                <span>{cfg['icon']}</span> {title}
            </div>
            <div style="color: #CBD5E1; font-size: 0.95rem; line-height: 1.5;">
                {message}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
