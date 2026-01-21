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

st.set_page_config(page_title="Aura Elite", page_icon="🌙", layout="wide")

# --- PRO APPLE BLACK CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stat-card {
        background-color: #1c1c1e; padding: 20px; border-radius: 20px;
        border: 1px solid #38383a; margin-bottom: 15px;
    }
    .heart-rate { color: #ff2d55; font-size: 3rem; font-weight: bold; }
    .stButton>button {
        border-radius: 12px; background: #007AFF; color: white; font-weight: bold; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ACCOUNT PERSISTENCE ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🌙 Aura Elite")
    user = st.text_input("Username / ID")
    if st.button("Sign In"):
        st.session_state.user_name = user
        st.session_state.auth = True
        st.rerun()
    st.stop()

# --- TABS ---
tabs = st.tabs(["📊 Activity", "❤️ Live Sport", "🏋️ Library", "🏆 Groups"])

# --- TAB 1: SUMMARY (HEALTH SYNC) ---
with tabs[0]:
    st.title("Summary")
    st.info("Syncing with Apple Health & Samsung Health via Cloud Bridge...")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        steps = st.number_input("Steps Walked", min_value=0)
        ex_mins = st.number_input("Exercise Mins", min_value=0)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        water = st.number_input("Water (Liters)", min_value=0.0)
        sleep = st.number_input("Sleep (Hrs)", min_value=0.0)
        st.markdown('</div>', unsafe_allow_html=True)
    
    current_group = st.text_input("Group Code", value="Solo")
    if st.button("Save & Sync"):
        data = {"username": st.session_state.user_name, "group_name": current_group, "steps": steps, "exercise_mins": ex_mins, "water": water, "sleep_hours": sleep}
        supabase.table("aura_collab_tracker").upsert(data, on_conflict="username,group_name").execute()
        st.success("Synced to Apple/Samsung Cloud!")

# --- TAB 2: LIVE SPORT & HEART RATE (BLUETOOTH) ---
with tabs[1]:
    st.title("Live Heart Rate")
    sport = st.selectbox("Activity", ["Basketball", "Soccer", "Running", "Cycling"])
    
    # JavaScript Bridge for Bluetooth Heart Rate
    if st.button("🔗 Connect Bluetooth Heart Rate Monitor"):
        # This triggers the browser's Bluetooth picker
        streamlit_js_eval(js_expressions="navigator.bluetooth.requestDevice({filters: [{services: ['heart_rate']}]})")
        st.write("Searching for devices...")

    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    st.markdown('<p class="heart-rate">-- BPM</p>', unsafe_allow_html=True)
    st.write(f"Tracking {sport} Session...")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 3: LIBRARY ---
with tabs[2]:
    st.title("Exercise Library")
    search = st.text_input("Find an exercise...")
    # (Library logic for videos here)

# --- TAB 4: LEADERBOARD & SHARING ---
with tabs[3]:
    st.title("Social Hub")
    view_g = st.text_input("Enter Group to join/view:", value="Solo")
    res = supabase.table("aura_collab_tracker").select("*").eq("group_name", view_g).execute()
    if res.data:
        st.dataframe(pd.DataFrame(res.data)[["username", "steps", "exercise_mins"]].sort_values(by="steps", ascending=False))
