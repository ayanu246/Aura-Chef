import streamlit as st
import datetime

# --- AURA CHEF | UNBLOCKABLE TERMINAL v37.0 ---
st.set_page_config(page_title="AURA CHEF | ELITE", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 50px; background-color: #000; padding: 25px; border-bottom: 1px solid #1a1a1a; }
    .video-container { 
        border: 3px solid #34d399; 
        border-radius: 12px; 
        overflow: hidden; 
        background: #000;
        box-shadow: 0 0 25px rgba(52, 211, 153, 0.2);
    }
    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #1f1f1f; border-radius: 8px; margin-top: 20px; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; border: 1px solid #34d399; padding: 4px 10px; font-family: monospace; }
    .spice-tag { background: #1e293b; color: #34d399; padding: 6px 12px; border-radius: 4px; font-size: 0.85rem; margin: 4px; display: inline-block; border: 1px solid #334155; }
</style>
""", unsafe_allow_html=True)

# --- THE 30-STEP MASTER DATABASE ---
heritage_db = {
    "Pakistani": {
        "spices": ["Kashmiri Chili", "Turmeric", "Garam Masala", "Kala Jeera", "Green Cardamom", "Kasuri Methi", "Nutmeg", "Mace"],
        "steps": 30, "focus": "The Bhuna (Oil-Masala Separation) & Dum Steam"
    },
    "Arab/Egyptian": {
        "spices": ["Black Lime (Loomi)", "Saffron", "Baharat Blend", "Clove", "Cinnamon Stick", "Bay Leaf", "Cardamom Pods"],
        "steps": 30, "focus": "Whole Spice Infusion & Rice Absorption"
    },
    "American": {
        "spices": ["Smoked Paprika", "Garlic Powder", "Cayenne", "Brown Sugar", "Thyme", "Mustard Powder"],
        "steps": 25, "focus": "Maillard Reaction & Butter Basting"
    }
}

# FOOD OF THE DAY ROTATION
daily_videos = [
    "https://assets.mixkit.co/videos/preview/mixkit-cooking-meat-in-a-pan-close-up-4690-large.mp4",
    "https://assets.mixkit.co/videos/preview/mixkit-fresh-steak-being-fried-in-a-pan-4693-large.mp4",
    "https://assets.mixkit.co/videos/preview/mixkit-chef-preparing-a-dish-in-a-professional-kitchen-4700-large.mp4"
]
day_url = daily_videos[datetime.datetime.now().weekday() % len(daily_videos)]

t1, t2 = st.tabs(["LIVE MASTERCLASS PLAYER", "GLOBAL HERITAGE ARCHITECT"])

with t1:
    st.markdown("<h1 style='text-align: center; font-weight: 900;'>ELITE CULINARY STREAM</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 4, 1])
    with mid:
        # THE "YETI" FIX: Pure HTML5 Injection
        # We use 'muted autoplay' to bypass browser blocks on video start
        st.markdown(f"""
            <div class="video-container">
                <video width="100%" height="auto" controls autoplay muted loop playsinline>
                    <source src="{day_url}" type="video/mp4">
                    Your browser is blocking the video element.
                </video>
            </div>
            <p style='text-align:center; color:#34d399; font-weight:bold; margin-top:15px;'>
                DIRECT MP4 BRIDGE: ACTIVE // V37.0
            </p>
        """, unsafe_allow_html=True)

with t2:
    st.markdown("### THE GLOBAL ARCHITECT")
    dish = st.text_input("DISH NAME", value="Lamb Mandi")
    style = st.selectbox("SELECT HERITAGE", list(heritage_db.keys()))
    
    h = heritage_db[style]
    st.markdown("**SEASONING PROTOCOL:**")
    st.markdown("".join([f"<span class='spice-tag'>{s}</span>" for s in h['spices']]), unsafe_allow_html=True)
    
    if st.button(f"GENERATE {h['steps']}-STEP BLUEPRINT"):
        st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
        for i in range(1, h['steps'] + 1):
            st.markdown(f"<p><span class='step-num'>{i:02}</span> Step {i}: Technical implementation for {style} {dish}.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
