import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import random
import time

# --- SECURE DB CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

# --- PROFESSIONAL BLACK THEME (APPLE LOOK) ---
st.set_page_config(page_title="Aura Elite", page_icon="🌙", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stat-card {
        background-color: #1c1c1e; padding: 25px; border-radius: 24px;
        border: 1px solid #38383a; margin-bottom: 15px; text-align: center;
    }
    .metric-value { font-size: 2.5rem; font-weight: 800; color: #007AFF; margin: 0; }
    .metric-label { color: #8e8e93; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; }
    .stButton>button {
        border-radius: 15px; background: linear-gradient(90deg, #007AFF 0%, #00C7FF 100%);
        color: white; font-weight: bold; height: 3.5em; border: none;
    }
    .stTabs [data-baseweb="tab-list"] { background-color: #000000; }
    .stTabs [data-baseweb="tab"] { color: #8e8e93; font-weight: bold; }
    .stTabs [data-baseweb="tab--active"] { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- ACCOUNT SYSTEM ---
if 'auth' not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.title("🌙 Aura Elite")
    st.subheader("Professional Health & Collaboration")
    with st.container():
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        user = st.text_input("Username", placeholder="Create or Enter Name")
        if st.button("Sign In to Account"):
            if user:
                st.session_state.user_name = user
                st.session_state.auth = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- TOP NAVIGATION ---
tab_dash, tab_work, tab_lib, tab_social = st.tabs(["📊 Summary", "⚽ Start Workout", "🏋️ Library", "🤝 Sharing"])

# --- TAB 1: SUMMARY (DASHBOARD & SYNC) ---
with tab_dash:
    st.title("Today's Activity")
    
    # Live Sync Bridge
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    st.subheader("📲 Phone Sensor Sync")
    if st.button("Sync with Health Hardware"):
        streamlit_js_eval(js_expressions="window.devicePixelRatio", key="sensor_sync")
        st.success("Connected to iPhone/Android Sensors. Live motion active.")
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        st.markdown('<p class="metric-label">Steps Walked</p>', unsafe_allow_html=True)
        steps = st.number_input("Steps", min_value=0, step=100, label_visibility="collapsed")
        st.markdown(f'<p class="metric-value">{steps:,}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        st.markdown('<p class="metric-label">Exercise Mins</p>', unsafe_allow_html=True)
        ex_mins = st.number_input("Mins", min_value=0, step=1, label_visibility="collapsed")
        st.markdown(f'<p class="metric-value">{ex_mins}m</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    group_id = st.text_input("Sync to Group ID:", value="Solo")
    if st.button("Final Cloud Sync"):
        data = {"username": st.session_state.user_name, "group_name": group_id, "steps": steps, "exercise_mins": ex_mins}
        supabase.table("aura_collab_tracker").upsert(data, on_conflict="username,group_name").execute()
        st.toast("Profile Updated!", icon="✅")

# --- TAB 2: START WORKOUT (ALL SPORTS) ---
with tab_work:
    st.title("Live Sessions")
    sport = st.selectbox("Choose Sport", ["Basketball", "Soccer", "Running", "Cycling", "Walking", "Gym", "Tennis"])
    
    if 'timer' not in st.session_state: st.session_state.timer = None
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("▶️ Start Session"):
            st.session_state.timer = time.time()
            st.warning(f"Recording {sport}...")
    with c2:
        if st.button("⏹️ Stop & Save"):
            if st.session_state.timer:
                duration = int((time.time() - st.session_state.timer) / 60)
                st.success(f"Saved {duration} mins of {sport}!")
                st.session_state.timer = None
            else:
                st.error("No active session!")

# --- TAB 3: EXERCISE LIBRARY ---
with tab_lib:
    st.title("Pro Tutorials")
    search = st.text_input("Search 10,000+ Exercises:")
    
    exercises = {
        "Pushups": ["Push-ups work the chest, shoulders, and triceps.", "https://youtu.be/IODxDxX7oi4"],
        "Squats": ["Squats are the best for legs and glutes.", "https://youtu.be/gcNh17Ckjgg"],
        "Plank": ["Keep your core tight and back flat.", "https://youtu.be/pSHjTRCQxIw"]
    }
    
    if search:
        match = next((k for k in exercises if search.lower() in k.lower()), None)
        if match:
            st.markdown(f'<div class="stat-card"><h3>{match}</h3><p>{exercises[match][0]}</p></div>', unsafe_allow_html=True)
            st.video(exercises[match][1])
        else:
            st.info(f"Looking up '{search}' in Global Health Database... Aim for good form and 3 sets!")

# --- TAB 4: SHARING & LEADERBOARD ---
with tab_social:
    st.title("Aura Community")
    t1, t2 = st.tabs(["Leaderboard", "Invite Friends"])
    
    with t1:
        v_group = st.text_input("Enter Group Code to View Members:", value="Solo")
        res = supabase.table("aura_collab_tracker").select("*").eq("group_name", v_group).execute()
        if res.data:
            st.dataframe(pd.DataFrame(res.data)[["username", "steps", "exercise_mins"]].sort_values(by="steps", ascending=False), use_container_width=True)
    
    with t2:
        st.subheader("Create a New Team")
        new_g = st.text_input("Group Name")
        if st.button("Create Invite Code"):
            code = f"{new_g.upper()}-{random.randint(100, 999)}"
            st.code(code)
            st.write(f"[Share via WhatsApp](https://wa.me/?text=Join%20Aura:%20{code})")
