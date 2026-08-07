"""Comprehensive Constitutional Knowledge Base for Fundamental Rights & Duties.

Provides in-depth educational data for Part III (Fundamental Rights, Articles 12-35)
and Part IVA (Fundamental Duties, Article 51A), includingConstituent Assembly rationale,
article-by-article breakdowns, real-life scenarios, reasonable restrictions, misconceptions,
landmark Supreme Court judgments, quick facts, and FAQs.
"""

from typing import List, Dict, Any

PREAMBLE_TEXT = [
    "WE, THE PEOPLE OF INDIA,",
    "having solemnly resolved to constitute India into a",
    "SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC",
    "and to secure to all its citizens:",
    "JUSTICE, social, economic and political;",
    "LIBERTY of thought, expression, belief, faith and worship;",
    "EQUALITY of status and of opportunity;",
    "and to promote among them all",
    "FRATERNITY assuring the dignity of the individual",
    "and the unity and integrity of the Nation;",
    "IN OUR CONSTITUENT ASSEMBLY this twenty-sixth day of November, 1949,",
    "do HEREBY ADOPT, ENACT AND GIVE TO OURSELVES THIS CONSTITUTION."
]

EXPANDED_FUNDAMENTAL_RIGHTS: List[Dict[str, Any]] = [
    {
        "id": "equality",
        "title": "Right to Equality",
        "articles_range": "Articles 14 – 18",
        "icon": "⚖️",
        "overview": (
            "The Right to Equality is the cornerstone of Indian democracy. Formulated by the Constituent Assembly under the guidance "
            "of Dr. B.R. Ambedkar, its primary purpose is to eradicate centuries-old social hierarchies, feudal titles, caste-based discrimination, "
            "and untouchability. It establishes that the State cannot show arbitrary favoritism to any individual or class, ensuring that "
            "every citizen stands equal before the law with dignity and equal opportunity."
        ),
        "simple_meaning": (
            "No matter how rich, powerful, or famous a person is, the law applies to everyone equally. "
            "Government offices, schools, public parks, and police must treat all citizens fairly without discriminating based on religion, caste, gender, or birthplace."
        ),
        "why_it_matters": (
            "Without equal treatment, democracy becomes an oligarchy where the privileged rule over the marginalized. "
            "This right guarantees that a daily wage worker and a multi-millionaire have the exact same rights when standing before an Indian court."
        ),
        "articles_detail": [
            {
                "article": "Article 14",
                "title": "Equality Before Law & Equal Protection of Laws",
                "meaning": "The State shall not deny to any person equality before the law or equal protection of the laws within India.",
                "purpose": "Prevents arbitrary state action. 'Equality before law' (British concept) means nobody is above the law. 'Equal protection' (American concept) means equals must be treated equally.",
                "example": "If a government officer and a citizen commit the same traffic offense, both face the exact same penalty."
            },
            {
                "article": "Article 15",
                "title": "Prohibition of Discrimination",
                "meaning": "Prohibits discrimination against any citizen on grounds ONLY of religion, race, caste, sex, or place of birth.",
                "purpose": "Ensures equal access to shops, public restaurants, hotels, wells, tanks, and roads. Also empowers the State to make special provisions for women, children, SCs, STs, and EWS.",
                "example": "A public restaurant cannot deny entry to a person based on their caste or attire."
            },
            {
                "article": "Article 16",
                "title": "Equality of Opportunity in Public Employment",
                "meaning": "Guarantees equal opportunity for all citizens in matters of government employment or appointment.",
                "purpose": "Prevents nepotism in civil services while allowing affirmative action (reservations) to uplift historically underrepresented communities.",
                "example": "Government job notifications must be publicly advertised so all eligible candidates can apply."
            },
            {
                "article": "Article 17",
                "title": "Abolition of Untouchability",
                "meaning": "Untouchability is abolished and its practice in any form is forbidden and punishable by law.",
                "purpose": "An absolute human right designed to completely wipe out the historical social stigma of untouchability.",
                "example": "Denying someone entry to a village well or temple based on caste is a severe criminal offense under the Protection of Civil Rights Act, 1955."
            },
            {
                "article": "Article 18",
                "title": "Abolition of Titles",
                "meaning": "Abolishes feudal and colonial titles like 'Rai Bahadur', 'Sir', or 'Knight'.",
                "purpose": "Prevents the creation of artificial noble classes in a republic. National awards like Bharat Ratna or Padma Vibhushan are civilian honors, not noble titles.",
                "example": "A citizen awarded Padma Shri cannot legally prefix 'Padma Shri' as a noble title to their name."
            }
        ],
        "real_life_examples": [
            "Employment: Government job exams must evaluate candidates strictly on merit and statutory reservation quotas without bribery.",
            "Education: Public universities cannot deny admission to students based on their state of origin or religion.",
            "Public Spaces: Municipal parks, public libraries, and hospitals must remain accessible to all citizens equally.",
            "Police Action: Police cannot grant special immunity to wealthy individuals while arresting poorer suspects for the same offense."
        ],
        "limitations": [
            "Reasonable Classification: Article 14 allows the State to classify people for valid policy reasons (e.g. taxing higher income earners at higher rates).",
            "Affirmative Action: Articles 15(3), 15(4), and 16(4) permit special provisions and reservations for women, children, SCs, STs, OBCs, and EWS.",
            "Foreign Dignitaries: Foreign sovereigns, diplomats, and the President/Governors enjoy constitutional immunities during their term (Article 361)."
        ],
        "common_misconceptions": [
            {
                "myth": "Equality means everyone must be treated exactly the same in every single scenario.",
                "truth": "Equality means 'equals must be treated equally'. Treating a disabled person and an able-bodied person identically without accommodations is actually inequality."
            },
            {
                "myth": "Reservations in public jobs violate Article 14.",
                "truth": "The Supreme Court has ruled that affirmative action is a tool to achieve real structural equality for historically marginalized groups."
            }
        ],
        "landmark_judgments": [
            {
                "case": "Indra Sawhney v. Union of India (1992)",
                "ruling": "Upheld 27% reservation for Other Backward Classes (OBCs), capped total reservations at 50%, and introduced the 'creamy layer' principle."
            },
            {
                "case": "Navtej Singh Johar v. Union of India (2018)",
                "ruling": "Decriminalized Section 377 IPC, ruling that discrimination based on sexual orientation violates Articles 14, 15, 19, and 21."
            }
        ],
        "quick_facts": [
            "Article 17 is one of the few absolute fundamental rights with no constitutional exceptions.",
            "India's Preamble explicitly lists 'Equality of status and of opportunity' as a primary objective."
        ],
        "faqs": [
            {
                "q": "Can a private company discriminate in hiring?",
                "a": "Fundamental Rights primarily bind the State. However, private discrimination is governed by labor laws, POSH Act, and statutory regulations."
            },
            {
                "q": "Are Padma awards considered titles under Article 18?",
                "a": "No, the Supreme Court ruled in Balaji Raghavan (1996) that National Awards are civilian honors recognizing merit, not titles of nobility."
            }
        ],
        "related_provisions": ["Article 19", "Article 21", "Directive Principles: Article 38 & 39"]
    },
    {
        "id": "freedom",
        "title": "Right to Freedom",
        "articles_range": "Articles 19 – 22",
        "icon": "🕊️",
        "overview": (
            "The Right to Freedom embodies the vital democratic liberties of every individual. "
            "Included by the Constituent Assembly to ensure that independent India would never suffer under authoritarian censorship, "
            "this right guarantees freedom of speech, assembly, association, movement, trade, personal liberty, and safeguards against arbitrary arrest."
        ),
        "simple_meaning": (
            "You have the right to express your views, travel anywhere in India, practice any profession, "
            "and live with dignity without fear of illegal police detention."
        ),
        "why_it_matters": (
            "Freedom of thought and movement allows citizens to hold their government accountable, innovate, build businesses, "
            "and live free from fear of unlawful arrest."
        ),
        "articles_detail": [
            {
                "article": "Article 19",
                "title": "Protection of 6 Fundamental Freedoms",
                "meaning": "Guarantees 6 basic freedoms to Indian citizens: (a) Speech & Expression, (b) Peaceful Assembly, (c) Associations/Unions, (d) Movement across India, (e) Residence anywhere in India, (g) Trade or Profession.",
                "purpose": "Provides the essential liberties required for active participation in a vibrant democratic society.",
                "example": "Citizens organizing a peaceful rally or journalists publishing investigative news stories."
            },
            {
                "article": "Article 20",
                "title": "Protection in Respect of Conviction for Offenses",
                "meaning": "Safeguards accused persons against: 1. Ex-post facto laws (retrospective punishment), 2. Double Jeopardy (punished twice for same offense), 3. Self-incrimination (forced to testify against oneself).",
                "purpose": "Prevents the State from misusing criminal law to target political opponents.",
                "example": "You cannot be convicted today under a law passed tomorrow for an action done yesterday."
            },
            {
                "article": "Article 21",
                "title": "Protection of Life and Personal Liberty",
                "meaning": "No person shall be deprived of life or personal liberty except according to procedure established by law.",
                "purpose": "Expands to include Right to Privacy, Right to Clean Environment, Right to Education, and Right to Live with Dignity.",
                "example": "A person cannot be locked up or executed without a fair judicial trial under valid law."
            },
            {
                "article": "Article 21A",
                "title": "Right to Free & Compulsory Education",
                "meaning": "State shall provide free and compulsory education to all children aged 6 to 14 years.",
                "purpose": "Added by the 86th Amendment Act (2002) to eradicate illiteracy and empower future generations.",
                "example": "Every child aged 6-14 has a legally enforceable right to study in a nearby government school without tuition fees."
            },
            {
                "article": "Article 22",
                "title": "Protection Against Arrest and Detention",
                "meaning": "Guarantees that an arrested person must be: 1. Informed of grounds of arrest, 2. Allowed to consult an advocate, 3. Produced before a Magistrate within 24 hours.",
                "purpose": "Curbs illegal police custody and unauthorized detention.",
                "example": "Police arresting a suspect must produce them before a Judicial Magistrate within 24 hours excluding travel time."
            }
        ],
        "real_life_examples": [
            "Freedom of Expression: Writing blog posts, creating art, or criticizing government policies peacefully.",
            "Freedom of Movement: Moving from Kerala to Delhi for higher studies or taking a job in Maharashtra.",
            "Right to Privacy: Protecting your personal biometric data and telephone conversations from unauthorized government wiretapping.",
            "Police Arrest: Informing your family and lawyer immediately upon being taken into police custody."
        ],
        "limitations": [
            "Reasonable Restrictions under Art 19(2): Speech can be restricted for Sovereignty of India, Security of State, Public Order, Decency, Contempt of Court, or Defamation.",
            "Preventive Detention: Under Article 22, suspects can be detained up to 3 months without trial under special national security laws.",
            "Emergency Provisions: Article 19 freedoms can be suspended during a National Emergency declared under Article 352."
        ],
        "common_misconceptions": [
            {
                "myth": "Freedom of speech means I can post hate speech or incite violence online without consequences.",
                "truth": "Article 19(2) allows the State to impose reasonable restrictions to preserve public order and prevent incitement to offenses."
            },
            {
                "myth": "Article 21 can be suspended during a Presidential Emergency.",
                "truth": "The 44th Amendment (1978) established that Articles 20 and 21 CANNOT be suspended even during a National Emergency."
            }
        ],
        "landmark_judgments": [
            {
                "case": "Maneka Gandhi v. Union of India (1978)",
                "ruling": "Ruled that 'procedure established by law' under Article 21 must be just, fair, and reasonable—not arbitrary or oppressive."
            },
            {
                "case": "K.S. Puttaswamy v. Union of India (2017)",
                "ruling": "Unanimously declared the Right to Privacy as a fundamental right protected under Article 21."
            }
        ],
        "quick_facts": [
            "Dr. B.R. Ambedkar called Article 21 the foundational heart of fundamental rights.",
            "Articles 20 and 21 are the only two rights that remain active during a National Emergency."
        ],
        "faqs": [
            {
                "q": "What happens if police fail to produce an arrested person within 24 hours?",
                "a": "Detention beyond 24 hours without a magistrate's order is illegal. A Habeas Corpus petition can be filed immediately."
            },
            {
                "q": "Does Article 19 apply to non-citizens?",
                "a": "No, Article 19 freedoms are available ONLY to Indian citizens. However, Article 21 applies to all persons."
            }
        ],
        "related_provisions": ["Article 14", "Article 32", "Article 226"]
    },
    {
        "id": "exploitation",
        "title": "Right against Exploitation",
        "articles_range": "Articles 23 – 24",
        "icon": "🛡️",
        "overview": (
            "The Right against Exploitation guarantees freedom from modern human slavery, debt bondage, forced labor, and child labor. "
            "The framers of the Constitution recognized that formal political democracy is meaningless if vulnerable women, children, "
            "and impoverished workers remain trapped in economic servitude."
        ),
        "simple_meaning": (
            "Nobody can force you to work without wages, buy or sell human beings, or employ children under 14 in factories or hazardous jobs."
        ),
        "why_it_matters": (
            "It protects vulnerable children and workers from human trafficking, bonded labor, and hazardous working conditions."
        ),
        "articles_detail": [
            {
                "article": "Article 23",
                "title": "Prohibition of Traffic in Human Beings & Forced Labor",
                "meaning": "Prohibits human trafficking, 'begar' (unpaid forced labor), and similar forms of forced labor. Contravention is a criminal offense.",
                "purpose": "Abolishes feudal forced labor and human trafficking. Exception: State can impose compulsory service for public purposes (military conscription) without discrimination.",
                "example": "Rescuing brick kiln workers trapped in generational debt bondage where wages were withheld."
            },
            {
                "article": "Article 24",
                "title": "Prohibition of Employment of Children in Hazardous Jobs",
                "meaning": "No child below the age of 14 years shall be employed to work in any factory, mine, or hazardous employment.",
                "purpose": "Protects children's health, safety, and right to education.",
                "example": "Inspecting carpet manufacturing units or match factories to ensure children under 14 are not employed."
            }
        ],
        "real_life_examples": [
            "Child Labor Enforcement: Raids conducted by labor inspectors to rescue minors working in firecracker units.",
            "Bonded Labor Rehabilitation: Government initiatives releasing agricultural workers trapped in illegal hereditary debt servitude.",
            "Anti-Human Trafficking: Police operations shutting down forced prostitution and commercial human trafficking networks."
        ],
        "limitations": [
            "Compulsory State Service: Under Article 23(2), the State can mandate compulsory public service (e.g. disaster management or military duty) provided it does not discriminate on religion, race, caste, or class."
        ],
        "common_misconceptions": [
            {
                "myth": "Paying someone very low wages below minimum wage is legal if they consented voluntarily.",
                "truth": "The Supreme Court in PUDR (Asiad Workers case) ruled that paying less than statutory minimum wage due to economic helplessness constitutes 'forced labor' under Article 23."
            }
        ],
        "landmark_judgments": [
            {
                "case": "People's Union for Democratic Rights (PUDR) v. Union of India (1982)",
                "ruling": "Ruled that 'forced labor' under Article 23 includes labor undertaken due to economic compulsion where wages paid are below minimum wage."
            },
            {
                "case": "M.C. Mehta v. State of Tamil Nadu (1996)",
                "ruling": "Issued comprehensive directions regarding child labor in Sivakasi match factories and mandated a Child Labour Rehabilitation Welfare Fund."
            }
        ],
        "quick_facts": [
            "'Begar' is a traditional practice where laborers were forced to work for landholders without any remuneration.",
            "Child Labour (Prohibition and Regulation) Amendment Act, 2016 completely prohibits employment of children below 14 years in all occupations."
        ],
        "faqs": [
            {
                "q": "Can a 15-year-old work legally in India?",
                "a": "Yes, adolescents (ages 14-18) can work in non-hazardous occupations, but cannot be employed in hazardous industries like mines or explosives."
            }
        ],
        "related_provisions": ["Article 21A", "Directive Principles: Article 39(e) & (f)"]
    },
    {
        "id": "religion",
        "title": "Right to Freedom of Religion",
        "articles_range": "Articles 25 – 28",
        "icon": "🕌",
        "overview": (
            "The Right to Freedom of Religion establishes India's unique model of positive secularism. "
            "Rather than enforcing strict separation between state and religion, the Constitution guarantees that all religions "
            "are treated with equal respect ('Sarva Dharma Sambhava'), ensuring freedom of conscience, practice, and administration of religious affairs."
        ),
        "simple_meaning": (
            "You have complete freedom to follow any religion, change your religion, perform rituals, or follow no religion at all."
        ),
        "why_it_matters": (
            "In a country as diverse as India, religious freedom ensures peace, mutual respect, and protects religious minorities."
        ),
        "articles_detail": [
            {
                "article": "Article 25",
                "title": "Freedom of Conscience & Right to Profess, Practice, and Propagate Religion",
                "meaning": "Guarantees to all persons equal freedom of conscience and the right to freely profess, practice, and propagate religion.",
                "purpose": "Protects individual religious liberty while empowering the State to reform social evils (e.g. opening Hindu temples to all castes).",
                "example": "A person wearing a turban, cross, or hijab as part of their sincere religious practice."
            },
            {
                "article": "Article 26",
                "title": "Freedom to Manage Religious Affairs",
                "meaning": "Gives religious denominations the right to establish institutions, manage their internal religious affairs, and acquire property.",
                "purpose": "Protects collective religious rights of communities and institutions.",
                "example": "A religious trust managing its places of worship, charities, and properties."
            },
            {
                "article": "Article 27",
                "title": "Freedom from Paying Taxes for Religion",
                "meaning": "No person shall be compelled to pay any taxes whose proceeds are specifically appropriated for promoting any particular religion.",
                "purpose": "Prevents state funds collected from general taxpayers from being used to favor one religion over others.",
                "example": "Government cannot levy a special tax on citizens to build a temple, mosque, or church."
            },
            {
                "article": "Article 28",
                "title": "Freedom from Attending Religious Instruction in Educational Institutions",
                "meaning": "No religious instruction shall be provided in any educational institution wholly maintained out of State funds.",
                "purpose": "Maintains secular environment in state-run public schools.",
                "example": "Government schools cannot make morning prayers or religious classes mandatory for students."
            }
        ],
        "real_life_examples": [
            "Personal Faith: Celebrating festivals, visiting places of worship, or maintaining personal religious diet.",
            "Public Processions: Organizing peaceful religious processions subject to police route permissions.",
            "Secular Education: Government-run schools following a secular curriculum free from mandatory religious rituals."
        ],
        "limitations": [
            "Public Order, Morality, and Health: Religious practices can be restricted if they harm public safety or health (e.g. banning Sati or regulating loudspeaker volumes).",
            "Social Reform: Article 25(2)(b) allows the State to pass laws providing for social welfare and throwing open Hindu religious institutions to all classes."
        ],
        "common_misconceptions": [
            {
                "myth": "The right to propagate religion includes the right to forcibly convert someone using money or threats.",
                "truth": "The Supreme Court in Rev. Stainislaus (1977) held that 'propagate' means transmitting religious tenets; it does NOT include the right to convert another person by coercion or inducement."
            }
        ],
        "landmark_judgments": [
            {
                "case": "S.R. Bommai v. Union of India (1994)",
                "ruling": "Unanimously affirmed that Secularism is a basic feature of the Constitution of India."
            },
            {
                "case": "Shayara Bano v. Union of India (2017)",
                "ruling": "Declared the practice of Instant Triple Talaq (Talaq-e-Biddat) unconstitutional and void under Article 14 and 21."
            }
        ],
        "quick_facts": [
            "Wearing and carrying of Kirpans is explicitly included in the profession of the Sikh religion under Article 25 Explanation I.",
            "Indian secularism means equal treatment of all religions by the State ('Sarva Dharma Sambhava')."
        ],
        "faqs": [
            {
                "q": "Can the government charge a fee at religious sites?",
                "a": "Yes, Article 27 prohibits taxes for promoting religion, but allows government fees levied to provide administrative or security services."
            }
        ],
        "related_provisions": ["Article 15", "Article 29", "Article 30"]
    },
    {
        "id": "cultural",
        "title": "Cultural and Educational Rights",
        "articles_range": "Articles 29 – 30",
        "icon": "📚",
        "overview": (
            "Cultural and Educational Rights safeguard minority communities against cultural assimilation. "
            "Recognizing India's immense linguistic, scriptural, and religious diversity, the Constituent Assembly enacted these protections "
            "so that minority groups could preserve their unique heritage and establish their own educational institutions."
        ),
        "simple_meaning": (
            "Minority communities (religious or linguistic) have the full right to preserve their language, script, and culture, and run their own schools and colleges."
        ),
        "why_it_matters": (
            "It prevents majoritarian cultural imposition and ensures that minority languages, literature, and traditions thrive."
        ),
        "articles_detail": [
            {
                "article": "Article 29",
                "title": "Protection of Interests of Minorities",
                "meaning": "Any section of citizens residing in India having a distinct language, script, or culture has the right to conserve the same. No citizen shall be denied admission into state-aided educational institutions on grounds only of religion, race, caste, or language.",
                "purpose": "Protects language, script, and cultural heritage of all citizen groups.",
                "example": "A group preserving an endangered tribal dialect or regional script."
            },
            {
                "article": "Article 30",
                "title": "Right of Minorities to Establish & Administer Educational Institutions",
                "meaning": "All religious and linguistic minorities have the right to establish and administer educational institutions of their choice.",
                "purpose": "Grants educational autonomy to religious and linguistic minorities.",
                "example": "Minority communities operating schools or universities offering education while preserving their heritage."
            }
        ],
        "real_life_examples": [
            "Linguistic Protection: Establishing Tamil or Bengali medium schools in states where they are a minority.",
            "University Administration: Minority educational institutions managing student admissions while maintaining academic standards."
        ],
        "limitations": [
            "Academic Standards: Minority institutions are subject to national regulatory standards regarding teacher qualifications, health, sanitation, and academic excellence."
        ],
        "common_misconceptions": [
            {
                "myth": "Article 29 applies ONLY to religious minorities.",
                "truth": "The Supreme Court has clarified that Article 29 applies to 'any section of citizens', including majority communities preserving a local script or dialect."
            }
        ],
        "landmark_judgments": [
            {
                "case": "T.M.A. Pai Foundation v. State of Karnataka (2002)",
                "ruling": "11-judge bench judgment establishing the rights of minority institutions to admit students and determine fee structures subject to non-profiteering."
            }
        ],
        "quick_facts": [
            "Article 30(1A) mandates that state land acquisition of minority educational institutions must pay compensation that does not restrict their constitutional right."
        ],
        "faqs": [
            {
                "q": "Are minority educational institutions exempt from national entrance exams like NEET?",
                "a": "No, the Supreme Court ruled that common national entrance tests (NEET) apply to minority institutions to ensure academic standards."
            }
        ],
        "related_provisions": ["Article 15", "Article 21A", "Article 350A"]
    },
    {
        "id": "remedies",
        "title": "Right to Constitutional Remedies",
        "articles_range": "Article 32 & 226",
        "icon": "⚖️",
        "overview": (
            "Article 32 is the enforcement engine of the Constitution. Dr. B.R. Ambedkar famously called Article 32 "
            "'the very soul of the Constitution and the very heart of it'. Without judicial enforcement mechanisms, "
            "Fundamental Rights would be mere pious declarations. Article 32 gives every citizen the right to approach the Supreme Court directly "
            "for the enforcement of Fundamental Rights through 5 High Constitutional Writs."
        ),
        "simple_meaning": (
            "If your Fundamental Rights are violated by the government or police, you can go directly to the Supreme Court (Article 32) or High Court (Article 226) to get an order enforcing your rights."
        ),
        "why_it_matters": (
            "It turns constitutional promises into enforceable legal realities. It gives courts the power to quash illegal government orders, release illegally detained persons, and stop administrative abuse."
        ),
        "articles_detail": [
            {
                "article": "Article 32",
                "title": "Remedies for Enforcement of Rights Guaranteed by Part III",
                "meaning": "Guarantees the right to move the Supreme Court by appropriate proceedings for the enforcement of Fundamental Rights.",
                "purpose": "Provides direct constitutional access to Apex Court. The Supreme Court can issue 5 types of Writs.",
                "example": "Approaching the Supreme Court directly when police illegally detain a person."
            },
            {
                "article": "Article 226",
                "title": "Power of High Courts to Issue Writs",
                "meaning": "Empowers High Courts to issue writs for the enforcement of Fundamental Rights AND for any other legal right.",
                "purpose": "Wider scope than Article 32 since High Courts can issue writs for statutory rights as well as fundamental rights.",
                "example": "Filing a writ in the State High Court against an illegal municipal demolition order."
            }
        ],
        "real_life_examples": [
            "Habeas Corpus: Filing a emergency petition when a family member is taken into police custody without record.",
            "Mandamus: Demanding a magistrate or municipal authority perform their mandatory statutory duty.",
            "Quo Warranto: Challenging the appointment of an official who lacks required statutory qualifications for a public office."
        ],
        "writs_breakdown": [
            {
                "writ": "1. Habeas Corpus ('To have the body of')",
                "desc": "Issued to produce an illegally detained person before the court. Safeguard against unlawful custody."
            },
            {
                "writ": "2. Mandamus ('We command')",
                "desc": "Issued to command a public authority to perform a mandatory statutory duty they failed or refused to perform."
            },
            {
                "writ": "3. Prohibition ('To forbid')",
                "desc": "Issued by a higher court to a lower court or tribunal to stop them from exceeding their jurisdiction."
            },
            {
                "writ": "4. Certiorari ('To be certified')",
                "desc": "Issued by a higher court to quash an illegal order already passed by a lower court or administrative tribunal."
            },
            {
                "writ": "5. Quo Warranto ('By what authority')",
                "desc": "Issued to inquire into the legality of a person holding a public office to prevent illegal usurpation."
            }
        ],
        "limitations": [
            "Suspension during Emergency: Article 32 can be suspended by Presidential Order under Article 359 during a National Emergency (except Articles 20 and 21).",
            "Alternative Remedy: Courts may direct petitioners to approach High Court under Article 226 first before coming to Supreme Court under Article 32."
        ],
        "common_misconceptions": [
            {
                "myth": "Article 32 can be used for routine money recovery or property title disputes.",
                "truth": "Article 32 is strictly for enforcing Part III Fundamental Rights. Civil disputes must go to civil courts or High Courts under Article 226."
            }
        ],
        "landmark_judgments": [
            {
                "case": "L. Chandra Kumar v. Union of India (1997)",
                "ruling": "Declared that the power of judicial review under Article 32 and Article 226 is an integral part of the Basic Structure of the Constitution."
            }
        ],
        "quick_facts": [
            "Dr. Ambedkar called Article 32 the 'Heart and Soul of the Constitution'.",
            "Article 226 is wider in scope than Article 32 because High Courts can issue writs for fundamental rights as well as ordinary legal rights."
        ],
        "faqs": [
            {
                "q": "Can PIL (Public Interest Litigation) be filed under Article 32?",
                "a": "Yes! Supreme Court expanded Article 32 to allow Public Interest Litigation (PIL) filed on behalf of disadvantaged citizens."
            }
        ],
        "related_provisions": ["Article 226", "Article 136", "Article 142"]
    }
]


EXPANDED_FUNDAMENTAL_DUTIES: List[Dict[str, Any]] = [
    {
        "code": "(a)",
        "title": "Respect Constitution, Flag & Anthem",
        "duty": "To abide by the Constitution and respect its ideals and institutions, the National Flag and the National Anthem.",
        "why_it_exists": "Fosters national unity and respect for sacred national symbols representing the sovereignty of India.",
        "historical_background": "Added by the 42nd Amendment Act (1976) based on the Swaran Singh Committee recommendations.",
        "how_to_fulfill": "Stand respectfully during the National Anthem, follow the Flag Code of India, and obey constitutional laws.",
        "enforcement_laws": "Prevention of Insults to National Honour Act, 1971 & Flag Code of India, 2002.",
        "misconception": "Thinking standing for national anthem in cinema halls is mandatory under all circumstances (SC clarified voluntary respect)."
    },
    {
        "code": "(b)",
        "title": "Cherish Ideals of Freedom Struggle",
        "duty": "To cherish and follow the noble ideals which inspired our national struggle for freedom.",
        "why_it_exists": "Reminds citizens of the sacrifices made by freedom fighters for independence, democracy, non-violence, and secularism.",
        "historical_background": "Rooted in the values of Mahatma Gandhi, Bhagat Singh, Subhas Chandra Bose, and the Constituent Assembly.",
        "how_to_fulfill": "Promote freedom, non-violence, truth, and democratic debate in civic life.",
        "enforcement_laws": "Moral civic duty reflecting national heritage.",
        "misconception": "Assuming freedom struggle ideals belong only to history textbooks."
    },
    {
        "code": "(c)",
        "title": "Uphold Sovereignty, Unity & Integrity",
        "duty": "To uphold and protect the sovereignty, unity and integrity of India.",
        "why_it_exists": "Protects the territorial integrity and unified national identity of India against secessionist threats.",
        "historical_background": "Enacted in 1976 during internal emergency concerns to reinforce national unity.",
        "how_to_fulfill": "Reject communal, regional, or secessionist violence; stand united during national crises.",
        "enforcement_laws": "Unlawful Activities (Prevention) Act (UAPA), 1967 & Bharatiya Nyaya Sanhita (Sec 152).",
        "misconception": "Believing peaceful regional pride is anti-national (regional culture enriches national composite integrity)."
    },
    {
        "code": "(d)",
        "title": "Defend Country & Render National Service",
        "duty": "To defend the country and render national service when called upon to do so.",
        "why_it_exists": "Ensures collective defense and civic participation during national security emergencies or natural disasters.",
        "historical_background": "Reflects constitutional duty to support armed forces and civil defense.",
        "how_to_fulfill": "Volunteer during natural disasters, support armed forces welfare, participate in civil defense drills.",
        "enforcement_laws": "National Cadet Corps Act, 1948 & Disaster Management Act, 2005.",
        "misconception": "Believing India has mandatory military conscription (military service in India remains strictly voluntary)."
    },
    {
        "code": "(e)",
        "title": "Promote Harmony & Renounce Practices Derogatory to Women",
        "duty": "To promote harmony and the spirit of common brotherhood amongst all the people of India transcending religious, linguistic and regional diversities; to renounce practices derogatory to the dignity of women.",
        "why_it_exists": "Combats communal violence, gender abuse, dowry, female foeticide, and sexual harassment.",
        "historical_background": "Core pillar of social reform ensuring gender equality and inter-faith harmony.",
        "how_to_fulfill": "Treat women with equal dignity, speak out against dowry/harassment, reject communal hate speech.",
        "enforcement_laws": "POSH Act 2013, Dowry Prohibition Act 1961, Protection of Women from Domestic Violence Act 2005, BNS.",
        "misconception": "Thinking respect for women is merely a private family affair rather than a mandatory constitutional duty."
    },
    {
        "code": "(f)",
        "title": "Preserve Composite Culture",
        "duty": "To value and preserve the rich heritage of our composite culture.",
        "why_it_exists": "Protects India's multi-cultural, multi-religious, and multi-linguistic heritage ('Ganga-Jamuni Tehzeeb').",
        "historical_background": "Recognizes that Indian culture is a synthesis of diverse traditions over millennia.",
        "how_to_fulfill": "Protect historical monuments, support traditional art forms, respect diverse cultural festivals.",
        "enforcement_laws": "Ancient Monuments and Archaeological Sites and Remains Act, 1958.",
        "misconception": "Equating composite culture to a single uniform cultural tradition."
    },
    {
        "code": "(g)",
        "title": "Protect Natural Environment & Wildlife",
        "duty": "To protect and improve the natural environment including forests, lakes, rivers and wild life, and to have compassion for living creatures.",
        "why_it_exists": "Crucial for ecological balance, climate action, and protecting animal welfare.",
        "historical_background": "Pioneering constitutional mandate binding citizens to environmental preservation.",
        "how_to_fulfill": "Plant trees, reduce plastic waste, conserve water, report illegal poaching or river pollution.",
        "enforcement_laws": "Wildlife Protection Act 1972, Water Act 1974, Forest Conservation Act 1980, Environment Protection Act 1986.",
        "misconception": "Believing environmental protection is solely the responsibility of government forest departments."
    },
    {
        "code": "(h)",
        "title": "Develop Scientific Temper & Humanism",
        "duty": "To develop the scientific temper, humanism and the spirit of inquiry and reform.",
        "why_it_exists": "Encourages rational thinking, evidence-based reasoning, and combats harmful superstitions.",
        "historical_background": "Championed by Jawaharlal Nehru as essential for India's scientific and technological advancement.",
        "how_to_fulfill": "Question superstitions, verify news before sharing online, support scientific research, embrace rational reform.",
        "enforcement_laws": "Drugs and Magic Remedies (Objectionable Advertisements) Act, 1954.",
        "misconception": "Thinking scientific temper is only for scientists or engineers (it is an everyday attitude of rational thinking)."
    },
    {
        "code": "(i)",
        "title": "Safeguard Public Property & Abjure Violence",
        "duty": "To safeguard public property and to abjure violence.",
        "why_it_exists": "Prevents destruction of buses, trains, government buildings, and public infrastructure during strikes or protests.",
        "historical_background": "Protects national wealth built with taxpayer money.",
        "how_to_fulfill": "Protest peacefully without damaging public buses or property; report vandalism.",
        "enforcement_laws": "Prevention of Damage to Public Property Act, 1984.",
        "misconception": "Believing damaging public property during strikes is an acceptable form of political protest."
    },
    {
        "code": "(j)",
        "title": "Strive Towards Excellence",
        "duty": "To strive towards excellence in all spheres of individual and collective activity so that the nation constantly rises to higher levels of endeavour and achievement.",
        "why_it_exists": "Drives national progress in sports, science, arts, trade, education, and governance.",
        "historical_background": "Encourages personal responsibility and hard work as a contribution to nation building.",
        "how_to_fulfill": "Work hard in your job or studies, maintain high ethical standards, support collective community goals.",
        "enforcement_laws": "Moral constitutional aspiration driving national policies.",
        "misconception": "Viewing personal excellence as separate from national progress."
    },
    {
        "code": "(k)",
        "title": "Provide Education to Child Aged 6-14",
        "duty": "Who is a parent or guardian to provide opportunities for education to his child or, as the case may be, ward between the age of six and fourteen years.",
        "why_it_exists": "Ensures parents fulfill their duty to send children to school alongside the state's obligation under Art 21A.",
        "historical_background": "Added by the 86th Constitutional Amendment Act (2002) alongside Right to Education (Art 21A).",
        "how_to_fulfill": "Send children to school, prevent child labor, support local school management committees.",
        "enforcement_laws": "Right to Free and Compulsory Education (RTE) Act, 2009.",
        "misconception": "Believing education is only the government's responsibility (parents share the constitutional duty)."
    }
]

# Backward compatibility aliases
FUNDAMENTAL_RIGHTS = EXPANDED_FUNDAMENTAL_RIGHTS
FUNDAMENTAL_DUTIES = EXPANDED_FUNDAMENTAL_DUTIES

