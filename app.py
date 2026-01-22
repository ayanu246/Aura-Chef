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
st.markdown("<style>.stApp{background:#000;color:#fff}.stat-card{background:#1c1c1e;padding:15px;border-radius:20px;border:1px solid #2c2c2e;text-align:center}.metric-val{font-size:1.8rem;font-weight:800;color:#007aff}</style>", unsafe_allow_html=True)

# --- 1. LOGIN & RESTORE ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🌙 Aura Elite")
    u_in = st.text_input("Athlete Username")
    if st.button("LOCKED IN"):
        if u_in:
            st.session_state.user_name = u_in
            st.session_state.auth = True
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

# --- INIT DEFAULTS ---
if 'steps' not in st.session_state: st.session_state.steps = 0
if 'water' not in st.session_state: st.session_state.water = 0
if 'exercise' not in st.session_state: st.session_state.exercise = 0
if 'active_group' not in st.session_state: st.session_state.active_group = "Global"

# --- TABS ---
t1, t2, t3, t4 = st.tabs(["📊 Activity", "⚽ Sport", "🏆 Leaderboard", "🤝 Groups"])

with t1:
    st.header(f"Athlete: {st.session_state.user_name}")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="stat-card"><p>MOVE</p><p class="metric-val">{st.session_state.steps}</p></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="stat-card"><p style="color:#30d158">EXERCISE</p><p class="metric-val" style="color:#30d158">{st.session_state.exercise}</p></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="stat-card"><p style="color:#64d2ff">WATER</p><p class="metric-val" style="color:#64d2ff">{st.session_state.water}</p></div>', unsafe_allow_html=True)

    if st.button("🔄 SYNC & SAVE"):
        streamlit_js_eval(js_expressions="window.devicePixelRatio", key="sync")
        p = {"username": st.session_state.user_name, "group_name": st.session_state.active_group, "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
        supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
        st.toast("Saved!")

    if st.button("💧 Drink Water"):
        st.session_state.water += 1
        st.rerun()

with t2:
    st.title("Sport Timer")
    sport = st.selectbox("Sport", ["Basketball", "Soccer", "Gym"])
    if 't_start' not in st.session_state: st.session_state.t_start = None
    if st.button("▶️ START"): st.session_state.t_start = time.time()
    if st.button("⏹️ STOP"):
        if st.session_state.t_start:
            dur = int((time.time() - st.session_state.t_start) / 60)
            st.session_state.exercise += dur
            st.session_state.t_start = None
            st.success(f"Added {dur} mins!")

with t3:
    st.title(f"🏆 {st.session_state.active_group} Ranks")
    res = supabase.table("aura_collab_tracker").select("*").eq("group_name", st.session_state.active_group).execute()
    if res.data:
        df = pd.DataFrame(res.data).sort_values(by="steps", ascending=False)
        st.dataframe(df[["username", "steps", "exercise_mins"]], hide_index=True)

with t4:
    st.title("Groups")
    new_g = st.text_input("Group Code", value=st.session_state.active_group)
    if st.button("JOIN TEAM"):
        st.session_state.active_group = new_g
        st.rerun()
