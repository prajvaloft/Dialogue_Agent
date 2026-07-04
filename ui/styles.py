def load_css(theme="dark"):
    if theme == "dark":
        bg = "#0B1120"
        sidebar = "#111827"
        text = "#FFFFFF"

        card_bg = "#1F2937"
        border = "rgba(255,255,255,0.12)"
        container_bg = "rgba(31,41,55,.85)"

    else:
        bg = "#F8FAFC"
        sidebar = "#FFFFFF"
        text = "#111827"

        card_bg = "#FFFFFF"
        border = "#E5E7EB"
        container_bg = "#FFFFFF"

    

    return f"""
    <style>

    /* Hide Streamlit UI */

    header {{
        visibility: hidden;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    [data-testid="stToolbar"] {{
        display: none;
    }}

    /* Main App */

    .stApp {{
        background: {bg};
        color: {text};
    }}

    .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }}

    /* Sidebar */

    [data-testid="stSidebar"] {{
        background: {sidebar};
    }}

    [data-testid="stSidebar"] * {{
        color: {text};
    }}

    /* Metric Cards */

    .metric-card {{
        background: {card_bg};
        border: 1px solid {border};
        color: {text};
        border-radius: 18px;
        padding: 18px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0,0,0,.12);
        transition: all .3s ease;
    }}

    .metric-card:hover {{
        transform: translateY(-6px);
        box-shadow: 0 15px 35px rgba(0,0,0,.25);
    }}

    .metric-title {{
        font-size: 16px;
        opacity: .8;
        margin-bottom: 10px;
    }}

    .metric-value {{
        font-size: 34px;
        font-weight: 700;
    }}

    /* Glass Cards */

    .glass-card {{
        background: {container_bg};
        color: {text};
        backdrop-filter: blur(18px);
        border: 1px solid {border};
        border-radius: 20px;
        padding: 28px;
        box-shadow: 0 12px 35px rgba(0,0,0,.12);
    }}

    /* Hero Header */

    .hero-header {{
        padding: 30px;
        border-radius: 20px;
        background: linear-gradient(135deg,#4F46E5,#2563EB);
        color: white;
        box-shadow: 0 12px 35px rgba(79,70,229,.25);
        animation: glow 3s ease-in-out infinite alternate;
    }}

    /* Streamlit Containers */

    [data-testid="stVerticalBlockBorderWrapper"] {{
        background: {container_bg};
        backdrop-filter: blur(18px);
        border: 1px solid {border};
        color: {text};
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 12px 35px rgba(0,0,0,.12);
    }}

    /* Buttons */

    .stButton > button {{
        width: 100%;
        border-radius: 12px;
        border: none;
        background: linear-gradient(135deg,#4F46E5,#2563EB);
        color: white;
        font-weight: 600;
        padding: .75rem;
        transition: all .3s ease;
    }}

    .stButton > button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(37,99,235,.35);
    }}

    /* Select Boxes */

    .stSelectbox {{
        margin-bottom: 12px;
    }}

    /* Progress Bar */

    .stProgress > div > div > div {{
        background: linear-gradient(90deg,#4F46E5,#2563EB);
    }}

    /* Chat Messages */

    [data-testid="stChatMessage"] {{
        border-radius: 14px;
    }}

    /* Live Status Dot */

    .live-dot {{
        width: 18px;
        height: 18px;
        background: #22C55E;
        border-radius: 50%;
        box-shadow: 0 0 10px #22C55E;
        animation: pulse 1.5s infinite;
    }}

    /* Animations */

    @keyframes pulse {{

        0% {{
            transform: scale(1);
            box-shadow: 0 0 5px #22C55E;
        }}

        50% {{
            transform: scale(1.3);
            box-shadow: 0 0 20px #22C55E;
        }}

        100% {{
            transform: scale(1);
            box-shadow: 0 0 5px #22C55E;
        }}
    }}

    @keyframes fadeInUp {{

        from {{
            opacity: 0;
            transform: translateY(30px);
        }}

        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    @keyframes glow {{

        from {{
            box-shadow: 0 12px 35px rgba(79,70,229,.20);
        }}

        to {{
            box-shadow: 0 15px 50px rgba(37,99,235,.60);
        }}
    }}
    /* ---------- Global Text ---------- */

    html,
    body,
    .stApp,
    p,
    label,
    small,
    strong,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {{
        color: {text};
    }}
/* ---------- Select Boxes ---------- */

div[data-baseweb="select"] > div {{
    background: {container_bg} !important;
    border: 1px solid {border} !important;
    color: {text} !important;
    border-radius: 10px;
}}

div[data-baseweb="popover"] {{
    background: {container_bg} !important;
}}

div[role="listbox"] {{
    background: {container_bg} !important;
}}

div[role="option"] {{
    background: {container_bg} !important;
    color: {text} !important;
}}

div[role="option"] * {{
    color: {text} !important;
}}

div[role="option"]:hover {{
    background: rgba(79,70,229,.25) !important;
}}
</style>
"""
