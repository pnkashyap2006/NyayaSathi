"""Fundamental Rights Learning Module Component (Part III).

Independent page dedicated strictly to Fundamental Rights (Articles 12 to 35),
featuring Constituent Assembly purpose, article-by-article breakdowns, real-life scenarios,
reasonable restrictions, common misconceptions, landmark judgments, quick facts, and FAQs.
"""

import streamlit as st
from data.constitution import EXPANDED_FUNDAMENTAL_RIGHTS


def render_rights_page():
    """Renders the independent Fundamental Rights (Part III) Learning Module."""
    st.markdown(
        """
        <div class="glass-card" style="border-left: 5px solid #00F3FF !important; padding: 1.8rem; margin-bottom: 1.5rem; text-align: center;">
            <h1 style="color: #00F3FF; font-family: 'Cinzel', serif; font-size: 2.1rem; margin-bottom: 0.4rem; text-shadow: 0 0 15px rgba(0, 243, 255, 0.4);">
                🛡️ Fundamental Rights (Part III)
            </h1>
            <p style="color: #CBD5E1; font-size: 1rem; max-width: 820px; margin: 0 auto; line-height: 1.5;">
                Understand the constitutional rights guaranteed to every citizen of India, their meaning, scope, limitations, landmark judgments, and practical applications.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="glass-card" style="border-left: 4px solid #10B981 !important; padding: 1rem; margin-bottom: 1.2rem;">
            <h4 style="color: #10B981; margin: 0 0 0.3rem 0; font-family: 'Cinzel', serif;">Justiciable Protections Against State Overreach</h4>
            <p style="color: #E2E8F0; margin: 0; font-size: 0.92rem;">
                Fundamental Rights are guaranteed by Part III of the Constitution (Articles 12 to 35). They are <b>justiciable</b>, meaning you can approach the Supreme Court (Article 32) or High Courts (Article 226) directly if they are violated.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    search_query = (
        st.text_input(
            "🔍 Search Fundamental Rights, Articles, or Concepts",
            placeholder="e.g. Equality, Freedom, Article 21, Article 19, Privacy, Untouchability, Arrest...",
            key="rights_page_search",
        )
        .strip()
        .lower()
    )

    for right in EXPANDED_FUNDAMENTAL_RIGHTS:
        # Filter check
        if search_query:
            combined_text = (
                right["title"]
                + " "
                + right["articles_range"]
                + " "
                + right["overview"]
                + " "
                + right["simple_meaning"]
                + " "
                + " ".join(
                    [
                        a["article"] + " " + a["title"] + " " + a["meaning"]
                        for a in right["articles_detail"]
                    ]
                )
            ).lower()
            if search_query not in combined_text:
                continue

        with st.expander(
            f"{right['icon']} {right['title']} ({right['articles_range']})",
            expanded=(search_query != ""),
        ):
            # 1. Overview
            st.markdown("### 📌 Overview & Constituent Assembly Purpose")
            st.write(right["overview"])

            col1, col2 = st.columns(2)
            with col1:
                st.markdown(
                    f"""
                    <div class="glass-card" style="border-left: 3px solid #00F3FF !important; padding: 0.8rem; height: 100%;">
                        <h5 style="color: #00F3FF; margin: 0 0 0.3rem 0;">💡 Meaning in Simple Language</h5>
                        <p style="color: #F8FAFC; margin: 0; font-size: 0.9rem;">{right['simple_meaning']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with col2:
                st.markdown(
                    f"""
                    <div class="glass-card" style="border-left: 3px solid #C084FC !important; padding: 0.8rem; height: 100%;">
                        <h5 style="color: #C084FC; margin: 0 0 0.3rem 0;">🌟 Why It Matters to Citizens</h5>
                        <p style="color: #F8FAFC; margin: 0; font-size: 0.9rem;">{right['why_it_matters']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            st.markdown("<br>", unsafe_allow_html=True)

            # 4. Rights Covered (Article-by-Article Breakdown)
            st.markdown("### 📖 Article-by-Article Breakdown")
            for art in right["articles_detail"]:
                st.markdown(
                    f"""
                    <div class="glass-card" style="border: 1px solid rgba(0, 243, 255, 0.25) !important; padding: 1rem; margin-bottom: 0.8rem;">
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.4rem;">
                            <span style="background: #00F3FF; color: #050314; font-weight: 800; padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.85rem;">{art['article']}</span>
                            <b style="color: #F8FAFC; font-size: 1rem;">{art['title']}</b>
                        </div>
                        <p style="color: #CBD5E1; margin: 0 0 0.4rem 0; font-size: 0.92rem;"><b>Constitutional Text:</b> <i>"{art['meaning']}"</i></p>
                        <p style="color: #94A3B8; margin: 0 0 0.4rem 0; font-size: 0.88rem;"><b>Purpose & Scope:</b> {art['purpose']}</p>
                        <p style="color: #10B981; margin: 0; font-size: 0.88rem;"><b>Practical Example:</b> {art['example']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
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
            st.info(
                "Fundamental Rights are NOT absolute. The State can impose valid legal restrictions under specified constitutional grounds:"
            )
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
                    unsafe_allow_html=True,
                )

            # 8. Landmark Judgments
            st.markdown("### 🏛️ Landmark Supreme Court Judgments")
            for case in right["landmark_judgments"]:
                st.markdown(
                    f"""
                    <div class="glass-card" style="border-left: 3px solid #C084FC !important; padding: 0.6rem 0.8rem; margin-bottom: 0.5rem;">
                        <b style="color: #C084FC;">{case['case']}</b><br>
                        <span style="color: #E2E8F0; font-size: 0.9rem;">{case['ruling']}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # 9. Quick Facts / Did You Know
            st.markdown(
                f"""
                <div class="glass-card" style="border: 1px dashed #00F3FF !important; padding: 0.8rem; margin: 1rem 0;">
                    <b style="color: #00F3FF;">💡 Did You Know?</b>
                    <ul style="color: #CBD5E1; margin: 0.3rem 0 0 1.2rem; font-size: 0.9rem;">
                        {"".join([f"<li>{fact}</li>" for fact in right['quick_facts']])}
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # 10. Interactive FAQs & Related Provisions
            st.markdown("### ❓ Frequently Asked Questions & Related Provisions")
            for faq in right["faqs"]:
                st.markdown(f"**Q: {faq['q']}**")
                st.write(f"**A:** {faq['a']}")

            st.markdown(
                f"**Related Constitutional Provisions:** {', '.join(right['related_provisions'])}"
            )