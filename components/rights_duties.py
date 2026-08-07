"""Interactive Constitutional Learning Module for Fundamental Rights & Duties.

Presents Part III (Fundamental Rights) and Part IVA (Fundamental Duties) as rich,
engaging learning modules with article-by-article breakdowns, Constituent Assembly rationale,
real-life scenarios, reasonable restrictions, common misconceptions debunked, landmark Supreme Court
judgments, quick facts, and interactive FAQs.
"""

import streamlit as st
from data.constitution import EXPANDED_FUNDAMENTAL_RIGHTS, EXPANDED_FUNDAMENTAL_DUTIES, PREAMBLE_TEXT


def render_rights_duties():
    """Renders the comprehensive interactive constitutional learning hub."""
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, rgba(11, 19, 43, 0.95), rgba(20, 30, 60, 0.9)); border: 1px solid rgba(212, 175, 55, 0.3); border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; text-align: center;">
            <h1 style="color: #D4AF37; font-family: 'Cinzel', serif; font-size: 2.2rem; margin-bottom: 0.3rem;">
                ⚖️ Interactive Constitutional Learning Module
            </h1>
            <p style="color: #CBD5E1; font-size: 1rem; max-width: 800px; margin: 0 auto;">
                Explore <b>Part III (Fundamental Rights)</b> and <b>Part IVA (Fundamental Duties)</b> of the Indian Constitution.
                Understand why these rights exist, how they protect your daily life, when they can be legally restricted, and how landmark Supreme Court rulings shaped democracy.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs([
        "📜 Fundamental Rights (Part III — Articles 12 to 35)",
        "🛡️ Fundamental Duties (Part IVA — Article 51A)"
    ])

    # ==================== TAB 1: FUNDAMENTAL RIGHTS ====================
    with tab1:
        st.markdown(
            """
            <div style="background: rgba(16, 185, 129, 0.1); border-left: 4px solid #10B981; padding: 1rem; border-radius: 6px; margin-bottom: 1rem;">
                <h4 style="color: #10B981; margin: 0 0 0.3rem 0;">Justiciable Protections Against State Overreach</h4>
                <p style="color: #E2E8F0; margin: 0; font-size: 0.92rem;">
                    Fundamental Rights are guaranteed by Part III of the Constitution. They are <b>justiciable</b>, meaning you can approach the Supreme Court (Article 32) or High Courts (Article 226) directly if they are violated.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        search_query = st.text_input(
            "🔍 Search Rights, Articles, or Concepts",
            placeholder="e.g. Article 21, Privacy, Speech, Equality, Untouchability, Arrest...",
            key="rights_search_input"
        ).strip().lower()

        for right in EXPANDED_FUNDAMENTAL_RIGHTS:
            # Search filter check
            if search_query:
                combined_text = (
                    right["title"] + " " +
                    right["articles_range"] + " " +
                    right["overview"] + " " +
                    right["simple_meaning"] + " " +
                    " ".join([a["article"] + " " + a["title"] + " " + a["meaning"] for a in right["articles_detail"]])
                ).lower()
                if search_query not in combined_text:
                    continue

            with st.expander(f"{right['icon']} {right['title']} ({right['articles_range']})", expanded=(search_query != "")):
                # 1. Overview
                st.markdown(f"### 📌 Overview & Constituent Assembly Purpose")
                st.write(right["overview"])

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(
                        f"""
                        <div style="background: rgba(212, 175, 55, 0.08); border-left: 3px solid #D4AF37; padding: 0.8rem; border-radius: 6px; height: 100%;">
                            <h5 style="color: #D4AF37; margin: 0 0 0.3rem 0;">💡 Meaning in Simple Language</h5>
                            <p style="color: #F8FAFC; margin: 0; font-size: 0.9rem;">{right['simple_meaning']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                with col2:
                    st.markdown(
                        f"""
                        <div style="background: rgba(59, 130, 246, 0.08); border-left: 3px solid #3B82F6; padding: 0.8rem; border-radius: 6px; height: 100%;">
                            <h5 style="color: #60A5FA; margin: 0 0 0.3rem 0;">🌟 Why It Matters to Citizens</h5>
                            <p style="color: #F8FAFC; margin: 0; font-size: 0.9rem;">{right['why_it_matters']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                st.markdown("<br>", unsafe_allow_html=True)

                # 4. Rights Covered (Article-by-Article Breakdown)
                st.markdown(f"### 📖 Article-by-Article Breakdown")
                for art in right["articles_detail"]:
                    st.markdown(
                        f"""
                        <div style="background: rgba(30, 41, 59, 0.6); border: 1px solid rgba(148, 163, 184, 0.2); padding: 1rem; border-radius: 8px; margin-bottom: 0.8rem;">
                            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.4rem;">
                                <span style="background: #D4AF37; color: #0B132B; font-weight: 700; padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.85rem;">{art['article']}</span>
                                <b style="color: #F8FAFC; font-size: 1rem;">{art['title']}</b>
                            </div>
                            <p style="color: #CBD5E1; margin: 0 0 0.4rem 0; font-size: 0.92rem;"><b>Constitutional Text:</b> <i>"{art['meaning']}"</i></p>
                            <p style="color: #94A3B8; margin: 0 0 0.4rem 0; font-size: 0.88rem;"><b>Purpose & Scope:</b> {art['purpose']}</p>
                            <p style="color: #10B981; margin: 0; font-size: 0.88rem;"><b>Practical Example:</b> {art['example']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                # Special Writs Breakdown if Article 32
                if "writs_breakdown" in right:
                    st.markdown("#### 📜 The 5 High Constitutional Writs")
                    for writ_item in right["writs_breakdown"]:
                        st.markdown(f"- **{writ_item['writ']}**: {writ_item['desc']}")

                # 5. Real-Life Examples
                st.markdown("### 🎯 Real-Life Practical Scenarios")
                for ex in right["real_life_examples"]:
                    st.markdown(f"- {ex}")

                # 6. Limitations & Reasonable Restrictions
                st.markdown("### ⚖️ Limitations & Reasonable Restrictions")
                st.info("Fundamental Rights are NOT absolute. The State can impose valid legal restrictions under specified constitutional grounds:")
                for lim in right["limitations"]:
                    st.markdown(f"- {lim}")

                # 7. Common Misconceptions
                st.markdown("### ❌ Common Misconceptions Debunked")
                for misc in right["common_misconceptions"]:
                    st.markdown(
                        f"""
                        <div style="background: rgba(239, 68, 68, 0.08); border-left: 3px solid #EF4444; padding: 0.6rem 0.8rem; border-radius: 4px; margin-bottom: 0.5rem;">
                            <b style="color: #FCA5A5;">Myth:</b> {misc['myth']}<br>
                            <b style="color: #34D399;">Truth:</b> {misc['truth']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                # 8. Landmark Judgments
                st.markdown("### 🏛️ Landmark Supreme Court Judgments")
                for case in right["landmark_judgments"]:
                    st.markdown(
                        f"""
                        <div style="background: rgba(139, 92, 246, 0.1); border-left: 3px solid #8B5CF6; padding: 0.6rem 0.8rem; border-radius: 4px; margin-bottom: 0.5rem;">
                            <b style="color: #DDD6FE;">{case['case']}</b><br>
                            <span style="color: #E2E8F0; font-size: 0.9rem;">{case['ruling']}</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                # 9. Quick Facts / Did You Know
                st.markdown(
                    f"""
                    <div style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.15), rgba(255, 153, 51, 0.15)); border: 1px dashed #D4AF37; padding: 0.8rem; border-radius: 8px; margin: 1rem 0;">
                        <b style="color: #D4AF37;">💡 Did You Know?</b>
                        <ul style="color: #F8FAFC; margin: 0.3rem 0 0 1.2rem; font-size: 0.9rem;">
                            {"".join([f"<li>{fact}</li>" for fact in right['quick_facts']])}
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # 10. Interactive FAQs & Related Provisions
                st.markdown("### ❓ Frequently Asked Questions & Related Provisions")
                for faq in right["faqs"]:
                    st.markdown(f"**Q: {faq['q']}**")
                    st.write(f"**A:** {faq['a']}")

                st.markdown(f"**Related Constitutional Provisions:** {', '.join(right['related_provisions'])}")

    # ==================== TAB 2: FUNDAMENTAL DUTIES ====================
    with tab2:
        st.markdown(
            """
            <div style="background: rgba(59, 130, 246, 0.1); border-left: 4px solid #3B82F6; padding: 1rem; border-radius: 6px; margin-bottom: 1rem;">
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
            placeholder="e.g. Flag, Environment, Women, Scientific temper, Education...",
            key="duties_search_input"
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
