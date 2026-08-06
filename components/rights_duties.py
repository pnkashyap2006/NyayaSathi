"""Rights and Duties Component."""

import streamlit as st
from data.constitution import FUNDAMENTAL_RIGHTS, FUNDAMENTAL_DUTIES

def render_rights_duties():
    st.markdown("<h2 style='color: #D4AF37; font-family: \"Cinzel\", serif;'>⚖️ Fundamental Rights & 🛡️ Duties</h2>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Fundamental Rights", "Fundamental Duties"])
    
    with tab1:
        st.markdown("### Fundamental Rights (Part III)")
        st.write("These rights are justiciable and enforceable by the courts.")
        
        for right in FUNDAMENTAL_RIGHTS:
            with st.expander(f"{right['title']} ({right['articles']})"):
                st.write(f"**Description:** {right['description']}")
                st.write(f"**Example:** {right['example']}")
                
    with tab2:
        st.markdown("### Fundamental Duties (Part IVA)")
        st.write("Added by the 42nd Amendment Act (1976) on the recommendation of the Swaran Singh Committee. These are non-justiciable moral obligations.")
        
        for duty in FUNDAMENTAL_DUTIES:
            st.markdown(f"- {duty}")
