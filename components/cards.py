"""Response cards rendering component for AI Legal Consultant.

Renders structured JSON outputs into glassmorphism cards with colored left borders,
action bars, copy buttons, and formatted alert components.
"""

import streamlit as st
from parser import LegalResponse
from utils import export_response_to_markdown, export_response_to_json_str


def render_response_cards(response: LegalResponse):
    """Renders all 6 structured response cards from a LegalResponse object.

    Cards:
    1. 📌 Legal Topic
    2. 📝 Summary
    3. ⚠ Important Points
    4. ⚖ Possible Considerations
    5. ➡ Suggested Next Steps
    6. 📢 Disclaimer
    """
    if not response:
        return

    # Card 1: Legal Topic
    st.markdown(
        f"""
        <div class="glass-card card-legal-topic">
            <div class="card-header">📌 Legal Topic</div>
            <div style="font-size: 1.15rem; font-weight: 700; color: #38BDF8;">
                {response.legal_topic}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Card 2: Executive Summary
    st.markdown(
        f"""
        <div class="glass-card card-summary">
            <div class="card-header">📝 Executive Summary</div>
            <div style="font-size: 1.02rem; line-height: 1.7; color: #E2E8F0;">
                {response.summary}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Card 3: Important Points & Clauses
    if response.important_points:
        points_html = "".join([f"<li>{pt}</li>" for pt in response.important_points])
        st.markdown(
            f"""
            <div class="glass-card card-important-points">
                <div class="card-header">⚠ Important Points & Parties</div>
                <ul class="card-list">
                    {points_html}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Card 3.1: Constitutional Articles
    if response.constitutional_articles:
        articles_html = "".join([f"<li>{pt}</li>" for pt in response.constitutional_articles])
        st.markdown(
            f"""
            <div class="glass-card card-articles">
                <div class="card-header">📖 Constitutional Articles</div>
                <ul class="card-list">
                    {articles_html}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Card 3.2: Related Acts
    if response.related_acts:
        acts_html = "".join([f"<li>{pt}</li>" for pt in response.related_acts])
        st.markdown(
            f"""
            <div class="glass-card card-acts">
                <div class="card-header">📚 Related Indian Acts</div>
                <ul class="card-list">
                    {acts_html}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Card 4: Legal Considerations & Risks
    if response.possible_considerations:
        cons_html = "".join([f"<li>{c}</li>" for c in response.possible_considerations])
        st.markdown(
            f"""
            <div class="glass-card card-considerations">
                <div class="card-header">⚖ Possible Considerations & Risks</div>
                <ul class="card-list">
                    {cons_html}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Card 5: Suggested Next Steps
    if response.suggested_next_steps:
        steps_html = "".join([f"<li>{s}</li>" for s in response.suggested_next_steps])
        st.markdown(
            f"""
            <div class="glass-card card-next-steps">
                <div class="card-header">➡ Suggested Next Steps</div>
                <ul class="card-list">
                    {steps_html}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Card 6: Mandatory Legal Disclaimer
    st.markdown(
        f"""
        <div class="glass-card card-disclaimer">
            <div class="card-header" style="color: #F87171;">📢 Legal Disclaimer</div>
            <div style="font-size: 0.92rem; color: #FCA5A5; line-height: 1.6;">
                {response.disclaimer}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Export Action Buttons Bar
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        md_text = export_response_to_markdown(response)
        st.download_button(
            label="📥 Download Markdown Report",
            data=md_text,
            file_name=f"{response.legal_topic.lower().replace(' ', '_')}_analysis.md",
            mime="text/markdown",
            use_container_width=True
        )

    with col2:
        json_text = export_response_to_json_str(response)
        st.download_button(
            label="📄 Export Raw JSON Schema",
            data=json_text,
            file_name=f"{response.legal_topic.lower().replace(' ', '_')}_schema.json",
            mime="application/json",
            use_container_width=True
        )


def render_alert_card(title: str, message: str, alert_type: str = "warning"):
    """Renders a styled error or warning alert card.

    Args:
        title: Alert headline.
        message: Detailed explanation.
        alert_type: 'error', 'warning', or 'info'.
    """
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
