"""Legal Safety & Emergency Detection Engine for NyayaSathi.

Detects urgent legal situations (cyber crime, domestic violence, child abuse, human trafficking,
sexual assault, arrest/police action, physical danger) and provides official Government of India emergency helpline banners.
Also enforces strict ethical safety filters refusing requests that facilitate illegal activity.
"""

import re
from typing import Dict, Any, Optional

# Official Emergency Helpline Contacts (Government of India)
EMERGENCY_HELPLINES = {
    "cyber_crime": {
        "title": "🚨 CYBERCRIME EMERGENCY DETECTED",
        "message": "If you are experiencing active financial fraud, online scam, or cyber harassment, immediately report it to the National Cyber Crime Reporting Portal or call the toll-free helpline.",
        "helpline": "1930",
        "website": "https://cybercrime.gov.in"
    },
    "women_safety": {
        "title": "🚨 DOMESTIC VIOLENCE / WOMEN HELPLINE",
        "message": "If you or someone you know is facing domestic abuse, sexual harassment, or violence, please reach out to the official National Commission for Women helpline immediately.",
        "helpline": "1091 / 7827170170",
        "website": "http://ncw.nic.in"
    },
    "national_emergency": {
        "title": "🚨 IMMEDIATE POLICE / PHYSICAL DANGER / ARREST EMERGENCY",
        "message": "If you are in immediate physical danger, facing violent assault, subject to illegal arrest, or human trafficking, contact Emergency Response Services instantly.",
        "helpline": "112 (All India Emergency)",
        "website": "https://erss.in"
    },
    "child_protection": {
        "title": "🚨 CHILD ABUSE & PROTECTION HELPLINE",
        "message": "For urgent child abuse, child labor, sexual exploitation, or child distress situations, contact Childline India immediately.",
        "helpline": "1098 (Childline)",
        "website": "https://www.childlineindia.org"
    }
}


def evaluate_emergency(query: str) -> Optional[Dict[str, str]]:
    """Scans query for emergency keywords and returns official helpline details if matched.

    Args:
        query: User input query string.

    Returns:
        Optional Dict with emergency helpline metadata, or None if no emergency detected.
    """
    if not query:
        return None

    lower_query = query.lower()

    # 1. Cyber Crime / Financial Fraud in progress
    cyber_keywords = [
        "money stolen", "otp scam", "account hacked", "bank fraud", "phishing", "scam",
        "unauthorized transaction", "cyber fraud", "scammed online", "blackmail online", "nude photo leaked", "otp"
    ]
    if any(kw in lower_query for kw in cyber_keywords) or ("money" in lower_query and "stolen" in lower_query):
        return EMERGENCY_HELPLINES["cyber_crime"]

    # 2. Women Safety, Domestic Abuse, Sexual Assault, POSH
    women_keywords = [
        "domestic violence", "husband beating", "in-laws harassment", "dowry torture",
        "sexual assault", "molestation", "stalking me", "rape", "posh harassment", "abuse at home"
    ]
    if any(kw in lower_query for kw in women_keywords):
        return EMERGENCY_HELPLINES["women_safety"]

    # 3. Physical Danger, Human Trafficking, Arrest, Police Action
    danger_keywords = [
        "being beaten", "physical attack", "life threat", "kidnapped", "human trafficking",
        "trafficked", "unlawful detention", "police beating me", "police arresting me now", "held hostage", "imminent arrest"
    ]
    if any(kw in lower_query for kw in danger_keywords):
        return EMERGENCY_HELPLINES["national_emergency"]

    # 4. Child Abuse & Distress
    child_keywords = ["child abuse", "child labor", "minor abuse", "child exploitation", "pedophile"]
    if any(kw in lower_query for kw in child_keywords):
        return EMERGENCY_HELPLINES["child_protection"]

    return None


def evaluate_safety_refusal(query: str) -> Optional[str]:
    """Checks if the query requests instructions on committing crimes or illegal acts.

    Args:
        query: User input query.

    Returns:
        Refusal message string explaining why request cannot be fulfilled if illegal activity detected, or None.
    """
    if not query:
        return None

    lower_query = query.lower()
    illegal_intent_patterns = [
        "how to forge", "how to hack a bank", "how to evade taxes illegally",
        "how to fake a deed", "how to bribe a police officer", "how to commit fraud without getting caught",
        "how to launder money", "how to fabricate evidence", "how to bypass law"
    ]

    for pattern in illegal_intent_patterns:
        if pattern in lower_query:
            return (
                "🛡️ Safety Refusal Notice: NyayaSathi strictly adheres to ethical standards and Indian law. "
                "We cannot assist with, facilitate, or provide instructions on committing illegal activities, "
                "forgery, bribery, tax evasion, or law-breaking. If you are seeking legitimate legal remedies, "
                "please rephrase your query or consult a licensed advocate."
            )

    return None
