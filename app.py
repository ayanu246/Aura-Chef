import streamlit as st
from supabase import create_client
import pandas as pd
import time

# --- DB CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Elite", layout="wide")

# --- PRO UI ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stat-card { background: #1c1c1e; padding: 20px; border-radius: 15px; border: 1px solid #2c2c2e; margin-bottom: 10px; }
    .label { color: #8e8e93; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; }
    .value { font-size: 2.2rem; font-weight: 900; color: #007aff; }
    .stButton>button { border-radius: 8px; background: #007aff; color: white; width: 100%; font-weight: 700; border: none; padding: 12px; }
</style>
""", unsafe_allow_html=True)

# --- LOGIN ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("Aura Elite Athlete Login")
    u_in = st.text_input("Athlete ID", placeholder="Enter username...")
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

# --- TABS ---
t1, t2, t3, t4 = st.tabs(["DASHBOARD", "TRAINING", "COMMUNITY", "NETWORKS"])

with t1:
    st.markdown(f"### Athlete: {st.session_state.user_name}")
    st.markdown(f'<div class="stat-card"><div class="label">Move</div><div class="value">{st.session_state.steps}</div><div class="label">Steps</div></div>', unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    col_a.markdown(f'<div class="stat-card"><div class="label">Exercise</div><div class="value" style="color:#30d158">{st.session_state.exercise}m</div></div>', unsafe_allow_html=True)
    col_b.markdown(f'<div class="stat-card"><div class="label">Water</div><div class="value" style="color:#64d2ff">{st.session_state.water}</div></div>', unsafe_allow_html=True)

    if st.button("🔄 PING SYSTEM & SYNC"):
        st.info("Pinging Hardware Sensors...")
        p = {"username": st.session_state.user_name, "group_name": st.session_state.active_group, 
             "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
        try: 
            supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
            st.toast("Sync Success!")
        except: st.error("Cloud Error")

    if st.button("Add Water +1"):
        st.session_state.water += 1
        st.rerun()

# (Remaining tabs stay the same)
with t2:
    st.title("Training Timer")
    if st.button("START SESSION"): st.session_state.t_start = time.time()
    if st.button("STOP & SAVE"):
        if 't_start' in st.session_state:
            dur = int((time.time() - st.session_state.t_start) / 60)
            st.session_state.exercise += dur
            st.success(f"Added {dur} mins!")
            st.session_state.t_start = None

with t3:
    st.title("Leaderboard")
    try:
        res = supabase.table("aura_collab_tracker").select("*").eq("group_name", st.session_state.active_group).execute()
        if res.data:
            df = pd.DataFrame(res.data).sort_values(by="steps", ascending=False)
            st.dataframe(df[["username", "steps", "exercise_mins"]], use_container_width=True, hide_index=True)
    except: st.write("No data found.")

with t4:
    st.title("Networks")
    new_g = st.text_input("Switch Team Name")
    if st.button("JOIN"):
        st.session_state.active_group = new_g
        st.rerun()
