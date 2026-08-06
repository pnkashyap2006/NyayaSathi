"""Laws Component."""

import streamlit as st
from data.landmark_acts import MAJOR_LAWS

def render_laws():
    st.markdown("<h2 style='color: #D4AF37; font-family: \"Cinzel\", serif;'>📚 Landmark Indian Laws</h2>", unsafe_allow_html=True)
    
    st.write("Explore key legislations that shape the legal landscape of India.")
    
    for law in MAJOR_LAWS:
        with st.expander(f"📌 {law['title']}"):
            st.write(f"**Overview:** {law['overview']}")
            
            st.write("**Key Provisions:**")
            for provision in law['key_provisions']:
                st.markdown(f"- {provision}")
                
            st.write(f"**When it applies:** {law['when_it_applies']}")
            st.write(f"**Common Misconceptions:** {law['common_misconceptions']}")
