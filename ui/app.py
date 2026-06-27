import time
import sys
from pathlib import Path
from styles import load_css
import plotly.express as px
ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

import streamlit as st
import pandas as pd
from agent.inference import predict_action

# ---------------- Page Configuration ---------------- #

st.set_page_config(
    page_title="Movie Booking AI Agent",
    page_icon="🎬",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

with st.sidebar:
    st.title("🎬 AI Agent")

    st.info("""
**Algorithm:** Deep Q Network (DQN)

**Environment:** Movie Booking

**State Size:** 4

**Action Space:** 5
""")

    st.success("✅ Model Loaded Successfully")
    st.markdown("---")
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True

    st.session_state.dark_mode = st.toggle(
        "🌙 Dark Mode",
        value=st.session_state.dark_mode
    )

    theme = "Dark" if st.session_state.dark_mode else "Light"
# ---------------- Theme Styling ---------------- #
st.markdown(
    load_css(theme.lower()),
    unsafe_allow_html=True
)
# ---------------- Header ---------------- #
st.markdown("""
<div class="hero-header">

<h1 style="margin:0;">
🎬 Movie Booking AI
</h1>

<h3 style="margin-top:8px;font-weight:400;">
Smart Reservation Assistant powered by Deep Q Networks
</h3>

</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

cards = [
    ("🟢", "Model", "ONLINE"),
    ("🧠", "Algorithm", "DQN"),
    ("📊", "State Size", "4"),
    ("⚡", "Actions", "5")
]

for col, (icon, title, value) in zip([c1, c2, c3, c4], cards):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size:34px;">{icon}</div>
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)
# ---------------- Main Layout ---------------- #

st.markdown("<br>", unsafe_allow_html=True)
left_col, right_col = st.columns(
    [1.7, 1],
    gap="large"
)
# ======================================================
# LEFT COLUMN
# ======================================================

with left_col:

    booking_container = st.container(border=True)

    with booking_container:

        st.markdown("## 🎟 Booking Information")

        movie = st.selectbox(
            "🎬 Movie",
            ["None", "Avengers", "Interstellar", "Batman", "Inception"],
            key="movie_select"
        )

        theater = st.selectbox(
            "🏢 Theater",
            ["None", "PVR", "INOX", "Cinepolis"],
            key="theater_select"
        )

        show_time = st.selectbox(
            "⏰ Show Time",
            ["None", "10:00 AM", "2:00 PM", "6:00 PM", "9:00 PM"],
            key="showtime_select"
        )

        confirm = st.toggle(
            "✅ Confirm Booking",
            key="confirm_toggle"
        )

        st.divider()

        progress = (
            (movie != "None")
            + (theater != "None")
            + (show_time != "None")
            + confirm
        ) / 4

        st.markdown("### 📈 Booking Progress")
        st.progress(progress)

        if confirm:
            status = "Completed"
        elif show_time != "None":
            status = "Ready for Confirmation"
        elif theater != "None":
            status = "Waiting for Show Time"
        elif movie != "None":
            status = "Waiting for Theater"
        else:
            status = "Pending"

        st.metric("Status", status)

        st.divider()

        st.markdown("### 📝 Booking Summary")

        st.info(f"""
**Movie:** {movie}

**Theater:** {theater}

**Show Time:** {show_time}

**Status:** {status}

**Confirmed:** {"Yes" if confirm else "No"}
""")    
    
# ======================================================
# RIGHT COLUMN
# ======================================================

# ======================================================
# RIGHT COLUMN
# ======================================================

with right_col:

    with st.container(border=True):

        st.markdown("## 🤖 AI Recommendation")

        state = [
            1 if movie != "None" else 0,
            1 if theater != "None" else 0,
            1 if show_time != "None" else 0,
            1 if confirm else 0
        ]
        with st.spinner("🤖 AI is analyzing booking state..."):
            time.sleep(1)
            action, q_values = predict_action(state)

        st.write("Raw Action:", action)

        display_action = action
        chat_action = action

        # Convert DQN action into user-friendly messages

        if confirm:
            display_action = "🎉 Booking Confirmed!"
            chat_action = f"""

🎉 Booking Confirmed!

🍿 Enjoy **{movie}**

🏢 Theater: **{theater}**

🕒 Showtime: **{show_time}**

🎟 Your tickets have been reserved successfully.

✨ Grab your popcorn and have an amazing movie experience!

Thank you for booking with Movie Booking AI ❤️
"""
            st.balloons()

        elif action == "Ask Movie":
            display_action = "🎬 Select a Movie"
            chat_action = "🎬 Which movie would you like to watch?"

        elif action == "Ask Theater":
            display_action = "🏢 Select a Theater"
            chat_action = "🏢 Which theater would you prefer?"

        elif action == "Ask Show Time":
            display_action = "🕒 Select Show Time"
            chat_action = "🕒 What show time would you like?"

        elif action == "Confirm Booking":
            display_action = "✅ Confirm Booking"
            chat_action = (
                "✅ Please confirm your booking to complete the reservation."
            )

        
        
        if theme == "Dark":
            ai_bg = "linear-gradient(145deg,#111827,#1E3A8A)"
            ai_text = "white"
        else:
            ai_bg = "#FFFFFF"
            ai_text = "#111827"
        st.markdown(f"""         
        <div style="
        background:{ai_bg};
        border-radius:25px;
        padding:28px;
        color:{ai_text};
        box-shadow:0 15px 40px rgba(0,0,0,.30);
        border:1px solid rgba(255,255,255,.08);
        margin-bottom:25px;
        ">

        <div style="font-size:15px;opacity:.8;">
        🤖 AI Assistant
        </div>

        <div style="
        font-size:30px;
        font-weight:bold;
        margin-top:10px;">
        {display_action}
        </div>

        <hr style="
        border:none;
        height:1px;
        background:rgba(255,255,255,.15);
        margin:20px 0;
        ">

        <div style="
        font-size:14px;
        line-height:1.8;
        opacity:.9;">

        🧠 Deep Q Network successfully evaluated the booking state.

        <br><br>

        ⚡ Confidence: High

        <br><br>

        🎯 Next Best Action selected automatically.

        </div>

        </div>
        """, unsafe_allow_html=True)

        # ---------------- Conversation ---------------- #

        # ---------------- Conversation ---------------- #

# ---------------- Conversation ---------------- #

with st.expander("💬 Conversation", expanded=False):

    conversation = []

    conversation.append(
        ("🤖 AI", "Welcome to Movie Booking AI!")
    )

    if movie != "None":
        conversation.append(
            ("👤 You", f"I want to watch **{movie}**.")
        )

    if theater != "None":
        conversation.append(
            ("👤 You", f"I prefer **{theater}** theater.")
        )

    if show_time != "None":
        conversation.append(
            ("👤 You", f"I would like the **{show_time}** show.")
        )

    conversation.append(
        ("🤖 AI", chat_action)
    )

    # Display Conversation
    for sender, message in conversation:
        st.markdown(f"**{sender}:** {message}")

    # ---------------- Q Network Analysis ---------------- #

    st.markdown("---")
    st.markdown("## 📊 Q Network Analysis")

    action_names = [
        "Ask Movie",
        "Ask Theater",
        "Ask Show Time",
        "Confirm Booking",
        "Complete Booking"
    ]

    q_df = pd.DataFrame({
        "Action": action_names,
        "Q Value": q_values
    })

    best_action = q_df.loc[q_df["Q Value"].idxmax()]

    st.info(
        f"🏆 Best Action: **{best_action['Action']}**"
    )

    st.dataframe(
        q_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 📈 Action Scores")

    fig = px.bar(
        q_df,
        x="Action",
        y="Q Value",
        text="Q Value",
        title="Deep Q Network Action Scores"
    )

    fig.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside"
    )

    fig.update_layout(
        height=400,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        xaxis_title="",
        yaxis_title="Q Value",
        margin=dict(l=20, r=20, t=60, b=20)
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="q_network_chart"
    )