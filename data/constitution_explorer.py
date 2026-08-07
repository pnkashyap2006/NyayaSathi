"""Constitution Explorer Data Module for NyayaSathi.

Provides structured data for major constitutional topics, landmark articles,
statistics, interactive facts, and AI assistant query starters.
"""

from typing import List, Dict, Any

CONSTITUTION_STATS = [
    {"label": "Current Articles", "value": "448+", "sub": "Originally 395"},
    {"label": "Parts", "value": "25", "sub": "Originally 22"},
    {"label": "Schedules", "value": "12", "sub": "Originally 8"},
    {"label": "Amendments", "value": "106", "sub": "1951 – 2024"},
    {"label": "World Rank", "value": "#1 Longest", "sub": "Written Constitution"},
    {"label": "Official Languages", "value": "22", "sub": "Eighth Schedule"}
]

MAJOR_CONSTITUTIONAL_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "preamble",
        "title": "Preamble",
        "icon": "📜",
        "articles": "Introductory Statement",
        "desc": "The key to the minds of the framers. Declares India a Sovereign, Socialist, Secular, Democratic Republic securing Justice, Liberty, Equality, and Fraternity.",
        "nav_target": "preamble"
    },
    {
        "id": "rights",
        "title": "Fundamental Rights",
        "icon": "🛡️",
        "articles": "Part III (Articles 12–35)",
        "desc": "Justiciable constitutional guarantees protecting equality, freedom, religion, educational rights, and remedies against state overreach.",
        "nav_target": "rights"
    },
    {
        "id": "duties",
        "title": "Fundamental Duties",
        "icon": "⚖️",
        "articles": "Part IVA (Article 51A)",
        "desc": "Moral obligations of every citizen to respect the National Flag, protect the environment, renounce derogation of women, and foster scientific temper.",
        "nav_target": "duties"
    },
    {
        "id": "dpsp",
        "title": "Directive Principles (DPSP)",
        "icon": "🏛️",
        "articles": "Part IV (Articles 36–51)",
        "desc": "Non-justiciable guidelines for the State to establish social and economic democracy, welfare governance, and equal opportunity.",
        "nav_target": None
    },
    {
        "id": "union_govt",
        "title": "Union Government",
        "icon": "👑",
        "articles": "Part V (Articles 52–151)",
        "desc": "Structures the Executive, Parliament, Federal Judiciary, and Comptroller and Auditor General (CAG) of the Union.",
        "nav_target": None
    },
    {
        "id": "state_govt",
        "title": "State Government",
        "icon": "🏢",
        "articles": "Part VI (Articles 152–237)",
        "desc": "Defines the executive, legislative, and judicial structure across Indian States.",
        "nav_target": None
    },
    {
        "id": "parliament",
        "title": "Parliament of India",
        "icon": "🏛️",
        "articles": "Articles 79–122",
        "desc": "Bicameral legislature comprising the President, Council of States (Rajya Sabha), and House of the People (Lok Sabha).",
        "nav_target": None
    },
    {
        "id": "judiciary",
        "title": "Indian Judiciary",
        "icon": "⚖️",
        "articles": "Part V & VI (Supreme Court & High Courts)",
        "desc": "Single integrated judicial system with the Supreme Court as guardian of the Constitution and supreme appellate authority.",
        "nav_target": "judiciary"
    },
    {
        "id": "president",
        "title": "President of India",
        "icon": "👤",
        "articles": "Articles 52–62, 72, 123",
        "desc": "Constitutional Head of State and Supreme Commander of the Armed Forces holding executive, legislative, and pardoning powers.",
        "nav_target": None
    },
    {
        "id": "prime_minister",
        "title": "Prime Minister & Council",
        "icon": "💼",
        "articles": "Articles 74–75",
        "desc": "Real executive authority of the Union government leading the Cabinet and aiding/advising the President.",
        "nav_target": None
    },
    {
        "id": "governor",
        "title": "Governor of a State",
        "icon": "🎖️",
        "articles": "Articles 153–162",
        "desc": "Constitutional head of the State executive appointed by the President, bridging Union-State federal administration.",
        "nav_target": None
    },
    {
        "id": "constitutional_bodies",
        "title": "Constitutional Bodies",
        "icon": "🌐",
        "articles": "Articles 280, 315, 324, 148",
        "desc": "Independent bodies created directly by the Constitution: Election Commission (324), Finance Commission (280), UPSC (315), CAG (148).",
        "nav_target": None
    },
    {
        "id": "emergency",
        "title": "Emergency Provisions",
        "icon": "🚨",
        "articles": "Part XVIII (Articles 352–360)",
        "desc": "Special extraordinary powers: National Emergency (352), State Emergency / President's Rule (356), Financial Emergency (360).",
        "nav_target": None
    },
    {
        "id": "amendment",
        "title": "Amendment Procedure",
        "icon": "✍️",
        "articles": "Part XX (Article 368)",
        "desc": "Power of Parliament to amend the Constitution by special majority, subject to the inviolable 'Basic Structure' doctrine.",
        "nav_target": None
    },
    {
        "id": "elections",
        "title": "Elections & Suffrage",
        "icon": "🗳️",
        "articles": "Part XV (Articles 324–329)",
        "desc": "Guarantees Universal Adult Suffrage (18+ voting rights) and free & fair elections conducted by the Election Commission.",
        "nav_target": None
    },
    {
        "id": "local_govt",
        "title": "Local Self-Government",
        "icon": "🏡",
        "articles": "Part IX & IXA (Articles 243–243ZG)",
        "desc": "Grassroots democracy established by 73rd & 74th Amendments introducing Panchayati Raj Institutions and Urban Municipalities.",
        "nav_target": None
    }
]

POPULAR_ARTICLES = [
    {
        "article": "Article 14",
        "title": "Equality Before Law",
        "summary": "State cannot deny equality before law or equal protection of laws to any person within India.",
        "significance": "Foundation of anti-arbitrariness and rule of law."
    },
    {
        "article": "Article 19",
        "title": "Six Fundamental Freedoms",
        "summary": "Guarantees freedom of speech, assembly, association, movement, residence, and profession.",
        "significance": "Core of civil liberties, subject to reasonable restrictions."
    },
    {
        "article": "Article 21",
        "title": "Right to Life & Liberty",
        "summary": "No person shall be deprived of life or personal liberty except by procedure established by law.",
        "significance": "Interpreted to include privacy, clean environment, legal aid, and dignity."
    },
    {
        "article": "Article 32",
        "title": "Supreme Court Writs",
        "summary": "Right to approach Supreme Court directly for enforcement of Fundamental Rights.",
        "significance": "Called the 'Heart and Soul' of the Constitution by Dr. B.R. Ambedkar."
    },
    {
        "article": "Article 226",
        "title": "High Court Writs",
        "summary": "Empowers High Courts to issue writs for fundamental rights AND any other legal rights.",
        "significance": "Wider in scope than Article 32."
    },
    {
        "article": "Article 368",
        "title": "Constitutional Amendments",
        "summary": "Procedure and parliamentary power to amend the Constitution.",
        "significance": "Subject to the Basic Structure Doctrine (Kesavananda Bharati case)."
    }
]

CONSTITUTIONAL_FACTS = [
    "Dr. B. R. Ambedkar served as the Chairman of the 7-member Drafting Committee and is recognized as the Chief Architect of the Constitution.",
    "Article 32 was declared by Dr. B. R. Ambedkar as 'the very soul of the Constitution and the very heart of it'.",
    "India has the longest written constitution of any sovereign nation in the world.",
    "The original Constitution was handwritten by Prem Behari Narain Raizada in beautiful italic calligraphy.",
    "Each page of the original manuscript was decorated by artists from Visva-Bharati, Santiniketan, including Nandalal Bose.",
    "The original handwritten copies are preserved in helium-filled cases inside the Parliament Library in New Delhi.",
    "The Constituent Assembly took exactly 2 years, 11 months, and 18 days to draft the Constitution."
]

ASK_CONSTITUTION_STARTERS = [
    "Explain Article 21 and Right to Privacy",
    "What are Directive Principles of State Policy?",
    "How is the Constitution amended under Article 368?",
    "What powers does the President of India hold?",
    "What is Article 370 and its current legal status?",
    "Difference between Fundamental Rights and Fundamental Duties"
]
