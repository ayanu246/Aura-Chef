import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import time

# --- 1. CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

# --- 2. CONFIG & UI ---
st.set_page_config(page_title="Aura Elite", layout="wide")
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Helvetica Neue', sans-serif; }
    .stat-card { background: #1c1c1e; padding: 25px; border-radius: 15px; border: 1px solid #2c2c2e; text-align: left; }
    .label { color: #8e8e93; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
    .value { font-size: 2.5rem; font-weight: 900; color: #007aff; margin: 5px 0; }
    .stButton>button { border-radius: 8px; background: #007aff; color: white; border: none; font-weight: 600; width: 100%; padding: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 3. AUTHENTICATION ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("Aura Elite Athlete Login")
    u_in = st.text_input("Athlete ID", placeholder="Enter username...")
    if st.button("AUTHENTICATE"):
        if u_in:
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
            except Exception: pass
            st.rerun()
    st.stop()

# --- 4. TABS ---
t1, t2, t3, t4 = st.tabs(["DASHBOARD", "TRAINING", "COMMUNITY", "NETWORKS"])

with t1:
    st.markdown(f"### Athlete: {st.session_state.user_name}")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="stat-card"><div class="label">Move</div><div class="value">{st.session_state.steps}</div><div class="label">Steps</div></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="stat-card"><div class="label">Exercise</div><div class="value" style="color:#30d158">{st.session_state.exercise}</div><div class="label">Mins</div></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="stat-card"><div class="label">Hydration</div><div class="value" style="color:#64d2ff">{st.session_state.water}</div><div class="label">Glasses</div></div>', unsafe_allow_html=True)

    if st.button("ACTIVATE HEALTH BRIDGE"):
        st.warning("Pinging System Health Sensors...")
        # --- FIXED JS BLOCK ---
        streamlit_js_eval(js_expressions="""(async () => { try { if ('Accelerometer' in window) { const acc = new Accelerometer({frequency: 10}); acc.start(); window.alert('Bridge Active'); } else { window.alert('Enable Motion Sensors in Chrome Settings'); } } catch (e) { console.log(e); } })()""", key="chrome_sync_final")
        
        p = {"username": st.session_state.user_name, "group_name": st.session_state.active_group, "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
        try: supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
        except Exception: pass

    if st.button("Log Water"):
        st.session_state.water += 1
        st.rerun()

with t2:
    st.title("Training Session")
    s_list = ["Basketball", "Soccer", "Gym", "Boxing", "Swimming", "Tennis"]
    sport = st.selectbox("Select Activity", s_list)
    if 't_start' not in st.session_state: st.session_state.t_start = None
    if st.button("START"): st.session_state.t_start = time.time()
    if st.button("STOP & SAVE"):
        if st.session_state.t_start:
            dur = int((time.time() - st.session_state.t_start) / 60)
            st.session_state.exercise += dur
            st.session_state.t_start = None
            p = {"username": st.session_state.user_name, "group_name": st.session_state.active_group, "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
            try: supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
            except Exception: pass
            st.rerun()

with t3:
    st.title("Community Rankings")
    try:
        all_g_res = supabase.table("aura_collab_tracker").select("group_name").execute()
        g_list = sorted(list(set([x['group_name'] for x in all_g_res.data])))
    except Exception: g_list = [st.session_state.active_group]
    view_g = st.selectbox("Leaderboard View", g_list, index=g_list.index(st.session_state.active_group) if st.session_state.active_group in g_list else 0)
    res = supabase.table("aura_collab_tracker").select("*").eq("group_name", view_g).execute()
    if res.data:
        df = pd.DataFrame(res.data).sort_values(by="steps", ascending=False)
        st.dataframe(df[["username", "steps", "exercise_mins"]], use_container_width=True, hide_index=True)

with t4:
    st.title("Networks")
    new_g = st.text_input("New or Existing Group Name")
    if st.button("LOCK IN TEAM"):
        if new_g:
            st.session_state.active_group = new_g
            p = {"username": st.session_state.user_name, "group_name": new_g, "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
            try: supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
            except Exception: pass
            st.rerun()
