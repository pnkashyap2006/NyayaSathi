"""CSS animations and glassmorphism styling module for Indian Legal AI Assistant.

Injects custom CSS keyframes, card styles, loading shimmers, and gradient typography
into the Streamlit app layout.
"""

import streamlit as st


def inject_custom_css():
    """Injects custom CSS design system into current Streamlit session."""
    custom_css = """
    <style>
    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    /* Global Typography & Reset */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #F8FAFC !important;
    }

    h1, h2, h3, .hero-title {
        font-family: 'Cinzel', serif !important;
    }

    /* Main Container Background - Deep Cosmic Navy with Neon Radial Glows */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #050314 !important;
        background-image: 
            radial-gradient(circle at 15% 20%, rgba(0, 243, 255, 0.08) 0%, transparent 45%),
            radial-gradient(circle at 85% 80%, rgba(192, 132, 252, 0.10) 0%, transparent 45%),
            radial-gradient(circle at 50% 50%, rgba(13, 10, 32, 0.6) 0%, transparent 100%) !important;
        background-attachment: fixed !important;
    }

    /* Keyframe Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideRight {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }

    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 0 15px rgba(0, 243, 255, 0.2); }
        50% { box-shadow: 0 0 30px rgba(0, 243, 255, 0.5); }
    }

    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }

    /* Animated Title & Hero Header */
    .hero-container {
        text-align: center;
        padding: 3rem 1.5rem 2.5rem 1.5rem;
        position: relative;
        overflow: hidden;
        border-radius: 20px;
        background: rgba(13, 10, 32, 0.75);
        border: 1px solid rgba(0, 243, 255, 0.35);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.8), inset 0 0 20px rgba(0, 243, 255, 0.05);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        margin-bottom: 2rem;
        animation: fadeIn 0.8s ease-out;
    }
    
    .hero-silhouettes {
        font-size: 8rem;
        opacity: 0.04;
        position: absolute;
        bottom: -20px;
        left: 0;
        width: 100%;
        display: flex;
        justify-content: space-around;
        pointer-events: none;
        z-index: 0;
        filter: drop-shadow(0 0 10px rgba(0, 243, 255, 0.8));
    }

    .hero-title-container {
        position: relative;
        z-index: 1;
        animation: slideUp 0.8s ease-out;
    }

    .hero-title {
        font-size: 3.2rem;
        font-weight: 900;
        background: linear-gradient(120deg, #FFFFFF 0%, #00F3FF 50%, #C084FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 0.02em;
        margin-bottom: 0.5rem;
        display: inline-flex;
        align-items: center;
        gap: 0.75rem;
        text-shadow: 0 0 20px rgba(0, 243, 255, 0.2);
    }

    .hero-subtitle {
        font-size: 1.2rem;
        color: #CBD5E1;
        max-width: 720px;
        margin: 0 auto;
        line-height: 1.6;
        font-weight: 400;
        font-family: 'Cinzel', serif;
    }

    /* Glassmorphism Card Style */
    .glass-card {
        background: rgba(13, 10, 32, 0.75) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 243, 255, 0.25) !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        margin-bottom: 1.25rem !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.6), inset 0 0 15px rgba(0, 243, 255, 0.03) !important;
        transition: all 0.3s ease !important;
        animation: slideUp 0.5s ease-out backwards;
    }

    .glass-card:hover {
        transform: translateY(-3px) !important;
        border-color: rgba(0, 243, 255, 0.5) !important;
        box-shadow: 0 12px 40px 0 rgba(0, 243, 255, 0.15), inset 0 0 20px rgba(0, 243, 255, 0.05) !important;
    }
    
    /* Parchment Card variant (Modernized Cosmic Glass Style) */
    .parchment-card {
        background: rgba(13, 10, 32, 0.85) !important;
        color: #F8FAFC !important;
        border: 1px solid rgba(192, 132, 252, 0.4) !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7), inset 0 0 20px rgba(192, 132, 252, 0.05) !important;
        backdrop-filter: blur(20px) !important;
    }
    .parchment-card .card-header {
        color: #C084FC !important;
        font-family: 'Cinzel', serif !important;
    }
    .parchment-card p, .parchment-card li {
        color: #CBD5E1 !important;
    }

    /* Response Section Cards with Theme Borders */
    .card-legal-topic {
        border-left: 5px solid #00F3FF !important; /* Neon Cyan */
    }

    .card-summary {
        border-left: 5px solid #C084FC !important; /* Neon Violet */
    }

    .card-important-points {
        border-left: 5px solid #38BDF8 !important; /* Sky Blue */
    }
    
    .card-articles {
        border-left: 5px solid #00F3FF !important;
    }
    
    .card-acts {
        border-left: 5px solid #C084FC !important;
    }

    .card-considerations {
        border-left: 5px solid #F59E0B !important;
    }

    .card-next-steps {
        border-left: 5px solid #10B981 !important;
    }

    .card-disclaimer {
        border-left: 5px solid #EF4444 !important;
        background: rgba(239, 68, 68, 0.08) !important;
    }

    /* Card Section Titles */
    .card-header {
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.6rem;
        color: #00F3FF; /* Cyan text */
        font-family: 'Cinzel', serif;
    }

    .card-list {
        margin: 0;
        padding-left: 1.2rem;
        color: #CBD5E1;
        line-height: 1.7;
    }

    .card-list li {
        margin-bottom: 0.5rem;
    }

    /* Glowing Input Container */
    .stTextArea textarea, .stTextInput input {
        background-color: rgba(8, 5, 26, 0.85) !important;
        border: 1px solid rgba(0, 243, 255, 0.3) !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }

    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #00F3FF !important;
        box-shadow: 0 0 18px rgba(0, 243, 255, 0.35) !important;
    }

    /* Buttons - Neon Cyan & Violet Glow */
    .stButton button {
        background: rgba(13, 10, 32, 0.8) !important;
        color: #F8FAFC !important;
        border: 1px solid rgba(0, 243, 255, 0.35) !important;
        border-radius: 10px !important;
        padding: 0.5rem 1.4rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.02em !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4) !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    .stButton button:hover {
        background: linear-gradient(135deg, rgba(0, 243, 255, 0.2) 0%, rgba(192, 132, 252, 0.2) 100%) !important;
        border-color: #00F3FF !important;
        color: #FFFFFF !important;
        box-shadow: 0 0 18px rgba(0, 243, 255, 0.4) !important;
        transform: translateY(-2px) !important;
    }

    /* Loading Shimmer Progress Bar */
    .shimmer-progress {
        height: 4px;
        width: 100%;
        background: linear-gradient(90deg, rgba(0,243,255,0.1) 0%, rgba(0,243,255,0.8) 50%, rgba(192,132,252,0.1) 100%);
        background-size: 200% 100%;
        animation: shimmer 1.5s infinite linear;
        border-radius: 4px;
        margin: 1rem 0;
    }

    /* Translucent Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(8, 5, 26, 0.95) !important;
        border-right: 1px solid rgba(0, 243, 255, 0.2) !important;
        backdrop-filter: blur(20px);
    }
    
    /* Timeline styles */
    .timeline {
        position: relative;
        max-width: 1200px;
        margin: 0 auto;
    }
    .timeline::after {
        content: '';
        position: absolute;
        width: 4px;
        background-color: rgba(0, 243, 255, 0.3);
        top: 0;
        bottom: 0;
        left: 50%;
        margin-left: -2px;
    }
    .timeline-container {
        padding: 10px 40px;
        position: relative;
        background-color: inherit;
        width: 50%;
    }
    .timeline-container::after {
        content: '';
        position: absolute;
        width: 20px;
        height: 20px;
        right: -10px;
        background-color: #050314;
        border: 4px solid #00F3FF;
        top: 15px;
        border-radius: 50%;
        z-index: 1;
        box-shadow: 0 0 10px rgba(0, 243, 255, 0.6);
    }
    .left { left: 0; }
    .right { left: 50%; }
    .right::after { left: -10px; }

    /* Sticky Footer */
    .sticky-footer {
        position: relative;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        padding: 1.8rem 0 1rem 0;
        color: #64748B;
        font-size: 0.88rem;
        border-top: 1px solid rgba(0, 243, 255, 0.15);
        margin-top: 3rem;
    }

    /* Emergency Helpline Banner */
    .emergency-banner {
        background: rgba(239, 68, 68, 0.12);
        border-left: 6px solid #EF4444;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 0 20px rgba(239, 68, 68, 0.25);
        animation: pulseGlow 2s infinite;
    }
    .emergency-title {
        font-weight: 700;
        color: #F87171;
        font-size: 1.15rem;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .emergency-helpline {
        display: inline-block;
        background: #DC2626;
        color: #FFFFFF;
        font-weight: 700;
        padding: 0.3rem 0.8rem;
        border-radius: 8px;
        font-size: 1.05rem;
        margin-top: 0.5rem;
    }

    /* Official Reference Badges */
    .badge-ref-law {
        display: inline-flex;
        align-items: center;
        background: rgba(0, 243, 255, 0.12);
        border: 1px solid rgba(0, 243, 255, 0.4);
        color: #00F3FF;
        padding: 0.35rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.2rem;
    }
    .badge-ref-constitution {
        display: inline-flex;
        align-items: center;
        background: rgba(192, 132, 252, 0.12);
        border: 1px solid rgba(192, 132, 252, 0.4);
        color: #C084FC;
        padding: 0.35rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.2rem;
    }

    /* Collapsible Legal Reasoning Card */
    .reasoning-card {
        background: rgba(13, 10, 32, 0.8);
        border: 1px solid rgba(0, 243, 255, 0.3);
        border-radius: 12px;
        padding: 1.2rem;
        margin: 1rem 0;
        backdrop-filter: blur(15px);
    }
    .reasoning-card details summary {
        cursor: pointer;
        font-weight: 700;
        color: #00F3FF;
        font-size: 1.05rem;
        outline: none;
        user-select: none;
    }
    .reasoning-content {
        margin-top: 1rem;
        color: #CBD5E1;
        line-height: 1.7;
        font-size: 0.95rem;
        border-top: 1px solid rgba(0, 243, 255, 0.15);
        padding-top: 1rem;
    }

    /* Chat Bubbles & Prompt Chips */
    .user-chat-bubble {
        background: rgba(0, 243, 255, 0.08) !important;
        border: 1px solid rgba(0, 243, 255, 0.3) !important;
        border-radius: 16px 16px 2px 16px;
        padding: 1rem 1.25rem;
        color: #F8FAFC;
        margin-bottom: 1rem;
        margin-left: 2rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
    }
    .ai-chat-bubble {
        background: rgba(13, 10, 32, 0.85);
        border: 1px solid rgba(192, 132, 252, 0.3);
        border-radius: 16px 16px 16px 2px;
        padding: 1.25rem;
        margin-bottom: 1.5rem;
        backdrop-filter: blur(15px);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }
    .prompt-chip-btn {
        background: rgba(13, 10, 32, 0.8) !important;
        border: 1px solid rgba(0, 243, 255, 0.3) !important;
        color: #F1F5F9 !important;
        border-radius: 20px !important;
        transition: all 0.2s ease !important;
    }
    .prompt-chip-btn:hover {
        background: rgba(0, 243, 255, 0.2) !important;
        border-color: #00F3FF !important;
        transform: translateY(-2px);
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


def render_hero_banner():
    """Renders the animated title and hero banner on the main page."""
    html_banner = """
    <div class="hero-container">
        <div class="hero-silhouettes">
            <span>🏛️</span>
            <span>⚖️</span>
            <span>🦁</span>
        </div>
        <div class="hero-title-container">
            <h1 class="hero-title">
                ⚖️ NYAYASATHI AI LEGAL CONSULTANT
            </h1>
            <p class="hero-subtitle">
                "Explore the Constitution. Understand Your Rights. Learn Indian Law."
            </p>
        </div>
    </div>
    """
    st.markdown(html_banner, unsafe_allow_html=True)


def render_footer():
    """Renders the sticky application footer."""
    html_footer = """
    <div class="sticky-footer">
        <div class="footer-badge" style="color: #00F3FF; font-weight: 600;">Indian Legal AI Assistant • NyayaSathi v1.1.0</div>
        <div style="margin-top: 0.2rem;">Built with Python • Streamlit • Groq LLM • Pydantic</div>
        <div style="margin-top: 0.4rem; color: #64748B; font-size: 0.8rem;">
            ⚠️ General Legal Information Only. Not a Substitute for Professional Legal Advice.
        </div>
    </div>
    """
    st.markdown(html_footer, unsafe_allow_html=True)