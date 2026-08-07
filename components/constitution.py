"""Constitution Explorer Component for NyayaSathi.

Transforms the Constitution page into an interactive, discoverable Constitution Knowledge Portal featuring:
1. Modern Hero Banner
2. Constitution at a Glance (Statistic Cards)
3. Interactive Constitution Explorer (16 Topic Cards)
4. Live Search Engine across Articles & Institutions
5. Popular & Landmark Articles Cards
6. Rotating 'Did You Know?' Constitutional Facts
7. 'Ask the Constitution' AI Assistant Starters
8. Optional Expandable History Section
"""

import streamlit as st
from data.constitution_explorer import (
    CONSTITUTION_STATS,
    MAJOR_CONSTITUTIONAL_TOPICS,
    POPULAR_ARTICLES,
    CONSTITUTIONAL_FACTS,
    ASK_CONSTITUTION_STARTERS
)
from data.timeline import TIMELINE_EVENTS


def render_constitution():
    """Renders the Interactive Constitution Explorer & Knowledge Portal."""
    # 1. Hero Section
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, rgba(11, 19, 43, 0.95), rgba(30, 45, 80, 0.9)); border: 1px solid rgba(212, 175, 55, 0.35); border-radius: 14px; padding: 2rem; margin-bottom: 1.5rem; text-align: center;">
            <div style="font-size: 2.8rem; margin-bottom: 0.3rem;">📖</div>
            <h1 style="color: #D4AF37; font-family: 'Cinzel', serif; font-size: 2.3rem; margin-bottom: 0.5rem;">
                Constitution Explorer & Knowledge Portal
            </h1>
            <p style="color: #CBD5E1; font-size: 1.05rem; max-width: 820px; margin: 0 auto 1rem auto; line-height: 1.6;">
                Explore the supreme law of the Republic of India. Discover constitutional provisions, fundamental guarantees, institutional powers, landmark judgments, and key articles in simple, accessible language.
            </p>
            <div style="display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap;">
                <span style="background: rgba(212, 175, 55, 0.15); border: 1px solid #D4AF37; color: #F8FAFC; padding: 0.3rem 0.9rem; border-radius: 20px; font-size: 0.88rem;">
                    📅 <b>Adopted:</b> 26 November 1949
                </span>
                <span style="background: rgba(16, 185, 129, 0.15); border: 1px solid #10B981; color: #F8FAFC; padding: 0.3rem 0.9rem; border-radius: 20px; font-size: 0.88rem;">
                    🚀 <b>Effective:</b> 26 January 1950
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 2. Constitution at a Glance (Statistic Cards)
    st.markdown("<h3 style='color: #F8FAFC; font-family: \"Cinzel\", serif;'>📊 Constitution at a Glance</h3>", unsafe_allow_html=True)
    cols = st.columns(6)
    for idx, stat in enumerate(CONSTITUTION_STATS):
        with cols[idx]:
            st.markdown(
                f"""
                <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 10px; padding: 0.9rem 0.5rem; text-align: center;">
                    <div style="color: #D4AF37; font-size: 1.3rem; font-weight: 800;">{stat['value']}</div>
                    <div style="color: #F8FAFC; font-size: 0.85rem; font-weight: 600; margin: 0.2rem 0;">{stat['label']}</div>
                    <div style="color: #94A3B8; font-size: 0.75rem;">{stat['sub']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. Live Search the Constitution
    st.markdown("<h3 style='color: #F8FAFC; font-family: \"Cinzel\", serif;'>🔍 Search the Constitution</h3>", unsafe_allow_html=True)
    search_query = st.text_input(
        "Search by Article Number, Institution, Topic, or Term",
        placeholder="e.g. Article 21, Parliament, Emergency, Governor, Judiciary, DPSP, Article 368...",
        key="constitution_explorer_search"
    ).strip().lower()

    if search_query:
        st.markdown(f"#### Search Results for *'{search_query}'*:")
        matched = False
        for topic in MAJOR_CONSTITUTIONAL_TOPICS:
            c_text = (topic["title"] + " " + topic["articles"] + " " + topic["desc"]).lower()
            if search_query in c_text:
                matched = True
                st.markdown(
                    f"""
                    <div style="background: rgba(30, 41, 59, 0.6); border-left: 4px solid #D4AF37; padding: 1rem; border-radius: 6px; margin-bottom: 0.6rem;">
                        <b style="color: #D4AF37; font-size: 1.05rem;">{topic['icon']} {topic['title']}</b> ({topic['articles']})<br>
                        <span style="color: #CBD5E1; font-size: 0.92rem;">{topic['desc']}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        for art in POPULAR_ARTICLES:
            c_text = (art["article"] + " " + art["title"] + " " + art["summary"] + " " + art["significance"]).lower()
            if search_query in c_text:
                matched = True
                st.markdown(
                    f"""
                    <div style="background: rgba(16, 185, 129, 0.08); border-left: 4px solid #10B981; padding: 1rem; border-radius: 6px; margin-bottom: 0.6rem;">
                        <b style="color: #34D399; font-size: 1.05rem;">{art['article']}: {art['title']}</b><br>
                        <span style="color: #E2E8F0; font-size: 0.92rem;">{art['summary']}</span><br>
                        <small style="color: #94A3B8;"><b>Significance:</b> {art['significance']}</small>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        if not matched:
            st.info(f"No direct matches found for '{search_query}'. Try searching for 'Article 21', 'Parliament', or 'Emergency'.")
        st.divider()

    # 4. Interactive Constitution Explorer (16 Major Topics Grid)
    st.markdown("<h3 style='color: #F8FAFC; font-family: \"Cinzel\", serif;'>🌐 Major Constitutional Topics</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8; margin-bottom: 1rem;'>Select any topic to navigate or explore its constitutional provisions:</p>", unsafe_allow_html=True)

    grid_cols = st.columns(4)
    for idx, topic in enumerate(MAJOR_CONSTITUTIONAL_TOPICS):
        col_idx = idx % 4
        with grid_cols[col_idx]:
            st.markdown(
                f"""
                <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(212, 175, 55, 0.25); border-radius: 10px; padding: 1rem; height: 185px; margin-bottom: 1rem; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.4rem;">
                            <span style="font-size: 1.4rem;">{topic['icon']}</span>
                            <span style="background: rgba(212, 175, 55, 0.15); color: #D4AF37; font-size: 0.72rem; font-weight: 700; padding: 0.1rem 0.4rem; border-radius: 4px;">{topic['articles']}</span>
                        </div>
                        <h4 style="color: #F8FAFC; font-size: 0.98rem; margin: 0 0 0.3rem 0; font-family: 'Cinzel', serif;">{topic['title']}</h4>
                        <p style="color: #94A3B8; font-size: 0.8rem; margin: 0; line-height: 1.35; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">{topic['desc']}</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            if topic["nav_target"]:
                if st.button(f"Explore {topic['title']}", key=f"btn_nav_{topic['id']}", use_container_width=True):
                    st.session_state.navigation_mode = topic["nav_target"]
                    st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # 5. Popular & Landmark Articles
    st.markdown("<h3 style='color: #F8FAFC; font-family: \"Cinzel\", serif;'>⭐ Popular & Landmark Articles</h3>", unsafe_allow_html=True)
    pop_cols = st.columns(3)
    for idx, art in enumerate(POPULAR_ARTICLES):
        col_idx = idx % 3
        with pop_cols[col_idx]:
            with st.expander(f"📌 {art['article']}: {art['title']}"):
                st.markdown(f"**Constitutional Provision:**")
                st.write(art["summary"])
                st.markdown(f"**Legal Significance:**")
                st.write(art["significance"])

    st.markdown("<br>", unsafe_allow_html=True)

    # 6. Did You Know? (Rotating Constitutional Facts)
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.12), rgba(255, 153, 51, 0.12)); border: 1px dashed #D4AF37; border-radius: 12px; padding: 1.2rem; margin-bottom: 1.5rem;">
            <h4 style="color: #D4AF37; margin: 0 0 0.5rem 0;">💡 Did You Know? — Fascinating Constitutional Facts</h4>
            <ul style="color: #F8FAFC; margin: 0 0 0 1.2rem; font-size: 0.93rem; line-height: 1.6;">
                <li><b>Dr. B. R. Ambedkar</b> served as the Chairman of the Drafting Committee and is recognized as the Chief Architect of the Constitution.</li>
                <li><b>Article 32</b> was described by Dr. Ambedkar as the <i>"very soul of the Constitution and the very heart of it"</i>.</li>
                <li>India's Constitution is the <b>longest written national constitution</b> in the world.</li>
                <li>The original Constitution was handwritten by master calligrapher <b>Prem Behari Narain Raizada</b> in flowing italic style.</li>
                <li>The original pages were illustrated by renowned artists from Santiniketan, including <b>Nandalal Bose</b>.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 7. AI Constitution Assistant ("Ask the Constitution")
    st.markdown(
        """
        <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(6, 182, 212, 0.3); border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem;">
            <h3 style="color: #06B6D4; font-family: 'Cinzel', serif; margin-bottom: 0.3rem;">
                🤖 Ask the AI Constitution Assistant
            </h3>
            <p style="color: #CBD5E1; font-size: 0.92rem; margin-bottom: 1rem;">
                Select any question below to immediately ask NyayaSathi's live AI engine:
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    prompt_cols = st.columns(3)
    for idx, prompt_text in enumerate(ASK_CONSTITUTION_STARTERS):
        col_idx = idx % 3
        with prompt_cols[col_idx]:
            if st.button(f"💬 {prompt_text}", key=f"btn_ask_const_{idx}", use_container_width=True):
                st.session_state.pending_user_input = prompt_text
                st.session_state.navigation_mode = "home"
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # 8. Optional Expandable History Section
    with st.expander("📜 History & Making of the Constitution (1946–1950)"):
        st.markdown("<p style='color: #94A3B8;'>Chronological timeline of the Constituent Assembly debates and drafting milestones:</p>", unsafe_allow_html=True)
        for event in TIMELINE_EVENTS:
            st.markdown(f"**{event['date']} — {event['title']}**")
            st.write(event["description"])
            st.markdown("---")
