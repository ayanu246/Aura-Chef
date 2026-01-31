import streamlit as st
import random
import time

# --- GAME ENGINE CONFIG ---
st.set_page_config(page_title="NEON SYNDICATE", page_icon="⚡", layout="wide")

# Custom CSS for a "Gamer" UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    html, body, [class*="st-"] { 
        background-color: #050505; 
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }
    
    .game-header {
        font-family: 'Orbitron', sans-serif;
        color: #34d399;
        text-align: center;
        letter-spacing: 5px;
        text-shadow: 0 0 20px rgba(52, 211, 153, 0.5);
    }
    
    .stat-card {
        background: #0a0a0a;
        border: 1px solid #1f1f1f;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
    }
    
    .terminal-box {
        background: #000;
        border-left: 5px solid #34d399;
        padding: 20px;
        font-family: 'Courier New', monospace;
        color: #34d399;
        margin: 20px 0;
    }
    
    .stButton>button {
        width: 100%;
        background: transparent;
        border: 1px solid #34d399;
        color: #34d399;
        font-family: 'Orbitron', sans-serif;
        padding: 15px;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background: #34d399;
        color: #000;
        box-shadow: 0 0 20px #34d399;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE (The Game Save) ---
if 'credits' not in st.session_state:
    st.session_state.credits = 1000
if 'rep' not in st.session_state:
    st.session_state.rep = 0
if 'logs' not in st.session_state:
    st.session_state.logs = ["SYNDICATE TERMINAL INITIALIZED...", "AWAITING ORDERS..."]

# --- SIDEBAR HUD ---
st.sidebar.markdown("<h2 class='game-header'>HUD</h2>", unsafe_allow_html=True)
st.sidebar.markdown(f"**CREDITS:** ${st.session_state.credits:,}")
st.sidebar.markdown(f"**REPUTATION:** {st.session_state.rep} XP")
if st.sidebar.button("RESET DATA"):
    st.session_state.credits = 1000
    st.session_state.rep = 0
    st.rerun()

# --- MAIN SCREEN ---
st.markdown("<h1 class='game-header'>NEON SYNDICATE</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### AVAILABLE OPERATIONS")
    
    # OP 1: Market Hack
    with st.expander("NETWORK INFILTRATION (Risk: Low)"):
        st.write("Hack a local credit exchange. Safe but low yield.")
        if st.button("EXECUTE HACK"):
            gain = random.randint(50, 200)
            st.session_state.credits += gain
            st.session_state.rep += 5
            st.session_state.logs.insert(0, f"SUCCESS: Infiltrated exchange. Gained ${gain}.")
            st.rerun()

    # OP 2: High Stakes Heist
    with st.expander("VALT-TECH HEIST (Risk: HIGH)"):
        st.write("Heavy security. Massive payout. High chance of failure.")
        if st.button("LAUNCH HEIST"):
            if random.random() > 0.6:
                gain = random.randint(2000, 5000)
                st.session_state.credits += gain
                st.session_state.rep += 50
                st.session_state.logs.insert(0, f"CRITICAL SUCCESS: Vault breached! Gained ${gain}.")
            else:
                loss = 500
                st.session_state.credits -= loss
                st.session_state.logs.insert(0, f"FAILED: Security caught the signal. Lost ${loss} in bribes.")
            st.rerun()

with col2:
    st.markdown("### LIVE FEED")
    log_text = "\n".join(st.session_state.logs[:8])
    st.markdown(f"<div class='terminal-box'>{log_text}</div>", unsafe_allow_html=True)

# --- ASSET ARCHITECT (The Million Dollar Growth) ---
st.write("---")
st.markdown("### SYNDICATE ASSETS")
a1, a2, a3 = st.columns(3)

with a1:
    st.markdown('<div class="stat-card"><h4>CRYPTO RIGS</h4><p>Generates $10/sec</p></div>', unsafe_allow_html=True)
    if st.button("PURCHASE ($500)"):
        if st.session_state.credits >= 500:
            st.session_state.credits -= 500
            st.session_state.logs.insert(0, "ASSET ACQUIRED: Crypto Rig online.")
            st.rerun()

with a2:
    st.markdown('<div class="stat-card"><h4>NEURAL LINK</h4><p>+20% Success Rate</p></div>', unsafe_allow_html=True)
    st.button("UPGRADE ($2000)")

with a3:
    st.markdown('<div class="stat-card"><h4>BLACK MARKET</h4><p>Unlocks High-Tier Ops</p></div>', unsafe_allow_html=True)
    st.button("UNLOCK ($5000)")
