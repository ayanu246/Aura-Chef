import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import time

# --- DB CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Elite", layout="wide")

# --- UI STYLE ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stat-card { background: #1c1c1e; padding: 20px; border-radius: 15px; border: 1px solid #2c2c2e; margin-bottom: 15px; }
    .label { color: #8e8e93; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; }
    .value { font-size: 2.5rem; font-weight: 900; color: #007aff; }
    .stButton>button { border-radius: 10px; background: #007aff; color: white; width: 100%; font-weight: 700; border: none; padding: 20px; font-size: 1.2rem; }
</style>
""", unsafe_allow_html=True)

# --- LOGIN ---
if 'auth' not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.title("Aura Elite Athlete Login")
    u_in = st.text_input("Athlete ID")
    if st.button("AUTHENTICATE"):
        st.session_state.user_name = u_in
        st.session_state.auth = True
        st.session_state.steps, st.session_state.exercise, st.session_state.water = 0, 0, 0
        st.session_state.active_group = "Global"
        try:
            r = supabase.table("aura_collab_tracker").select("*").eq("username", u_in).execute()
            if r.data:
                st.session_state.steps = r.data[0].get('steps', 0)
                st.session_state.exercise = r.data[0].get('exercise_mins', 0)
                st.session_state.water = r.data[0].get('water', 0)
                st.session_state.active_group = r.data[0].get('group_name', 'Global')
        except: pass
        st.rerun()
    st.stop()

# --- DASHBOARD ---
t1, t2, t3, t4 = st.tabs(["DASHBOARD", "TRAINING", "COMMUNITY", "NETWORKS"])

with t1:
    st.markdown(f"### Athlete: {st.session_state.user_name}")
    
    st.markdown(f'<div class="stat-card"><div class="label">Total Steps</div><div class="value">{st.session_state.steps}</div></div>', unsafe_allow_html=True)
    
    # THE AUTOMATIC BRIDGE BUTTON
    if st.button("🛰️ SYNC AUTOMATIC STEPS"):
        st.warning("Connecting to Hardware Sensors...")
        # This script attempts to force the "Physical Activity" permission in Chrome
        streamlit_js_eval(js_expressions="""
            (async () => {
                try {
                    // Try the modern 'Physical Activity' API
                    if ('Accelerometer' in window) {
                        const acc = new Accelerometer({frequency: 10});
                        acc.start();
                        window.alert('AUTOMATIC TRACKING: ACTIVE');
                    } 
                    // Try the old 'DeviceMotion' API as a backup for Samsung
                    if (typeof DeviceMotionEvent.requestPermission === 'function') {
                        const response = await DeviceMotionEvent.requestPermission();
                        window.alert('Permission Status: ' + response);
                    }
                } catch (e) {
                    window.alert('SECURITY BLOCK: Open Chrome Settings > Site Settings > Motion Sensors > ALLOW');
                }
            })()
        """, key="auto_sync_bridge")
        
        # Update Database
        p = {"username": st.session_state.user_name, "group_name": st.session_state.active_group, 
             "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
        try: supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
        except: pass

    st.markdown("---")
    c1, c2 = st.columns(2)
    c1.markdown(f'<div class="stat-card"><div class="label">Exercise</div><div class="value" style="color:#30d158">{st.session_state.exercise}m</div></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="stat-card"><div class="label">Water</div><div class="value" style="color:#64d2ff">{st.session_state.water}</div></div>', unsafe_allow_html=True)
