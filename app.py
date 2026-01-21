import streamlit as st
from supabase import create_client
import pandas as pd
import random
import string

# Connection
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Health", page_icon="❤️", layout="centered")

# Custom Apple-style CSS
st.markdown("""
    <style>
    .main { background-color: #f2f2f7; }
    .stButton>button { border-radius: 20px; background-color: #007aff; color: white; width: 100%; }
    .stat-card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- APP LOGIC ---
if 'user_name' not in st.session_state: st.session_state.user_name = ""
if 'group_code' not in st.session_state: st.session_state.group_code = "Solo"

# SIDEBAR: The "Profile" section
with st.sidebar:
    st.title("Settings")
    st.session_state.user_name = st.text_input("Your Name", value=st.session_state.user_name)
    st.write(f"**Current Group:** {st.session_state.group_code}")
    menu = st.radio("Menu", ["Summary", "Sharing", "Trends"])

# --- TAB 1: SUMMARY (Apple Health Style) ---
if menu == "Summary":
    st.title("Summary")
    st.subheader(f"How are you doing, {st.session_state.user_name}?")
    
    # Activity Card
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        steps = st.number_input("Steps", min_value=0, step=100)
        dist = st.caption(f"Approx: {round(steps * 0.0008, 2)} km")
    with col2:
        exercise = st.number_input("Exercise (Min)", min_value=0)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("") # Spacer

    # Health Card
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        sleep = st.number_input("Sleep (Hrs)", min_value=0.0, step=0.5)
    with col4:
        water = st.number_input("Water (Cups)", min_value=0)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Log Daily Activity"):
        if st.session_state.user_name:
            data = {
                "username": st.session_state.user_name,
                "group_name": st.session_state.group_code,
                "steps": steps, "sleep_hours": sleep,
                "water": water, "exercise_mins": exercise
            }
            supabase.table("aura_collab_tracker").upsert(data).execute()
            st.success("Activity Saved to Cloud!")

# --- TAB 2: SHARING (The Group System) ---
elif menu == "Sharing":
    st.title("Sharing")
    
    tab_join, tab_create = st.tabs(["Join a Group", "Create New Group"])
    
    with tab_join:
        st.write("Enter the code a friend sent you:")
        input_code = st.text_input("Group Code", placeholder="e.g. AURA-77")
        if st.button("Join Team"):
            st.session_state.group_code = input_code
            st.success(f"Joined {input_code}!")

    with tab_create:
        st.write("Start a new private group:")
        new_name = st.text_input("Give your group a name:")
        if st.button("Generate Group Code"):
            # Generates a 4-digit code like "AURA-1234"
            random_code = f"{new_name.upper()}-{random.randint(1000, 9999)}"
            st.session_state.group_code = random_code
            st.write("### Your New Group Code:")
            st.code(random_code)
            
            # Universal Share Link
            msg = f"Join my Aura Health group! Open the app and use code: {random_code}"
            st.write(f"[Share via WhatsApp](https://wa.me/?text={msg})")
            st.write(f"[Share via Email](mailto:?subject=Join%20My%20Group&body={msg})")

# --- TAB 3: TRENDS (Leaderboard) ---
elif menu == "Trends":
    st.title("Group Trends")
    st.write(f"Viewing stats for: **{st.session_state.group_code}**")
    
    res = supabase.table("aura_collab_tracker").select("*").eq("group_name", st.session_state.group_code).execute()
    if res.data:
        df = pd.DataFrame(res.data)
        st.dataframe(df[["username", "steps", "exercise_mins", "sleep_hours"]], use_container_width=True)
    else:
        st.info("No data in this group yet. Go to 'Sharing' to invite friends!")
