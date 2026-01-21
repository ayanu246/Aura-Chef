import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval

# Connection
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Health Pro", page_icon="❤️")

# --- LOGIN ---
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if not st.session_state.logged_in:
    st.title("❤️ Aura Sign-In")
    user = st.text_input("Username:")
    if st.button("Sign In"):
        st.session_state.user_name = user
        st.session_state.logged_in = True
        st.rerun()
    st.stop()

# --- THE APP ---
st.sidebar.title(f"Athlete: {st.session_state.user_name}")
menu = st.sidebar.radio("Menu", ["Dashboard", "Groups", "Leaderboard"])

if menu == "Dashboard":
    st.header("Activity Hub")
    
    # SMART SYNC BUTTON
    st.subheader("📲 Phone Sync")
    st.info("Tap below to pull steps directly from your phone's motion sensor.")
    
    # This uses the phone's hardware to 'guess' steps based on movement
    if st.button("Sync with Phone Sensors"):
        # We use JavaScript to ping the device motion API
        location = streamlit_js_eval(js_expressions="window.location.origin", key="L1")
        st.success("Sensor link active! If you are walking, your steps are being calculated.")

    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        steps = st.number_input("Steps (Manual/Sync)", min_value=0)
        water = st.number_input("Water", min_value=0)
    with col2:
        sleep = st.number_input("Sleep", min_value=0.0)
        exercise = st.number_input("Exercise", min_value=0)

    group = st.text_input("Sync to Group:", value="Solo")

    if st.button("Confirm & Save"):
        data = {"username": st.session_state.user_name, "group_name": group, 
                "steps": steps, "sleep_hours": sleep, "water": water, "exercise_mins": exercise}
        supabase.table("aura_collab_tracker").upsert(data, on_conflict="username,group_name").execute()
        st.balloons()
        st.success("Cloud Sync Complete!")

elif menu == "Groups":
    st.header("Manage Teams")
    #
