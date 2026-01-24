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

# --- PRO ATHLETE UI ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stat-card { background: #1c1c1e; padding: 20px; border-radius: 15px; border: 1px solid #2c2c2e; margin-bottom: 15px; }
    .label { color: #8e8e93; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; }
    .value { font-size: 2.8rem; font-weight: 900; color: #007aff; }
    .stButton>button { border-radius: 12px; background: #007aff; color: white; width: 100%; font-weight: 700; border: none; padding: 18px; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #1c1c1e; border-radius: 10px 10px 0 0; color: white; padding: 10px 20px; }
</style>
""", unsafe_allow_html=True)

# --- LOGIN LOGIC ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("Aura Elite Athlete Login")
    u_in = st.text_input("Athlete ID", placeholder="Enter your username...")
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

# --- APP TABS ---
t1, t2, t3, t4 = st.tabs(["DASHBOARD", "TRAINING", "COMMUNITY", "NETWORKS"])

# --- TAB 1: DASHBOARD (Steps & Water) ---
with t1:
    st.markdown(f"### Athlete: {st.session_state.user_name}")
    
    st.markdown(f'<div class="stat-card"><div class="label">Total Steps</div><div class="value">{st.session_state.steps}</div></div>', unsafe_allow_html=True)
    
    # SENSOR ACTIVATOR
    if st.button("🛰️ ACTIVATE AUTO-TRACKING"):
        st.info("Bridge Online. Keep this tab open in your pocket.")
        streamlit_js_eval(js_expressions="""
            (async () => {
                if ('LinearAccelerationSensor' in window) {
                    const sensor = new LinearAccelerationSensor({frequency: 10});
                    sensor.addEventListener('reading', () => {
                        let mag = Math.sqrt(sensor.x**2 + sensor.y**2 + sensor.z**2);
                        if (mag > 12) { console.log('Movement Detected'); }
                    });
                    sensor.start();
                    window.alert('Sensors Engaged. Movement is being tracked.');
                }
            })()
        """, key="accel_vfinal")

    # WATER TRACKER
    st.markdown(f'<div class="stat-card"><div class="label">Hydration</div><div class="value" style="color:#64d2ff">{st.session_state.water} <span style="font-size:1rem">Cups</span></div></div>', unsafe_allow_html=True)
    if st.button("💧 LOG WATER +1"):
        st.session_state.water += 1
        st.rerun()

# --- TAB 2: TRAINING (Exercise Timer) ---
with t2:
    st.markdown(f'<div class="stat-card"><div class="label">Daily Exercise</div><div class="value" style="color:#30d158">{st.session_state.exercise}m</div></div>', unsafe_allow_html=True)
    
    if 't_start' not in st.session_state: st.session_state.t_start = None
    
    c1, c2 = st.columns(2)
    if c1.button("▶️ START SESSION"):
        st.session_state.t_start = time.time()
        st.toast("Session Clock Started!")
        
    if c2.button("⏹️ STOP & SAVE"):
        if st.session_state.t_start:
            dur = int((time.time() - st.session_state.t_start) / 60)
            st.session_state.exercise += dur
            st.session_state.t_start = None
            st.success(f"Added {dur} minutes to your daily total!")
            time.sleep(1)
            st.rerun()

# --- TAB 3: COMMUNITY (Leaderboard) ---
with t3:
    st.title("Network Rankings")
    try:
        res = supabase.table("aura_collab_tracker").select("*").eq("group_name", st.session_state.active_group).execute()
        if res.data:
            df = pd.DataFrame(res.data).sort_values(by="steps", ascending=False)
            st.dataframe(df[["username", "steps", "exercise_mins", "water"]], use_container_width=True, hide_index=True)
    except: st.write("Searching for teammates...")

# --- TAB 4: NETWORKS (Group Switching) ---
with t4:
    st.title("Network Hub")
    st.write(f"Current Network: **{st.session_state.active_group}**")
    new_g = st.text_input("Enter New Network Name")
    if st.button("JOIN NETWORK"):
        st.session_state.active_group = new_g
        st.success(f"Switched to {new_g}")
        st.rerun()

# --- GLOBAL SYNC (Saves everything to the cloud automatically) ---
p = {
    "username": st.session_state.user_name, 
    "group_name": st.session_state.active_group, 
    "steps": st.session_state.steps, 
    "exercise_mins": st.session_state.exercise, 
    "water": st.session_state.water
}
try: supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
except: pass
