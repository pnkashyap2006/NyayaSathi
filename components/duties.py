"""Fundamental Duties Learning Module Component (Part IVA).

Independent page dedicated strictly to Fundamental Duties (Article 51A),
featuring historical background, rationale, civic actions, enforcement statutes,
and misconceptions debunked.
"""

import streamlit as st
from data.constitution import EXPANDED_FUNDAMENTAL_DUTIES


def render_duties_page():
    """Renders the independent Fundamental Duties (Part IVA) Learning Module."""
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, rgba(11, 19, 43, 0.95), rgba(20, 35, 65, 0.9)); border: 1px solid rgba(255, 153, 51, 0.35); border-radius: 12px; padding: 1.8rem; margin-bottom: 1.5rem; text-align: center;">
            <h1 style="color: #FF9933; font-family: 'Cinzel', serif; font-size: 2.1rem; margin-bottom: 0.4rem;">
                ⚖️ Fundamental Duties (Part IVA)
            </h1>
            <p style="color: #CBD5E1; font-size: 1rem; max-width: 820px; margin: 0 auto; line-height: 1.5;">
                Understand the moral and civic responsibilities expected of every citizen, why they were introduced, and how they contribute to nation-building.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background: rgba(59, 130, 246, 0.1); border-left: 4px solid #3B82F6; padding: 1rem; border-radius: 6px; margin-bottom: 1.2rem;">
            <h4 style="color: #60A5FA; margin: 0 0 0.3rem 0;">Part IVA — Moral Obligations of Every Citizen</h4>
            <p style="color: #E2E8F0; margin: 0; font-size: 0.92rem;">
                Added by the <b>42nd Amendment Act (1976)</b> on the recommendation of the <b>Swaran Singh Committee</b> (and expanded by the 86th Amendment in 2002).
                While Fundamental Duties are non-justiciable (cannot be enforced directly by court writs), courts use them to interpret statutes and enforce environmental, civic, and penal legislation.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    duties_search = st.text_input(
        "🔍 Search Fundamental Duties",
        placeholder="e.g. Environment, National Flag, Scientific Temper, Heritage, Education...",
        key="duties_page_search"
    ).strip().lower()

    for duty in EXPANDED_FUNDAMENTAL_DUTIES:
        if duties_search:
            combined_d_text = (duty["title"] + " " + duty["duty"] + " " + duty["why_it_exists"] + " " + duty["enforcement_laws"]).lower()
            if duties_search not in combined_d_text:
                continue

        with st.expander(f"🛡️ Article 51A{duty['code']} — {duty['title']}"):
            st.markdown(
                f"""
                <div style="background: rgba(30, 41, 59, 0.7); border-left: 4px solid #FF9933; padding: 1rem; border-radius: 6px; margin-bottom: 1rem;">
                    <b style="color: #FF9933; font-size: 1.05rem;">Constitutional Duty:</b>
                    <p style="color: #F8FAFC; font-size: 1rem; margin: 0.3rem 0 0 0;"><i>"{duty['duty']}"</i></p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("#### 📌 Why This Duty Exists")
            st.write(duty["why_it_exists"])

            st.markdown("#### 📜 Historical Background")
            st.write(duty["historical_background"])

            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(
                    f"""
                    <div style="background: rgba(16, 185, 129, 0.08); border-left: 3px solid #10B981; padding: 0.8rem; border-radius: 6px; height: 100%;">
                        <h5 style="color: #34D399; margin: 0 0 0.3rem 0;">🌱 How Citizens Can Fulfill It</h5>
                        <p style="color: #F8FAFC; margin: 0; font-size: 0.9rem;">{duty['how_to_fulfill']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col_b:
                st.markdown(
                    f"""
                    <div style="background: rgba(139, 92, 246, 0.08); border-left: 3px solid #8B5CF6; padding: 0.8rem; border-radius: 6px; height: 100%;">
                        <h5 style="color: #C4B5FD; margin: 0 0 0.3rem 0;">⚖️ Enforcement Laws</h5>
                        <p style="color: #F8FAFC; margin: 0; font-size: 0.9rem;">{duty['enforcement_laws']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"**❌ Common Misconception:** {duty['misconception']}")
