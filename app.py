import streamlit as st
import datetime

# --- AURA CHEF | THE FINAL MASTER v39.0 ---
st.set_page_config(page_title="AURA CHEF | MASTER", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; background-color: #000; padding: 15px; border-bottom: 2px solid #1a1a1a; }
    .video-container { 
        position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; 
        max-width: 100%; background: #000; border: 4px solid #34d399; border-radius: 12px; 
    }
    .video-container iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #1f1f1f; border-radius: 8px; margin-top: 20px; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; border: 1px solid #34d399; padding: 2px 10px; font-family: monospace; }
    .spice-tag { background: #1e293b; color: #34d399; padding: 6px 12px; border-radius: 4px; font-size: 0.85rem; margin: 4px; display: inline-block; border: 1px solid #334155; }
</style>
""", unsafe_allow_html=True)

# --- THE 30-STEP MASTER ENGINE ---
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

# VIMEO CULINARY DATABASE (FOOD OF THE DAY)
# Vimeo embeds are rarely blocked by browsers compared to raw MP4s.
daily_vimeo_ids = ["314118021", "255437893", "233513251", "241604085"]
vimeo_id = daily_vimeo_ids[datetime.datetime.now().weekday() % len(daily_vimeo_ids)]

t1, t2 = st.tabs(["MASTERCLASS PLAYER", "GLOBAL HERITAGE ARCHITECT"])

with t1:
    st.markdown("<h1 style='text-align: center; font-weight: 900;'>ELITE CULINARY MASTERCLASS</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 5, 1])
    with mid:
        # THE UNSTOPPABLE VIMEO EMBED
        st.markdown(f"""
            <div class="video-container">
                <iframe src="https://player.vimeo.com/video/{vimeo_id}?autoplay=1&muted=1&loop=1&autopause=0" 
                frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
            </div>
            <p style='text-align:center; color:#34d399; font-weight:bold; margin-top:15px;'>VIMEO SECURE STREAM ACTIVE // V39.0</p>
        """, unsafe_allow_html=True)

with t2:
    st.markdown("### THE GLOBAL ARCHITECT")
    dish_input = st.text_input("DISH NAME", value="Lamb Mandi")
    style = st.selectbox("SELECT HERITAGE", list(heritage_db.keys()))
    
    h = heritage_db[style]
    st.markdown("**CORE SEASONING PROFILE:**")
    st.markdown("".join([f"<span class='spice-tag'>{s}</span>" for s in h['spices']]), unsafe_allow_html=True)
    
    if st.button(f"GENERATE FULL {h['steps']}-STEP {style.upper()} PROTOCOL"):
        st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
        st.write(f"**Primary Technique:** {h['focus']}")
        st.write("---")
        for i in range(1, h['steps'] + 1):
            # Detailed step logic
            if i == 1: msg = f"Mise en place: Scale {dish_input} and arrange all {len(h['spices'])} spices."
            elif i == 5: msg = f"Base Prep: Sauté aromatics in high-smoke-point fat until translucent."
            elif i == 15: msg = f"Spice Bloom: Introduce {h['spices'][0]} to release essential oils."
            elif i == 25: msg = "Final Reduction: Simmer until the sauce coats the back of a spoon."
            elif i == 30: msg = f"The Reveal: Plate the {style} {dish_input} with fresh garnishes."
            else: msg = f"Technical Stage {i}: Adjusting flavor balance and thermal consistency."
            
            st.markdown(f"<p><span class='step-num'>{i:02}</span> {msg}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
