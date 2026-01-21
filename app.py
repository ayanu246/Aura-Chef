import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import random
import time

# --- DB CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Elite", page_icon="⚡", layout="wide")

# --- UI STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stat-card {
        background-color: #1c1c1e; padding: 20px; border-radius: 20px;
        border: 1px solid #38383a; margin-bottom: 15px;
    }
    .exercise-card {
        background: linear-gradient(145deg, #2c2c2e, #1c1c1e);
        padding: 15px; border-radius: 15px; border-left: 5px solid #007AFF; margin-top: 10px;
    }
    .stButton>button {
        border-radius: 12px; background: #007AFF; color: white; font-weight: bold; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- AUTH ---
if 'auth' not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.title("⚡ Aura Elite")
    user = st.text_input("Username")
    if st.button("Enter Pro Hub"):
        st.session_state.user_name = user
        st.session_state.auth = True
        st.rerun()
    st.stop()

# --- NAVIGATION ---
tabs = st.tabs(["📊 Summary", "🏋️ Exercise Library", "⚽ Start Workout", "🤝 Social"])

# --- TAB 1: SUMMARY ---
with tabs[0]:
    st.title("My Health")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        steps = st.number_input("Steps", min_value=0, step=100)
        exercise_min = st.number_input("Total Exercise (Min)", min_value=0)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        water = st.number_input("Water", min_value=0.0)
        sleep = st.number_input("Sleep", min_value=0.0)
        st.markdown('</div>', unsafe_allow_html=True)
    
    active_g = st.text_input("Sync to Group:", value="Solo")
    if st.button("Cloud Sync"):
        data = {"username": st.session_state.user_name, "group_name": active_g, "steps": steps, "sleep_hours": sleep, "water": water, "exercise_mins": exercise_min}
        supabase.table("aura_collab_tracker").upsert(data, on_conflict="username,group_name").execute()
        st.success("Synced!")

# --- TAB 2: EXERCISE LIBRARY ---
with tabs[1]:
    st.title("Exercise Library")
    search = st.text_input("🔍 Search 1000+ Exercises (e.g., Pushups, Squats, Bench Press)")
    
    # Mock Database of Exercises
    exercises = {
        "Pushups": {"steps": "1. Hands shoulder-width apart. 2. Lower chest to floor. 3. Push back up.", "video": "https://www
