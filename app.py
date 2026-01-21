import streamlit as st
from supabase import create_client
import pandas as pd
import random

# --- DATABASE CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

# --- PROFESSIONAL THEMING ---
st.set_page_config(page_title="Aura Pro", page_icon="🌙", layout="wide")

# Custom CSS for the "Black/Professional" Apple look
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #1c1c1e; }
    .stat-card {
        background-color: #1c1c1e;
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #38383a;
        margin-bottom: 10px;
    }
    h1, h2, h3 { color: #ffffff !important; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    .stButton>button {
        border-radius: 12px;
        background-image: linear-gradient(to right, #007AFF, #00C7FF);
        color: white;
        border: none;
        font-weight: bold;
        height: 3em;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ACCOUNT SYSTEM (PERSISTENT) ---
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🌙 Aura Health")
    st.subheader("Professional Grade Fitness Tracking")
    with st.container():
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        user = st.text_input("Username", placeholder="Enter your unique name...")
        if st.button("Sign In / Create Account"):
            if user:
                st.session_state.user_name = user
                st.session_state.auth = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- TOP NAVIGATION BAR ---
tabs = st.tabs(["📊 Summary", "👥 Sharing & Groups", "🏆 Leaderboard"])

# --- TAB 1: SUMMARY (DASHBOARD) ---
with tabs[0]:
    st.title("Summary")
    st.write(f"Logged in as: **{st.session_state.user_name}**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="stat-card"><h3>🏃 Activity</h3>', unsafe_allow_html=True)
        steps = st.number_input("Steps", min_value=0, step=500)
        exercise = st.number_input("Exercise (Min)", min_value=0)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="stat-card"><h3>💧 Health</h3>', unsafe_allow_html=True)
        water = st.number_input("Water (Cups)", min_value=0)
        sleep = st.number_input("Sleep (Hrs)", min_value=0.0, step=0.5)
        st.markdown('</div>', unsafe_allow_html=True)

    active_group = st.text_input("Active Group Code (Default: Solo)", value="Solo")

    if st.button("Sync with Cloud"):
        data = {
            "username": st.session_state.user_name,
            "group_name": active_group,
            "steps": steps, "sleep_hours": sleep,
            "water": water, "exercise_mins": exercise
        }
        supabase.table("aura_collab_tracker").upsert(data, on_conflict="username,group_name").execute()
        st.success("Cloud Synchronized")
        st.balloons()

# --- TAB 2: SHARING & GROUPS ---
with tabs[1]:
    st.title("Sharing")
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Create a Group")
        g_name = st.text_input("Group Name")
        if st.button("Generate Pro Code"):
            code = f"{g_name.upper()}-{random.randint(100, 999)}"
            st.code(code)
            st.write(f"[Share on WhatsApp](https://wa.me/?text=Join%20my%20Aura%20Group!%20Code:%20{code})")
    
    with c2:
        st.subheader("Join a Group")
        join_code = st.text_input("Enter Invite Code")
        if st.button("Link Account to Group"):
            st.success(f"Linked to {join_code}. Now sync your Dashboard!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 3: LEADERBOARD ---
with tabs[2]:
    st.title("Trends")
    view_code = st.text_input("Enter Group Code to view:", value="Solo")
    
    res = supabase.table("aura_collab_tracker").select("*").eq("group_name", view_code).execute()
    if res.data:
        df = pd.DataFrame(res.data)
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        st.dataframe(df[["username", "steps", "exercise_mins"]].sort_values(by="steps", ascending=False), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No data for this group yet.")

# --- SIDEBAR (SIGN OUT) ---
st.sidebar.markdown("### Profile Settings")
if st.sidebar.button("Log Out"):
    st.session_state.auth = False
    st.rerun()
