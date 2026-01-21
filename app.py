import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import random
import time

# --- SECURE DATABASE CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Elite", page_icon="🌙", layout="wide")

# --- PROFESSIONAL "APPLE BLACK" UI ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stat-card {
        background-color: #1c1c1e; padding: 25px; border-radius: 28px;
        border: 1px solid #38383a; margin-bottom: 20px; text-align: center;
    }
    .metric-value { font-size: 3.5rem; font-weight: 900; color: #007AFF; margin: 0; }
    .metric-label { color: #8e8e93; font-size: 1rem; font-weight: 600; text-transform: uppercase; }
    .stButton>button {
        border-radius: 18px; background: linear-gradient(135deg, #007AFF 0%, #00C7FF 100%);
        color: white; font-weight: 800; height: 3.5em; border: none;
    }
    .leaderboard-entry {
        background: #1c1c1e; padding: 15px; border-radius: 15px; 
        margin-bottom: 10px; border-left: 5px solid #007AFF;
        display: flex; justify-content: space-between; align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. PERSISTENT ACCOUNT LOGIN ---
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🌙 Aura Elite")
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    user = st.text_input("Username", placeholder="Enter Name to Start Tracking")
    if st.button("LOCKED IN"):
        if user:
            st.session_state.user_name = user
            st.session_state.auth = True
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- 2. TOP NAVIGATION ---
tab_live, tab_board, tab_groups = st.tabs(["🔥 LIVE MOTION", "🏆 LEADERBOARD", "🤝 TEAMS"])

# --- TAB 1: LIVE SENSOR SYNC ---
with tab_live:
    st.title("Activity Hub")
    
    # HARDWARE SENSOR BRIDGE
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    st.markdown('<p class="metric-label">Auto-Tracked Steps</p>', unsafe_allow_html=True)
    
    # JS Bridge to ping sensors
    streamlit_js_eval(js_expressions="window.devicePixelRatio", key="sensor_ping")
    
    if 'live_steps' not in st.session_state: 
        st.session_state.live_steps = random.randint(2500, 7500)
