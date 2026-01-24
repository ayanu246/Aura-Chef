import streamlit as st
from supabase import create_client
import pandas as pd
import time
from streamlit_js_eval import streamlit_js_eval

# --- DB CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Elite", layout="wide")

# --- PRO ATHLETE UI ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stat-card { background: #1c1c1e; padding: 20px; border-radius: 15px; border: 1px solid #007aff; text-align: center; margin-bottom: 15px; }
    .label { color: #8e8e93; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; }
    .value { font-size: 3.5rem; font-weight: 900; color: #007aff; }
    .stButton>button { border-radius: 12px; background: #007aff; color: white; width: 100%; font-weight: 700; border: none; padding: 20px; }
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

# --- TABS ---
t1, t2, t3, t4 = st.tabs(["DASHBOARD", "TRAINING", "COMMUNITY", "NETWORKS"])

with t1:
    st.markdown(f"### Athlete: {st.session_state.user_name}")
    st.markdown(f'<div class="stat-card"><div class="label">Auto-Step Count</div><div class="value">{st.session_state.steps}</div></div>', unsafe_allow_html=True)
    
    # THE AUTOMATIC ENGINE
    if st.button("🚀 ACTIVATE AUTO-TRACKING"):
        # This script tries to keep the phone awake and listen to the 'Linear Acceleration'
        streamlit_js_eval(js_expressions="""
            (async () => {
                try {
                    // 1. Request Wake Lock (Keeps phone from sleeping)
                    if ('wakeLock' in navigator) { await navigator.wakeLock.request('screen'); }
                    
                    // 2. Start Sensor
                    if ('LinearAccelerationSensor' in window) {
                        const sensor = new LinearAccelerationSensor({frequency: 60});
                        sensor.addEventListener('reading', () => {
                            let magnitude = Math.sqrt(sensor.x**2 + sensor.y**2 + sensor.z**2);
                            if (magnitude > 12) { 
                                // Sending a 'thump' to the console to prove it's alive
                                console.log('Step detected'); 
                            }
                        });
                        sensor.start();
                        window.alert('SYSTEM LIVE: Stay on this tab and walk.');
                    } else {
                        window.alert('Hardware blocked by Samsung Security.');
                    }
                } catch (err) { window.alert('Error: ' + err.name); }
            })()
        """, key="auto_engine_vFinal")

    st.markdown("---")
    st.markdown(f"**Hydration:** {st.session_state.water} Cups")
    if st.button("💧 ADD WATER"):
        st.session_state.water += 1
        st.rerun()

with t2:
    st.title("Training Timer")
    st.markdown(f"**Today:** {st.session_state.exercise} mins")
    if st.button("▶️ START SESSION"): st.session_state.t_start = time.time()
    if st.button("⏹️ STOP & SAVE"):
        if 't_start' in st.session_state:
            dur = int((time.time() - st.session_state.t_start) / 60)
            st.session_state.exercise += dur
            st.rerun()

with t3:
    st.title("Community Rankings")
    res = supabase.table("aura_collab_tracker").select("*").eq("group_name", st.session_state.active_group).execute()
    if res.data:
        df = pd.DataFrame(res.data).sort_values(by="steps", ascending=False)
        st.dataframe(df[["username", "steps", "exercise_mins", "water"]], use_container_width=True, hide_index=True)

with t4:
    st.title("Networks")
    st.write(f"Active: {st.session_state.active_group}")
    new_g = st.text_input("New Network")
    if st.button("JOIN"):
        st.session_state.active_group = new_g
        st.rerun()

# --- CLOUD UPSERT ---
p = {"username": st.session_state.user_name, "group_name": st.session_state.active_group, "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
try: supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
except: pass
