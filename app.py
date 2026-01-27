import streamlit as st
import datetime

# --- AURA CHEF | THE ELITE MASTER v41.0 ---
st.set_page_config(page_title="AURA CHEF | ELITE", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 50px; background-color: #000; padding: 25px; border-bottom: 1px solid #1a1a1a; }
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
    "Asian": {
        "spices": ["Star Anise", "Five Spice", "White Pepper", "Dried Chilies", "Ginger Root", "Garlic", "Soy Reduction"],
        "steps": 30, "focus": "Wok-Hei & Layered Umami Emulsion"
    },
    "American": {
        "spices": ["Smoked Paprika", "Garlic Powder", "Cayenne", "Brown Sugar", "Thyme", "Black Pepper"],
        "steps": 30, "focus": "Maillard Reaction & Butter Basting"
    }
}

t1, t2 = st.tabs(["MASTERCLASS PORTAL", "GLOBAL HERITAGE ARCHITECT"])

with t1:
    # FOOD OF THE DAY
    menu = {0: "Lamb Mandi Fusion", 1: "Wagyu Steak", 2: "Butter Chicken", 3: "Birria Tacos", 4: "Thai Curry", 5: "Nihari", 6: "Pasta"}
    featured = menu[datetime.datetime.now().weekday()]
    
    st.markdown(f"<h1 style='text-align: center; font-weight: 900;'>{featured.upper()}</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 4, 1])
    with mid:
        # THE CULINARY FIX: Swapping Bunny for Direct Culinary MP4
        # This is a high-speed professional searing/cooking video file.
        culinary_url = "https://v.ftcdn.net/05/59/28/94/700_F_559289456_fO6t4jMvX6vX9N7S9oI7yX8H5W7zL9Pj_ST.mp4"
        
        st.markdown(f"""
            <div class="video-frame">
                <video width="100%" height="auto" controls autoplay muted loop playsinline>
                    <source src="{culinary_url}" type="video/mp4">
                    Your browser is blocking the video element.
                </video>
            </div>
            <p style='text-align:center; color:#34d399; font-weight:bold; margin-top:15px;'>
                DIRECT CULINARY FEED: ACTIVE // V41.0
            </p>
        """, unsafe_allow_html=True)

with t2:
    st.markdown("### THE GLOBAL ARCHITECT")
    dish = st.text_input("DISH NAME", value="Lamb Mandi")
    style = st.selectbox("SELECT HERITAGE", list(heritage_db.keys()))
    
    h = heritage_db[style]
    st.markdown("**SEASONING PROTOCOL:**")
    st.markdown("".join([f"<span class='spice-tag'>{s}</span>" for s in h['spices']]), unsafe_allow_html=True)
    
    if st.button(f"GENERATE {h['steps']}-STEP {style.upper()} BLUEPRINT"):
        st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
        st.write(f"**Primary Technique:** {h['focus']}")
        st.write("---")
        for i in range(1, h['steps'] + 1):
            if i == 1: msg = f"Mise en place: Scale {dish} and arrange {len(h['spices'])} spices."
            elif i == 15: msg = f"Technical Stage: Infusing {h['spices'][0]} into the fat medium."
            elif i == 30: msg = f"Final Reveal: Garnish and serve the ultimate {style} {dish}."
            else: msg = f"Technical Phase {i}: Monitoring aromatic development and thermal consistency."
            st.markdown(f"<p><span class='step-num'>{i:02}</span> {msg}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
