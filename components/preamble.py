"""Preamble Component for the Indian Legal AI Assistant."""

import streamlit as st
import streamlit.components.v1 as components


def render_preamble():
    st.markdown(
        """
        <h1 style='text-align: center; color: #00F3FF; font-family: "Cinzel", serif; font-size: 2.3rem; margin-bottom: 1.5rem; text-shadow: 0 0 15px rgba(0, 243, 255, 0.4);'>
            📜 The Preamble of India
        </h1>
        """,
        unsafe_allow_html=True,
    )

    # Advanced unrolling scroll animation styled with Cosmic Glassmorphism & Neon Glows
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;800;900&family=Plus+Jakarta+Sans:wght@400;600&display=swap');
    
    body {
        background-color: transparent;
        color: #F8FAFC;
        font-family: 'Cinzel', serif;
        text-align: center;
        overflow: hidden;
        margin: 0;
        padding: 10px;
    }

    .scroll-container {
        width: 85%;
        margin: 15px auto;
        padding: 40px 30px;
        background: rgba(13, 10, 32, 0.85);
        border: 2px solid #00F3FF;
        border-radius: 16px;
        box-shadow: 0 0 35px rgba(0, 243, 255, 0.3), inset 0 0 20px rgba(192, 132, 252, 0.1);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        position: relative;
        transform-origin: top center;
        animation: unfold 2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    /* Scroll Roller Handles - Neon Violet Glow */
    .scroll-container::before, .scroll-container::after {
        content: '';
        position: absolute;
        left: -2%;
        right: -2%;
        height: 16px;
        background: linear-gradient(90deg, #120831 0%, #C084FC 50%, #120831 100%);
        border: 1px solid #00F3FF;
        border-radius: 8px;
        box-shadow: 0 0 15px rgba(192, 132, 252, 0.6);
    }
    .scroll-container::before { top: -10px; }
    .scroll-container::after { bottom: -10px; }

    .preamble-text {
        opacity: 0;
        transform: translateY(20px);
        animation: fadeUp 1.2s ease-out forwards;
        margin: 12px 0;
        line-height: 1.5;
        letter-spacing: 0.02em;
    }

    .preamble-title {
        font-size: 24px;
        font-weight: 800;
        color: #00F3FF;
        text-shadow: 0 0 10px rgba(0, 243, 255, 0.6);
    }

    .preamble-highlight {
        font-size: 19px;
        font-weight: 700;
        color: #C084FC;
        text-shadow: 0 0 8px rgba(192, 132, 252, 0.5);
    }

    .preamble-body {
        font-size: 17px;
        color: #CBD5E1;
    }

    @keyframes unfold {
        0% { transform: scaleY(0); opacity: 0; }
        100% { transform: scaleY(1); opacity: 1; }
    }

    @keyframes fadeUp {
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
    </head>
    <body>
        <div class="scroll-container">
            <p class="preamble-text preamble-title" style="animation-delay: 0.6s;">WE, THE PEOPLE OF INDIA,</p>
            <p class="preamble-text preamble-body" style="animation-delay: 1.0s;">having solemnly resolved to constitute India into a</p>
            <p class="preamble-text preamble-title" style="animation-delay: 1.4s; font-size: 21px;">SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC</p>
            <p class="preamble-text preamble-body" style="animation-delay: 1.8s;">and to secure to all its citizens:</p>
            <p class="preamble-text preamble-highlight" style="animation-delay: 2.2s;">JUSTICE, social, economic and political;</p>
            <p class="preamble-text preamble-highlight" style="animation-delay: 2.6s;">LIBERTY of thought, expression, belief, faith and worship;</p>
            <p class="preamble-text preamble-highlight" style="animation-delay: 3.0s;">EQUALITY of status and of opportunity;</p>
            <p class="preamble-text preamble-body" style="animation-delay: 3.4s;">and to promote among them all</p>
            <p class="preamble-text preamble-highlight" style="animation-delay: 3.8s;">FRATERNITY assuring the dignity of the individual</p>
            <p class="preamble-text preamble-highlight" style="animation-delay: 4.2s;">and the unity and integrity of the Nation;</p>
            <p class="preamble-text preamble-body" style="animation-delay: 4.6s;">IN OUR CONSTITUENT ASSEMBLY this twenty-sixth day of November, 1949,</p>
            <p class="preamble-text preamble-title" style="animation-delay: 5.0s; font-size: 18px;">do HEREBY ADOPT, ENACT AND GIVE TO OURSELVES THIS CONSTITUTION.</p>
        </div>
    </body>
    </html>
    """

    components.html(html_code, height=620)

    st.markdown(
        """
        <div class="glass-card" style="border-left: 5px solid #00F3FF !important; margin-top: 1.5rem; padding: 1.2rem;">
            <p style="color: #CBD5E1; margin: 0; font-size: 0.95rem; line-height: 1.6;">
                💡 <b>Constitutional Note:</b> The Preamble serves as the guiding soul and foundational key to the Indian Constitution. It outlines the core values, democratic philosophy, and socio-economic objectives upon which the sovereign Indian Republic is built.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )