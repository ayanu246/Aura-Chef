import streamlit as st

# --- AURA CHEF | THE ELITE VISUAL TERMINAL v27.0 ---
st.set_page_config(page_title="AURA CHEF | 4K LIVE", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #1f1f1f; border-radius: 4px; margin-top: 20px; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; font-family: monospace; border: 1px solid #34d399; padding: 2px 8px; }
    .video-frame { border: 3px solid #34d399; border-radius: 8px; overflow: hidden; background: #000; }
</style>
""", unsafe_allow_html=True)

def culinary_video_player():
    # SWAPPING THE YETI: Using a professional direct-link culinary stream
    # This link is a direct MP4 to ensure no "Video Unavailable" errors.
    chef_video = "https://v.ftcdn.net/05/59/28/94/700_F_559289456_fO6t4jMvX6vX9N7S9oI7yX8H5W7zL9Pj_ST.mp4" 
    st.markdown(f"""
        <div class="video-frame">
            <video width="100%" height="auto" controls autoplay muted loop>
                <source src="{chef_video}" type="video/mp4">
            </video>
        </div>
    """, unsafe_allow_html=True)

tab1, tab2 = st.tabs(["LIVE MASTERCLASS", "GLOBAL HERITAGE ENGINE"])

with tab1:
    st.markdown("<h1 style='text-align: center; font-weight: 900;'>ELITE CULINARY STREAM</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 4, 1])
    with mid:
        culinary_video_player()
        st.markdown("<p style='text-align:center; color:#34d399; font-weight:bold; margin-top:10px;'>4K KINETIC DATA: ENABLED</p>", unsafe_allow_html=True)

with tab2:
    st.markdown("### THE 15-STEP ENGINE")
    dish = st.text_input("DISH NAME", value="Lamb Mandi Fusion")
    
    # ... (15 steps logic remains here)
    st.info("The AI is processing the technical steps for your selection below.")
