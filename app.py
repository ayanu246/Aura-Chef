import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import time

# --- DATABASE ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Elite", layout="wide")

# --- UI ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stat-card { background: #1c1c1e; padding: 20px; border-radius: 15px; border: 1px solid #007aff; text-align: center; }
    .value { font-size: 3.5rem; font-weight: 900; color: #007aff; }
    .stButton>button { border-radius: 12px; background: #007aff; color: white; width: 100%; font-weight: 700; height: 3em; }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("Aura Elite")
    u_in = st.text_input("Athlete ID")
    if st.button("LOGIN"):
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
    
    # THE MAIN COUNTER
    st.markdown(f'<div class="stat-card"><div style="color:#8e8e93">AUTOMATIC MOVE COUNT</div><div class="value">{st.session_state.steps}</div></div>', unsafe_allow_html=True)
    
    st.write(" ")
    
    # THE ENGINE START BUTTON
    # This script is the only way to bypass the Samsung sensor lock
    if st.button("🚀 ACTIVATE AUTO-SENSORS"):
        streamlit_js_eval(js_expressions="""
            (async () => {
                if (window.DeviceMotionEvent) {
                    window.addEventListener('devicemotion', (event) => {
                        let acc = event.accelerationIncludingGravity;
                        let total = Math.sqrt(acc.x**2 + acc.y**2 + acc.z**2);
                        // If phone 'bounces' (step taken), send signal
                        if (total > 13) { 
                            console.log('MOTION_DETECTED');
                        }
                    }, true);
                    window.alert('SENSORS LIVE: Keep this screen on and walk.');
                } else {
                    window.alert('Error: Sensor hardware not found or blocked.');
                }
            })()
        """, key="accel_bridge")

    # WATER LOG
    st.markdown(f"**Hydration:** {st.session_state.water} Cups")
    if st.button("Add Water"):
        st.session_state.water += 1
        st.rerun()

with t2:
    st.title("Exercise Timer")
    if st.button("START TIMER"): st.session_state.t_start = time.time()
    if st.button("STOP & SAVE"):
        if 't_start' in st.session_state:
            dur = int((time.time() - st.session_state.t_start) / 60)
            st.session_state.exercise += dur
            st.rerun()

with t3:
    st.title("Leaderboard")
    res = supabase.table("aura_collab_tracker").select("*").eq("group_name", st.session_state.active_group).execute()
    if res.data:
        df = pd.DataFrame(res.data).sort_values(by="steps", ascending=False)
        st.dataframe(df[["username", "steps", "exercise_mins"]], use_container_width=True, hide_index=True)

with t4:
    st.title("Networks")
    new_g = st.text_input("Network Name")
    if st.button("JOIN"):
        st.session_state.active_group = new_g
        st.rerun()

# --- AUTO-SYNC TO DATABASE ---
p = {"username": st.session_state.user_name, "group_name": st.session_state.active_group, "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
try: supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
except: pass
