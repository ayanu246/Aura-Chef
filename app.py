import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import time

# --- 1. DB CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="Aura Elite", layout="wide")

# --- 3. PRO UI STYLING ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Helvetica Neue', sans-serif; }
    .stat-card { background: #1c1c1e; padding: 25px; border-radius: 15px; border: 1px solid #2c2c2e; text-align: left; }
    .label { color: #8e8e93; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
    .value { font-size: 2.5rem; font-weight: 900; color: #007aff; margin: 5px 0; }
    .stButton>button { border-radius: 8px; background: #007aff; color: white; border: none; font-weight: 600; width: 100%; padding: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 4. AUTHENTICATION (WITH CRASH PROTECTION) ---
if 'auth' not in st.session_state: 
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("Aura Elite Athlete Login")
    u_in = st.text_input("Athlete ID", placeholder="Enter username...")
    if st.button("AUTHENTICATE"):
        if u_in:
            st.session_state.user_name = u_in
            st.session_state.auth = True
            # Set absolute defaults first to prevent black screen
            st.session_state.steps = 0
            st.session_state.exercise = 0
            st.session_state.water = 0
            st.session_state.active_group = "Global"
            
            try:
                r = supabase.table("aura_collab_tracker").select("*").eq("username", u_in).execute()
                if r.data:
                    st.session_state.steps = r.data[0].get('steps', 0)
                    st.session_state.exercise = r.data[0].get('exercise_mins', 0)
                    st.session_state.water = r.data[0].get('water', 0)
                    st.session_state.active_group = r.data[0].get('group_name', 'Global')
            except Exception as e:
                pass # Defaults are already set, so app will still load
            st.rerun()
    st.stop()

# --- 5. RE-VERIFY STATE EXISTS ---
for k, v in {"steps": 0, "water": 0, "exercise": 0, "active_group": "Global"}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- 6. MAIN NAVIGATION TABS ---
t1, t2, t3, t4 = st.tabs(["DASHBOARD", "TRAINING", "COMMUNITY", "NETWORKS"])

with t1:
    st.markdown(f"### Athlete: {st.session_state.user_name}")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="stat-card"><div class="label">Move</div><div class="value">{st.session_state.steps}</div><div class="label">Steps</div></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="stat-card"><div class="label">Exercise</div><div class="value" style="color:#30d158">{st.session_state.exercise}</div><div class="label">Mins</div></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="stat-card"><div class="label">Hydration</div><div class="value" style="color:#64d2ff">{st.session_state.water}</div><div class="label">Glasses</div></div>', unsafe_allow_html=True)

    if st.button("ACTIVATE CHROME HEALTH BRIDGE"):
        st.warning("Pinging System Health Sensors...")
        streamlit_js_eval(js_expressions="""
            (async () => {
                try {
                    if ('Accelerometer' in window) {
                        const acc = new Accelerometer({frequency: 10});
                        acc.start();
                        window.alert('Handshake Sent.');
                    } else {
                        window.alert('Check Chrome Settings > Site Settings > Motion Sensors.');
                    }
                } catch (e) { console.log(e); }
            })()
        """, key="chrome_sync_final")
        
        p = {
            "username
