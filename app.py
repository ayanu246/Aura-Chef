import streamlit as st
import datetime

# --- AURA CHEF | THE FINAL ARCHITECT v34.0 ---
st.set_page_config(page_title="AURA CHEF | FINAL FIX", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; background-color: #000; padding: 15px; border-bottom: 2px solid #1a1a1a; }
    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #1f1f1f; border-radius: 8px; margin-top: 20px; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; border: 1px solid #34d399; padding: 2px 8px; font-family: monospace; }
    .spice-tag { background: #1e293b; color: #34d399; padding: 6px 12px; border-radius: 4px; font-size: 0.85rem; margin: 4px; display: inline-block; border: 1px solid #334155; }
    .action-btn {
        display: block; width: 100%; padding: 20px; background: #34d399; color: #000; 
        text-align: center; font-weight: 900; text-decoration: none; border-radius: 8px;
        text-transform: uppercase; letter-spacing: 2px; margin: 20px 0; font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# --- THE ULTIMATE HERITAGE ENGINE ---
heritage_db = {
    "Pakistani": {
        "spices": ["Kashmiri Chili", "Turmeric", "Garam Masala", "Kala Jeera", "Green Cardamom", "Kasuri Methi", "Nutmeg", "Mace"],
        "steps": 30,
        "focus": "The Bhuna (Oil-Masala Separation) & Dum Steam"
    },
    "Arab/Egyptian": {
        "spices": ["Black Lime (Loomi)", "Saffron", "Baharat Blend", "Clove", "Cinnamon Stick", "Bay Leaf", "Cardamom Pods"],
        "steps": 28,
        "focus": "Whole Spice Infusion & Rice Absorption"
    },
    "Asian": {
        "spices": ["Star Anise", "Five Spice", "White Pepper", "Dried Chilies", "Ginger Root", "Garlic", "Soy Reduction"],
        "steps": 25,
        "focus": "Wok-Hei & Layered Umami Emulsion"
    },
    "American": {
        "spices": ["Celery Salt", "Smoked Paprika", "Onion Powder", "Cayenne", "Brown Sugar", "Thyme", "Black Pepper"],
        "steps": 22,
        "focus": "Maillard Reaction & Fat Basting"
    },
    "Mexican": {
        "spices": ["Ancho Chili", "Guajillo Chili", "Mexican Oregano", "Cumin", "Clove", "Cinnamon", "Apple Cider Vinegar"],
        "steps": 30,
        "focus": "Chili Rehydration & Acidic Balancing"
    }
}

t1, t2 = st.tabs(["MASTERCLASS PORTAL", "GLOBAL HERITAGE ENGINE"])

with t1:
    # Today's Food of the Day
    menu = {0: "Lamb Mandi Biryani Fusion", 1: "Wagyu Steak", 2: "Butter Chicken", 3: "Birria Tacos", 4: "Thai Curry", 5: "Nihari", 6: "Pasta"}
    featured = menu[datetime.datetime.now().weekday()]
    
    st.markdown(f"<h1 style='text-align:center;'>{featured.upper()}</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 4, 1])
    with mid:
        # THE LIVE FIX: This generates the search instantly.
        search_url = f"https://www.youtube.com/results?search_query=best+professional+{featured.replace(' ', '+')}+recipe+4k"
        st.markdown(f"""
            <div class="recipe-card" style="border: 2px solid #34d399;">
                <p><b>STATUS:</b> <span style="color:#34d399;">LIVE CONNECTION READY</span></p>
                <p>Click below to find the absolute best, most recent professional video for today's dish.</p>
                <a href="{search_url}" target="_blank" class="action-btn">▶ SYNC MASTERCLASS VIDEO</a>
            </div>
        """, unsafe_allow_html=True)

with t2:
    st.markdown("### THE GLOBAL ARCHITECT")
    dish_input = st.text_input("ENTER YOUR INGREDIENT", value="Lamb")
    style_choice = st.selectbox("SELECT HERITAGE STYLE", list(heritage_db.keys()))
    
    h = heritage_db[style_choice]
    
    st.markdown(f"#### {style_choice.upper()} {dish_input.upper()} PROTOCOL")
    
    # Seasoning Display
    st.markdown("**CORE SEASONING & AROMATICS:**")
    spice_html = "".join([f"<span class='spice-tag'>{s}</span>" for s in h["spices"]])
    st.markdown(spice_html, unsafe_allow_html=True)
    
    if st.button(f"GENERATE {h['steps']}-STEP BLUEPRINT"):
        st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
        st.write(f"**Primary Technique:** {h['focus']}")
        st.write("---")
        
        # High-Complexity Step Logic
        for i in range(1, h["steps"] + 1):
            if i == 1: text = f"Mise en place: Weight {dish_input} to exactly 1000g; prep {h['spices'][0]}."
            elif i == 5: text = f"Thermal Prep: Heat heavy-bottomed pot to 180°C."
            elif i == 10: text = f"The Sear: Brown {dish_input} in small batches to maintain pan heat."
            elif i == 15: text = f"The Bloom: Add {', '.join(h['spices'][:3])} to the hot oil for 45 seconds."
            elif i == 20: text = "Moisture Control: Deglaze pan with bone broth or heritage liquids."
            elif i == 25: text = "The Long Simmer: Reduce heat to 85°C and seal with a heavy lid."
            elif i == h["steps"]: text = f"Final Reveal: Garnish with fresh herbs and serve the perfect {dish_input}."
            else: text = f"Technical Phase {i}: Monitoring internal temperature and aromatic development."
            
            st.markdown(f"<p><span class='step-num'>{i:02}</span> {text}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // ARCHITECT v34.0 // 2026</p>", unsafe_allow_html=True)
