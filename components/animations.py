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
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    /* Global Typography & Reset */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    h1, h2, h3, .hero-title {
        font-family: 'Cinzel', serif; /* Elegant, classic serif for headings */
    }

    /* Main Container Background - Deep Navy */
    .stApp {
        background-color: #0B132B;
        background-image: 
            radial-gradient(circle at 15% 50%, rgba(255, 153, 51, 0.05) 0%, transparent 40%),
            radial-gradient(circle at 85% 30%, rgba(19, 136, 8, 0.05) 0%, transparent 40%),
            radial-gradient(circle at 50% 80%, rgba(212, 175, 55, 0.08) 0%, transparent 50%);
        background-attachment: fixed;
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
        0%, 100% { box-shadow: 0 0 15px rgba(212, 175, 55, 0.2); }
        50% { box-shadow: 0 0 30px rgba(212, 175, 55, 0.5); }
    }

    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    
    @keyframes particleDrift {
        0% { transform: translateY(0) translateX(0); opacity: 0.3; }
        50% { transform: translateY(-20px) translateX(10px); opacity: 0.7; }
        100% { transform: translateY(-40px) translateX(-10px); opacity: 0; }
    }

    /* Animated Title & Hero Header */
    .hero-container {
        text-align: center;
        padding: 4rem 1rem 3rem 1rem;
        position: relative;
        overflow: hidden;
        border-radius: 20px;
        background: linear-gradient(180deg, rgba(11, 19, 43, 0) 0%, rgba(212, 175, 55, 0.05) 100%);
        border-bottom: 1px solid rgba(212, 175, 55, 0.1);
        margin-bottom: 2rem;
        animation: fadeIn 1s ease-out;
    }
    
    /* Simulate silhouettes */
    .hero-silhouettes {
        font-size: 8rem;
        opacity: 0.05;
        position: absolute;
        bottom: -20px;
        left: 0;
        width: 100%;
        display: flex;
        justify-content: space-around;
        pointer-events: none;
        z-index: 0;
    }

    .hero-title-container {
        position: relative;
        z-index: 1;
        animation: slideUp 0.8s ease-out;
    }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #FF9933 0%, #D4AF37 50%, #138808 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 0.02em;
        margin-bottom: 0.5rem;
        display: inline-flex;
        align-items: center;
        gap: 0.75rem;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        color: #E2E8F0;
        max-width: 680px;
        margin: 0 auto;
        line-height: 1.6;
        font-weight: 300;
        font-family: 'Cinzel', serif;
    }

    /* Glassmorphism Card Style */
    .glass-card {
        background: rgba(11, 19, 43, 0.6);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(212, 175, 55, 0.15); /* Gold tinted border */
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.5);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        animation: slideUp 0.5s ease-out backwards;
    }

    .glass-card:hover {
        transform: translateY(-5px);
        border-color: rgba(212, 175, 55, 0.4);
        box-shadow: 0 20px 40px -10px rgba(212, 175, 55, 0.15);
    }
    
    /* Parchment Card variant */
    .parchment-card {
        background: #FDF5E6; /* Ivory Parchment */
        color: #3E2723; /* Dark Brown Text */
        border: 1px solid #D4AF37;
        box-shadow: inset 0 0 50px rgba(92, 64, 51, 0.1), 0 10px 20px rgba(0,0,0,0.3);
    }
    .parchment-card .card-header {
        color: #5C4033;
        font-family: 'Cinzel', serif;
    }
    .parchment-card p, .parchment-card li {
        color: #4E342E;
    }

    /* Response Section Cards with Theme Borders */
    .card-legal-topic {
        border-left: 5px solid #D4AF37 !important; /* Gold */
    }

    .card-summary {
        border-left: 5px solid #FF9933 !important; /* Saffron */
    }

    .card-important-points {
        border-left: 5px solid #138808 !important; /* Emerald */
    }
    
    .card-articles {
        border-left: 5px solid #38BDF8 !important;
    }
    
    .card-acts {
        border-left: 5px solid #8B5CF6 !important;
    }

    .card-considerations {
        border-left: 5px solid #F59E0B !important;
    }

    .card-next-steps {
        border-left: 5px solid #10B981 !important;
    }

    .card-disclaimer {
        border-left: 5px solid #EF4444 !important;
        background: rgba(239, 68, 68, 0.05) !important;
    }

    /* Card Section Titles */
    .card-header {
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.6rem;
        color: #FDF5E6; /* Ivory text */
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
        background-color: rgba(11, 19, 43, 0.8) !important;
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        border-radius: 12px !important;
        color: #FDF5E6 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }

    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #D4AF37 !important;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.3) !important;
    }

    /* Buttons */
    .stButton button {
        background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%) !important;
        color: #0B132B !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.6rem 1.8rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.02em !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3) !important;
        transition: all 0.3s ease !important;
    }

    .stButton button:hover {
        transform: translateY(-2px) scale(1.02) !important;
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.5) !important;
        background: linear-gradient(135deg, #FF9933 0%, #D4AF37 100%) !important;
        color: #0B132B !important;
    }

    /* Loading Shimmer Progress Bar */
    .shimmer-progress {
        height: 6px;
        width: 100%;
        background: linear-gradient(90deg, rgba(212, 175, 55, 0.1) 0%, rgba(255, 153, 51, 0.8) 50%, rgba(212, 175, 55, 0.1) 100%);
        background-size: 200% 100%;
        animation: shimmer 1.5s infinite linear;
        border-radius: 4px;
        margin: 1rem 0;
    }

    /* Translucent Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(6, 11, 25, 0.95) !important; /* Very dark navy */
        border-right: 1px solid rgba(212, 175, 55, 0.1) !important;
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
        background-color: rgba(212, 175, 55, 0.3);
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
        background-color: #0B132B;
        border: 4px solid #D4AF37;
        top: 15px;
        border-radius: 50%;
        z-index: 1;
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
        padding: 1.5rem 0 1rem 0;
        color: #64748B;
        font-size: 0.88rem;
        border-top: 1px solid rgba(212, 175, 55, 0.1);
        margin-top: 3rem;
    }

    .footer-badge {
        display: inline-block;
        background: rgba(11, 19, 43, 0.8);
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        color: #D4AF37;
        font-size: 0.8rem;
        margin-bottom: 0.5rem;
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
                ⚖️ Indian Legal AI Consultant
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
        <div class="footer-badge">Indian Legal AI Assistant • v1.1.0</div>
        <div>Built with Python • Streamlit • LLM • Pydantic</div>
        <div style="margin-top: 0.4rem; color: #475569; font-size: 0.8rem;">
            ⚠️ General Legal Information Only. Not a Substitute for Professional Legal Advice.
        </div>
    </div>
    """
    st.markdown(html_footer, unsafe_allow_html=True)
