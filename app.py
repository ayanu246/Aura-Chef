import streamlit as st
from supabase import create_client
import pandas as pd
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
    .stat-card { background: #1c1c1e; padding: 20px; border-radius: 15px; border: 1px solid #2c2c2e; margin-bottom: 15px; text-align: center; }
    .label { color: #8e8e93; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
    .value { font-size: 3rem; font-weight: 900; color: #007aff; margin: 10px 0; }
    .stButton>button { border-radius: 12px; background: #007aff; color: white; width: 100%; font-weight: 700; border: none; padding: 18px; font-size: 1.1rem; }
    .stNumberInput input { background-color: #1c1c1e !important; color: white !important; border: 1px solid #2c2c2e !important; font-size: 1.5rem !important; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- LOGIN LOGIC ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("Aura Elite Athlete Login")
    u_in = st.text_input("Athlete ID", placeholder="Username...")
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

# --- TAB 1: DASHBOARD ---
with t1:
    st.markdown(f"### Athlete: {st.session_state.user_name}")
    
    st.markdown(f'<div class="stat-card"><div class="label">Cloud Total</div><div class="value">{st.session_state.steps}</div><div class="label">Steps Synced</div></div>', unsafe_allow_html=True)
    
    # SMART-MANUAL SYNC
    st.markdown("### 🏃 Quick Step Sync")
    st.caption("Check your phone's lock screen or Samsung Health and enter your total steps below.")
    daily_total = st.number_input("Enter Current Total Steps", min_value=0, value=st.session_state.steps, step=100)
    
    if st.button("🚀 SYNC TO LEADERBOARD"):
        st.session_state.steps = daily_total
        # Global Sync Trigger
        p = {"username": st.session_state.user_name, "group_name": st.session_state.active_group, 
             "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
        try: 
            supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
            st.success("Leaderboard Updated!")
            time.sleep(1)
            st.rerun()
        except: st.error("Database connection issue.")

    st.markdown("---")
    
    # WATER TRACKER
    st.markdown(f'<div class="stat-card"><div class="label">Hydration</div><div class="value" style="color:#64d2ff">{st.session_state.water} <span style="font-size:1.2rem">Cups</span></div></div>', unsafe_allow_html=True)
    if st.button("💧 LOG WATER +1"):
        st.session_state.water += 1
        st.rerun()

# --- TAB 2: TRAINING ---
with t2:
    st.title("Session Timer")
    st.markdown(f'<div class="stat-card"><div class="label">Daily Exercise</div><div class="value" style="color:#30d158">{st.session_state.exercise}m</div></div>', unsafe_allow_html=True)
    
    if 't_start' not in st.session_state: st.session_state.t_start = None
    
    if not st.session_state.t_start:
        if st.button("▶️ START SESSION"):
            st.session_state.t_start = time.time()
            st.rerun()
    else:
        st.info("Timer is running...")
        if st.button("⏹️ STOP & SAVE"):
            dur = int((time.time() - st.session_state.t_start) / 60)
            st.session_state.exercise += dur
            st.session_state.t_start = None
            st.rerun()

# --- TAB 3: COMMUNITY ---
with t3:
    st.title("Network Rankings")
    try:
        res = supabase.table("aura_collab_tracker").select("*").eq("group_name", st.session_state.active_group).execute()
        if res.data:
            df = pd.DataFrame(res.data).sort_values(by="steps", ascending=False)
            st.dataframe(df[["username", "steps", "exercise_mins", "water"]], use_container_width=True, hide_index=True)
    except: st.write("Loading leaderboard...")

# --- TAB 4: NETWORKS ---
with t4:
    st.title("Join a Network")
    st.write(f"Active Network: **{st.session_state.active_group}**")
    new_g = st.text_input("Network Name")
    if st.button("SWITCH"):
        st.session_state.active_group = new_g
        st.rerun()
