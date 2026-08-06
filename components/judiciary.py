"""Judiciary Component."""

import streamlit as st

def render_judiciary():
    st.markdown("<h2 style='color: #D4AF37; font-family: \"Cinzel\", serif;'>🏛️ Indian Judiciary</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    The Indian Judiciary is an integrated and independent system that acts as the guardian of the Constitution.
    """)
    
    st.markdown("### Supreme Court of India")
    st.write("The apex court of India, established under Article 124 of the Constitution.")
    st.markdown("""
    - **Original Jurisdiction:** Disputes between the Government of India and one or more States.
    - **Appellate Jurisdiction:** Appeals against judgments of High Courts.
    - **Writ Jurisdiction:** Enforcement of Fundamental Rights (Article 32).
    - **Advisory Jurisdiction:** President can seek the Supreme Court's opinion (Article 143).
    """)
    
    st.markdown("### High Courts")
    st.write("The highest judicial body at the State level.")
    st.write("Under Article 226, High Courts have the power to issue writs for the enforcement of Fundamental Rights and for any other purpose.")
    
    st.markdown("### Subordinate Courts")
    st.write("Includes District Courts, Sessions Courts, and other lower courts dealing with civil and criminal cases at the district level.")
