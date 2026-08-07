"""Constitution Explorer Component for NyayaSathi AI Legal Consultant.

Transforms the Constitution page into an interactive, discoverable Constitution Knowledge Portal featuring:
1. Cosmic Glass Hero Banner
2. Constitution at a Glance (Statistic Cards)
3. Interactive Constitution Explorer (Major Topic Cards)
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
    
    # 1. Hero Section (Cosmic Glass Banner)
    st.markdown(
        """
        <div class="glass-card" style="padding: 2.2rem; text-align: center; border-color: rgba(0, 243, 255, 0.35) !important;">
            <div style="font-size: 3rem; margin-bottom: 0.3rem; filter: drop-shadow(0 0 10px rgba(0,243,255,0.5));">📖</div>
            <h1 style="color: #00F3FF; font-family: 'Cinzel', serif; font-size: 2.3rem; margin-bottom: 0.5rem; text-shadow: 0 0 15px rgba(0, 243, 255, 0.4);">
                Constitution Explorer & Knowledge Portal
            </h1>
            <p style="color: #CBD5E1; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.05rem; max-width: 820px; margin: 0 auto 1.2rem auto; line-height: 1.6;">
                Explore the supreme law of the Republic of India. Discover constitutional provisions, fundamental guarantees, institutional powers, landmark judgments, and key articles in simple, accessible language.
            </p>
            <div style="display: flex; justify-content: center; gap: 1.2rem; flex-wrap: wrap;">
                <span style="background: rgba(0, 243, 255, 0.12); border: 1px solid rgba(0, 243, 255, 0.4); color: #00F3FF; padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.88rem; font-weight: 600;">
                    📅 <b>Adopted:</b> 26 November 1949
                </span>
                <span style="background: rgba(192, 132, 252, 0.12); border: 1px solid rgba(192, 132, 252, 0.4); color: #C084FC; padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.88rem; font-weight: 600;">
                    🚀 <b>Effective:</b> 26 January 1950
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 2. Constitution at a Glance (Statistic Cards)
    st.markdown("<h3 style='color: #00F3FF; font-family: \"Cinzel\", serif; margin-bottom: 0.8rem;'>📊 Constitution at a Glance</h3>", unsafe_allow_html=True)
    cols = st.columns(6)
    for idx, stat in enumerate(CONSTITUTION_STATS):
        with cols[idx]:
            st.markdown(
                f"""
                <div style="background: rgba(13, 10, 32, 0.75); border: 1px solid rgba(0, 243, 255, 0.25); border-radius: 12px; padding: 1rem 0.5rem; text-align: center; height: 110px; display: flex; flex-direction: column; justify-content: center; backdrop-filter: blur(12px);">
                    <div style="color: #00F3FF; font-size: 1.3rem; font-weight: 800; line-height: 1.1;">{stat['value']}</div>
                    <div style="color: #F8FAFC; font-size: 0.82rem; font-weight: 600; margin: 0.3rem 0 0.1rem 0;">{stat['label']}</div>
                    <div style="color: #94A3B8; font-size: 0.72rem;">{stat['sub']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. Live Search the Constitution
    st.markdown("<h3 style='color: #00F3FF; font-family: \"Cinzel\", serif;'>🔍 Search the Constitution</h3>", unsafe_allow_html=True)
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
                    <div class="glass-card" style="border-left: 5px solid #00F3FF !important; margin-bottom: 0.8rem; padding: 1.1rem;">
                        <b style="color: #00F3FF; font-size: 1.05rem;">{topic['icon']} {topic['title']}</b> ({topic['articles']})<br>
                        <span style="color: #CBD5E1; font-size: 0.92rem; line-height: 1.5; display: block; margin-top: 0.3rem;">{topic['desc']}</span>
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
                    <div class="glass-card" style="border-left: 5px solid #C084FC !important; margin-bottom: 0.8rem; padding: 1.1rem;">
                        <b style="color: #C084FC; font-size: 1.05rem;">{art['article']}: {art['title']}</b><br>
                        <span style="color: #E2E8F0; font-size: 0.92rem; line-height: 1.5; display: block; margin: 0.3rem 0;">{art['summary']}</span>
                        <small style="color: #94A3B8;"><b>Significance:</b> {art['significance']}</small>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        if not matched:
            st.info(f"No direct matches found for '{search_query}'. Try searching for 'Article 21', 'Parliament', or 'Emergency'.")
        st.divider()

    # 4. Interactive Constitution Explorer (16 Major Topics Grid)
    st.markdown("<h3 style='color: #00F3FF; font-family: \"Cinzel\", serif;'>🌐 Major Constitutional Topics</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8; margin-bottom: 1rem;'>Select any topic to navigate or explore its constitutional provisions:</p>", unsafe_allow_html=True)

    grid_cols = st.columns(4)
    for idx, topic in enumerate(MAJOR_CONSTITUTIONAL_TOPICS):
        col_idx = idx % 4
        with grid_cols[col_idx]:
            st.markdown(
                f"""
                <div class="glass-card" style="height: 190px; margin-bottom: 0.8rem; padding: 1rem; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.4rem;">
                            <span style="font-size: 1.4rem;">{topic['icon']}</span>
                            <span style="background: rgba(0, 243, 255, 0.15); border: 1px solid rgba(0, 243, 255, 0.3); color: #00F3FF; font-size: 0.72rem; font-weight: 700; padding: 0.1rem 0.5rem; border-radius: 4px;">{topic['articles']}</span>
                        </div>
                        <h4 style="color: #F8FAFC; font-size: 0.98rem; margin: 0 0 0.3rem 0; font-family: 'Cinzel', serif;">{topic['title']}</h4>
                        <p style="color: #CBD5E1; font-size: 0.8rem; margin: 0; line-height: 1.4; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">{topic['desc']}</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            if topic.get("nav_target"):
                if st.button(f"Explore {topic['title']}", key=f"btn_nav_{topic['id']}", use_container_width=True):
                    st.session_state.navigation_mode = topic["nav_target"]
                    st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # 5. Popular & Landmark Articles
    st.markdown("<h3 style='color: #00F3FF; font-family: \"Cinzel\", serif;'>⭐ Popular & Landmark Articles</h3>", unsafe_allow_html=True)
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
        <div class="glass-card" style="border: 1px dashed #00F3FF !important; background: rgba(13, 10, 32, 0.85) !important; padding: 1.4rem; margin-bottom: 1.5rem;">
            <h4 style="color: #00F3FF; font-family: 'Cinzel', serif; margin: 0 0 0.6rem 0; font-size: 1.15rem;">💡 Did You Know? — Fascinating Constitutional Facts</h4>
            <ul style="color: #CBD5E1; margin: 0 0 0 1.2rem; font-size: 0.93rem; line-height: 1.7;">
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
        <div class="glass-card" style="border-left: 5px solid #C084FC !important; padding: 1.5rem; margin-bottom: 1.2rem;">
            <h3 style="color: #C084FC; font-family: 'Cinzel', serif; margin-bottom: 0.3rem;">
                🤖 Ask the AI Constitution Assistant
            </h3>
            <p style="color: #CBD5E1; font-size: 0.92rem; margin-bottom: 0;">
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