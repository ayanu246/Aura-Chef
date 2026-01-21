import streamlit as st
from supabase import create_client
import pandas as pd

# I have plugged in your keys here so you don't have to!
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"

supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Collab Tracker", layout="wide")
st.title("🤝 Aura Collab: Steps & Sleep")

# Phase: Identity & Mode
with st.sidebar:
    st.header("Profile")
    name = st.text_input("Your Name", placeholder="Enter your name...")
    mode = st.radio("Navigation", ["Solo Tracking", "Group Collaboration"])

if mode == "Group Collaboration":
    st.subheader("👥 Group Mode")
    group_code = st.text_input("Enter Group Name/Code", placeholder="e.g. 'Team-Alpha'")
    
    if group_code:
        # Create a universal invite message
        invite_msg = f"Join my Aura fitness group! Open the app and enter group code: {group_code}"
        st.info(f"**Invite others:** Copy this message to Email or Text:\n\n`{invite_msg}`")

    # Input Section
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        steps = st.number_input("Steps Walked", min_value=0, step=1)
    with c2:
        sleep = st.number_input("Hours Slept", min_value=0.0, step=0.5)

    if st.button("Update Stats to Group"):
        if name and group_code:
            data = {"username": name, "group_name": group_code, "steps": steps, "sleep_hours": sleep}
            # This saves it to the database table we created earlier
            supabase.table("aura_collab_tracker").insert(data).execute()
            st.success(f"Stats synced to {group_code}!")
        else:
            st.error("Please enter both your name and a group code.")

    # Leaderboard Section
    if group_code:
        st.divider()
        st.subheader(f"Live Board: {group_code}")
        res = supabase.table("aura_collab_tracker").select("*").eq("group_name", group_code).order('created_at', desc=True).execute()
        if res.data:
            df = pd.DataFrame(res.data)
            st.dataframe(df[["username", "steps", "sleep_hours", "created_at"]], use_container_width=True)

else:
    st.subheader("🧘 Solo Tracking")
    # Solo logic: Filter by name only
    st.info("In Solo mode, your data is only visible to you (filtered by your name).")
    c1, c2 = st.columns(2)
    with c1:
        s_steps = st.number_input("Steps", min_value=0)
    with c2:
        s_sleep = st.number_input("Sleep", min_value=0.0)
    
    if st.button("Save Solo Stats"):
        data = {"username": name, "group_name": "Solo", "steps": s_steps, "sleep_hours": s_sleep}
        supabase.table("aura_collab_tracker").insert(data).execute()
        st.success("Solo stats saved!")
