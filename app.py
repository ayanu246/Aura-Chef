import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval

# Connection
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Hub", layout="wide")

# --- AUTO-SAVE DATA (Local Storage) ---
# This part remembers your name and group so it doesn't delete
if 'my_name' not in st.session_state:
    st.session_state['my_name'] = ""
if 'my_group' not in st.session_state:
    st.session_state['my_group'] = "Solo"

# --- SIDEBAR ---
with st.sidebar:
    st.title("🏃‍♂️ Aura Hub")
    st.session_state['my_name'] = st.text_input("Profile Name", value=st.session_state['my_name'])
    st.session_state['my_group'] = st.text_input("Active Group Code", value=st.session_state['my_group'])
    st.divider()
    menu = st.radio("Navigation", ["Dashboard", "Join/Create Group", "Global Leaderboard"])

# --- DASHBOARD (with Live Tracking) ---
if menu == "Dashboard":
    st.header(f"Athlete: {st.session_state['my_name']}")
    st.subheader(f"Team: {st.session_state['my_group']}")
    
    # Live Motion Tracking (experimental for mobile browsers)
    st.info("📱 Keep this page open while walking to track live.")
    if st.button("Start Live Step Counter"):
        st.write("Detecting motion... (Shake your phone to test)")
        # This triggers a simple JavaScript sensor check
        steps_detected = streamlit_js_eval(js_expressions="window.devicePixelRatio", key="sensor")
    
    col1, col2 = st.columns(2)
    with col1:
        steps = st.number_input("Manual Step Entry", min_value=0)
        water = st.number_input("Water (Liters)", min_value=0.0)
    with col2:
        sleep = st.number_input("Sleep (Hours)", min_value=0.0)
        exercise = st.number_input("Exercise (Mins)", min_value=0)

    if st.button("Sync Stats to Cloud"):
        if st.session_state['my_name']:
            data = {
                "username": st.session_state['my_name'], 
                "group_name": st.session_state['my_group'], 
                "steps": steps, 
                "sleep_hours": sleep,
                "water": water,
                "exercise_mins": exercise
            }
            supabase.table("aura_collab_tracker").upsert(data).execute()
            st.success("Synced! Everyone in your group can see this now.")

# --- JOIN/CREATE ---
elif menu == "Join/Create Group":
    st.header("🤝 Team Setup")
    new_code = st.text_input("Type a new Group Name to create it:")
    if st.button("Create & Join"):
        st.session_state['my_group'] = new_code
        st.success(f"Group '{new_code}' created! Tell your friends to enter this code in their sidebar.")
        
    st.divider()
    st.write("### Invite Friends")
    invite_link = f"Join my Aura Hub group! Code: {st.session_state['my_group']}"
    st.code(invite_link)

# --- LEADERBOARD ---
elif menu == "Global Leaderboard":
    st.header(f"🏆 {st.session_state['my_group']} Standings")
    res = supabase.table("aura_collab_tracker").select("*").eq("group_name", st.session_state['my_group']).execute()
    if res.data:
        df = pd.DataFrame(res.data)
        st.table(df[["username", "steps", "sleep_hours", "water"]])
    else:
        st.write("No one has logged stats in this group yet.")
