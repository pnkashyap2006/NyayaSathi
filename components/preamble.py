"""Preamble Component for the Indian Legal AI Assistant."""

import streamlit as st
import streamlit.components.v1 as components
from data.constitution import PREAMBLE_TEXT

def render_preamble():
    st.markdown("<h1 style='text-align: center; color: #D4AF37; font-family: \"Cinzel\", serif;'>The Preamble</h1>", unsafe_allow_html=True)
    
    # Advanced animation using iframe/components
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');
    body {
        background-color: transparent;
        color: #F8F5E6;
        font-family: 'Cinzel', serif;
        text-align: center;
        overflow: hidden;
    }
    .scroll-container {
        width: 80%;
        margin: 0 auto;
        padding: 40px;
        background: linear-gradient(to bottom, rgba(248, 245, 230, 0.1), rgba(248, 245, 230, 0.05));
        border: 2px solid #D4AF37;
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
        position: relative;
        animation: unfold 2s ease-out forwards;
    }
    .scroll-container::before, .scroll-container::after {
        content: '';
        position: absolute;
        left: 0;
        right: 0;
        height: 20px;
        background: #8B5A2B;
        border-radius: 5px;
    }
    .scroll-container::before { top: -10px; }
    .scroll-container::after { bottom: -10px; }
    
    .preamble-text {
        opacity: 0;
        transform: translateY(20px);
        animation: fadeUp 1.5s ease-out forwards;
    }
    
    .preamble-text:nth-child(1) { font-size: 24px; font-weight: bold; color: #FF9933; animation-delay: 0.5s; }
    .preamble-text:nth-child(3) { font-size: 22px; font-weight: bold; color: #138808; animation-delay: 1.5s; }
    
    @keyframes unfold {
        0% { transform: scaleY(0); }
        100% { transform: scaleY(1); }
    }
    @keyframes fadeUp {
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
    </head>
    <body>
        <div class="scroll-container">
            <p class="preamble-text" style="animation-delay: 1s;">WE, THE PEOPLE OF INDIA,</p>
            <p class="preamble-text" style="animation-delay: 1.5s;">having solemnly resolved to constitute India into a</p>
            <p class="preamble-text" style="animation-delay: 2s;">SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC</p>
            <p class="preamble-text" style="animation-delay: 2.5s;">and to secure to all its citizens:</p>
            <p class="preamble-text" style="animation-delay: 3s; color: #D4AF37;">JUSTICE, social, economic and political;</p>
            <p class="preamble-text" style="animation-delay: 3.5s; color: #D4AF37;">LIBERTY of thought, expression, belief, faith and worship;</p>
            <p class="preamble-text" style="animation-delay: 4s; color: #D4AF37;">EQUALITY of status and of opportunity;</p>
            <p class="preamble-text" style="animation-delay: 4.5s;">and to promote among them all</p>
            <p class="preamble-text" style="animation-delay: 5s; color: #D4AF37;">FRATERNITY assuring the dignity of the individual</p>
            <p class="preamble-text" style="animation-delay: 5.5s; color: #D4AF37;">and the unity and integrity of the Nation;</p>
            <p class="preamble-text" style="animation-delay: 6s;">IN OUR CONSTITUENT ASSEMBLY this twenty-sixth day of November, 1949,</p>
            <p class="preamble-text" style="animation-delay: 6.5s; font-weight: bold;">do HEREBY ADOPT, ENACT AND GIVE TO OURSELVES THIS CONSTITUTION.</p>
        </div>
    </body>
    </html>
    """
    
    components.html(html_code, height=600)
    
    st.info("The Preamble is the soul of the Constitution. It outlines the fundamental values, philosophy, and objectives upon which the Indian Constitution is based.")
