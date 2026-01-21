import streamlit as st
from supabase import create_client
import pandas as pd

# Connection (Already filled for you)
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Hub", layout="wide")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🏃‍♂️ Aura Hub")
    name = st.text_input("1. Your Name", placeholder="Enter your name...")
    st.divider()
    # This is the "Tabs on the side" you asked for
    menu = st.radio("2. Go to:", ["My Daily Tracker", "Join/Create a Group", "Leaderboard"])

# --- TAB 1: TRACKING ---
if menu == "My Daily Tracker":
    st.header(f"Logged in as: {name if name else 'New User'}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 Activity")
        steps = st.number_input("Steps Today", min_value=0, step=100)
        exercise = st.number_input("Workout Minutes", min_value=0)
        
    with col2:
        st.subheader("💧 Health")
        sleep = st.number_input("Sleep (Hours)", min_value=0.0, step=0.5)
        water = st.number_input("Water (Liters/Glasses)", min_value=0.0)

    # Allow user to pick which group they are saving to
    active_group = st.text_input("Save to Group Name:", value="Solo")

    if st.button("Save All Stats"):
        if name:
            data = {
                "username": name, 
                "group_name": active_group, 
                "steps": steps, 
                "sleep_hours": sleep,
                "water": water,
                "exercise_mins": exercise
            }
            supabase.table("aura_collab_tracker").upsert(data).execute()
            st.success(f"Stats synced to {active_group}!")
        else:
            st.error("Please enter your name in the sidebar first!")

# --- TAB 2: JOIN/CREATE ---
elif menu == "Join/Create a Group":
    st.header("👥 Group Management")
    
    t1, t2 = st.tabs(["Create/Join", "Invite Others"])
    
    with t1:
        st.subheader("Join a Group")
        st.write("Enter a group name below. If it doesn't exist, it will be created once you save stats to it.")
        group_name = st.text_input("Group Name:")
        if group_name:
            st.info(f"To join this group, go to 'My Daily Tracker' and set your group to: **{group_name}**")
            
    with t2:
        st.subheader("Share with Friends")
        share_code = st.text_input("Group Code to Share:")
        if share_code:
            msg = f"Join my Aura Hub group! Enter code '{share_code}' in the app."
            st.text_area("Copy this message:", value=msg)
            st.write(f"[Share via WhatsApp](https://wa.me/?text={msg})")

# --- TAB 3: LEADERBOARD ---
elif menu == "Leaderboard":
    st.header("🏆 Group Standings")
    view_group = st.text_input("Enter Group Name to see members:")
    
    if view_group:
        res = supabase.table("aura_collab_tracker").select("*").eq("group_name", view_group).execute()
        if res.data:
            df = pd.DataFrame(res.data)
            # This shows everyone who joined that specific group
            st.dataframe(df[["username", "steps", "sleep_hours", "water", "exercise_mins"]], use_container_width=True)
        else:
            st.warning("No data found for this group. Tell your friends to log some stats!")
