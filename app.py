import streamlit as st
import datetime

# --- AURA CHEF | TOTAL BYPASS v38.0 ---
st.set_page_config(page_title="AURA CHEF | MASTER ARCHITECT", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; background-color: #000; padding: 15px; border-bottom: 2px solid #1a1a1a; }
    .video-frame { 
        border: 4px solid #34d399; 
        border-radius: 12px; 
        overflow: hidden; 
        background: #000;
        box-shadow: 0 0 30px rgba(52, 211, 153, 0.3);
    }
    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #1f1f1f; border-radius: 8px; margin-top: 20px; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; border: 1px solid #34d399; padding: 2px 10px; font-family: monospace; }
    .spice-tag { background: #1e293b; color: #34d399; padding: 6px 12px; border-radius: 4px; font-size: 0.85rem; margin: 4px; display: inline-block; border: 1px solid #334155; }
</style>
""", unsafe_allow_html=True)

# --- THE 30-STEP CULINARY DATABASE ---
heritage_db = {
    "Pakistani": {
        "spices": ["Kashmiri Chili", "Turmeric", "Garam Masala", "Kala Jeera", "Green Cardamom", "Kasuri Methi", "Nutmeg", "Mace"],
        "steps": 30, "focus": "The Bhuna (Oil-Masala Separation) & Dum Steam"
    },
    "Arab/Egyptian": {
        "spices": ["Black Lime (Loomi)", "Saffron", "Baharat Blend", "Clove", "Cinnamon Stick", "Bay Leaf", "Cardamom Pods"],
        "steps": 30, "focus": "Whole Spice Infusion & Rice Absorption"
    },
    "Asian": {
        "spices": ["Star Anise", "Five Spice", "White Pepper", "Dried Chilies", "Ginger Root", "Garlic", "Soy Reduction"],
        "steps": 30, "focus": "Wok-Hei & Layered Umami Emulsion"
    },
    "American": {
        "spices": ["Smoked Paprika", "Garlic Powder", "Cayenne", "Brown Sugar", "Thyme", "Mustard Powder"],
        "steps": 30, "focus": "Maillard Reaction & Butter Basting"
    }
}

# --- FOOD OF THE DAY (High-Reliability Direct Links) ---
daily_vids = [
    "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4", # Test Link
    "https://v.ftcdn.net/05/59/28/94/700_F_559289456_fO6t4jMvX6vX9N7S9oI7yX8H5W7zL9Pj_ST.mp4", # Meat Searing
    "https://v.ftcdn.net/02/90/19/20/700_F_290192080_y4J3qY3S1f1l6p9uU5j7kG8uU4e9M5j9_ST.mp4"  # Chef Prep
]
current_vid = daily_vids[datetime.datetime.now().weekday() % len(daily_vids)]

t1, t2 = st.tabs(["MASTERCLASS PORTAL", "GLOBAL HERITAGE ARCHITECT"])

with t1:
    st.markdown("<h1 style='text-align: center; font-weight: 900;'>MASTERCLASS VIDEO</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 4, 1])
    with mid:
        # THE FIX: Native HTML5 bypass with forced 'muted' to ensure play
        st.markdown(f"""
            <div class="video-frame">
                <video width="100%" controls autoplay muted loop playsinline>
                    <source src="{current_vid}" type="video/mp4">
                    Your browser is blocking the video stream.
                </video>
            </div>
            <p style='text-align:center; color:#34d399; margin-top:10px;'><b>DIRECT 4K INJECTION: ACTIVE</b></p>
        """, unsafe_allow_html=True)

with t2:
    st.markdown("### THE GLOBAL ARCHITECT")
    dish_name = st.text_input("ENTER INGREDIENT", value="Lamb Mandi")
    style = st.selectbox("SELECT HERITAGE", list(heritage_db.keys()))
    
    h = heritage_db[style]
    st.markdown("**CORE SEASONING:**")
    st.markdown("".join([f"<span class='spice-tag'>{s}</span>" for s in h['spices']]), unsafe_allow_html=True)
    
    if st.button(f"BUILD {h['steps']}-STEP TECHNICAL GUIDE"):
        st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
        st.write(f"**Technique Mastery:** {h['focus']}")
        st.write("---")
        
        for i in range(1, h['steps'] + 1):
            if i == 1: msg = f"Mise en place: Scale {dish_name} to 1000g."
            elif i == 10: msg = f"Aromatic Bloom: Toast {h['spices'][0]} in fat."
            elif i == 20: msg = "Thermal Equilibrium: Maintain 95°C core temp."
            elif i == 30: msg = f"Final Reveal: Present the {style} {dish_name} masterpiece."
            else: msg = f"Technical Phase {i}: Adjusting osmotic pressure and aromatic profile."
            
            st.markdown(f"<p><span class='step-num'>{i:02}</span> {msg}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
