"""Configuration module for AI Legal Consultant.

Loads environment variables, defines application constants, UI theme tokens,
Groq model parameters, and default legal disclaimers.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Base Paths
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
SAMPLE_DOCS_DIR = BASE_DIR / "sample_documents"
LOGO_PATH = ASSETS_DIR / "logo.png"

# App Metadata
APP_NAME = "Indian Legal AI Assistant"
APP_TAGLINE = "Explore the Constitution. Understand Your Rights. Learn Indian Law."
APP_VERSION = "1.2.0"

# Legal Disclaimer
DEFAULT_DISCLAIMER = (
    "This application provides general legal information for educational and research purposes only under Indian law. "
    "It is not formal legal advice or an attorney-client relationship. Consult a qualified advocate for advice tailored to your jurisdiction."
)

# Groq API Configuration
_env_key = os.getenv("GROQ_API_KEY", "").strip()

if not _env_key or _env_key == "your_groq_api_key_here":
    api_txt_path = Path("C:/Users/SIC/Desktop/API.txt")
    if api_txt_path.exists():
        try:
            _env_key = api_txt_path.read_text(encoding="utf-8").strip()
        except Exception:
            pass

GROQ_API_KEY = _env_key
DEFAULT_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

AVAILABLE_MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-70b-versatile",
    "llama3-70b-8192",
    "mixtral-8x7b-32768"
]

# UI Color Tokens
COLORS = {
    "background": "#0B132B",          # Deep Navy
    "card_bg": "rgba(11, 19, 43, 0.7)", # Deep Navy translucent
    "accent_gold": "#D4AF37",         # Premium Gold
    "accent_saffron": "#FF9933",      # Indian Saffron
    "accent_emerald": "#138808",      # Indian Green / Emerald
    "accent_brown": "#5C4033",        # Dark Brown
    "ivory_parchment": "#FDF5E6",     # Parchment background
    "text_primary": "#F8FAFC",
    "text_secondary": "#94A3B8",
}
