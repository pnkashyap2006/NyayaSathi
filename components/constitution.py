"""Constitution Explorer Component."""

import streamlit as st
from data.timeline import TIMELINE_EVENTS

def render_constitution():
    st.markdown("<h2 style='color: #D4AF37; font-family: \"Cinzel\", serif;'>📖 Constitution of India</h2>", unsafe_allow_html=True)
    st.write("Explore the supreme law of India, adopted on 26th November 1949 and effective from 26th January 1950.")
    
    st.divider()
    st.markdown("### Making of the Constitution")
    
    for event in TIMELINE_EVENTS:
        st.markdown(f"**{event['date']} - {event['title']}**")
        st.write(event['description'])
        st.markdown("---")
        
    st.info("The Constitution originally had 395 Articles in 22 Parts and 8 Schedules. Today, it has over 470 Articles, 25 Parts, and 12 Schedules.")
