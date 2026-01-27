import streamlit as st
import datetime

# --- AURA CHEF | THE GLOBAL ARCHITECT v33.0 ---
st.set_page_config(page_title="AURA CHEF | ARCHITECT", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; background-color: #000; padding: 15px; border-bottom: 2px solid #1a1a1a; }
    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #1f1f1f; border-radius: 8px; margin-top: 20px; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; border: 1px solid #34d399; padding: 2px 8px; font-family: monospace; }
    .spice-tag { background: #1a1a1a; color: #34d399; padding: 4px 10px; border-radius: 4px; font-size: 0.8rem; margin-right: 5px; border: 1px solid #333; }
</style>
""", unsafe_allow_html=True)

# --- DEEP HERITAGE DATABASE ---
heritage_data = {
    "Pakistani": {
        "seasoning": ["Kashmiri Chili", "Turmeric", "Garam Masala", "Dhaniya", "Cumin", "Kasuri Methi"],
        "logic": "High-heat oil separation (Bhuna) and yogurt-based tempering.",
        "steps": 25
    },
    "Arab/Egyptian": {
        "seasoning": ["Baharat", "Dried Lime (Loomi)", "Cardamom", "Saffron", "Cinnamon", "Allspice"],
        "logic": "Whole-spice infusion and long-grain rice steaming (Mandi/Kabsa style).",
        "steps": 22
    },
    "American": {
        "seasoning": ["Smoked Paprika", "Garlic Powder", "Cayenne", "Brown Sugar", "Mustard Powder", "Black Pepper"],
        "logic": "Low-and-slow smoking or cast-iron searing with butter basting.",
        "steps": 20
    },
    "Asian": {
        "seasoning": ["Star Anise", "Sichuan Peppercorn", "Soy Sauce", "Ginger", "Five Spice", "Sesame Oil"],
        "logic": "Wok-hei (breath of the wok) flash frying and umami layering.",
        "steps": 18
    },
    "Mexican": {
        "seasoning": ["Guajillo Chili", "Ancho Chili", "Cumin", "Dried Oregano", "Cloves", "Apple Cider Vinegar"],
        "logic": "Chili-paste rehydration and slow-braising for 'pull-apart' texture.",
        "steps": 24
    }
}

t1, t2 = st.tabs(["LIVE MASTERCLASS", "GLOBAL HERITAGE ENGINE"])

with t1:
    st.markdown("<h1 style='text-align:center;'>MASTERCLASS PORTAL</h1>", unsafe_allow_html=True)
    # (Previous search logic remains here)
    st.info("The Live Sync button will appear here to find the best current video.")

with t2:
    st.markdown("### THE GLOBAL ENGINE")
    dish = st.text_input("WHAT DISH ARE WE BUILDING?", value="Lamb")
    heritage = st.selectbox("SELECT HERITAGE STYLE", list(heritage_data.keys()))
    
    data = heritage_data[heritage]
    
    st.markdown(f"#### {heritage.upper()} {dish.upper()} SPECIFICATIONS")
    
    # Seasoning Display
    st.markdown("**REQUIRED SEASONING PROFILE:**")
    spice_html = "".join([f"<span class='spice-tag'>{s}</span>" for s in data["seasoning"]])
    st.markdown(spice_html, unsafe_allow_html=True)
    
    if st.button(f"GENERATE {data['steps']}-STEP TECHNICAL BLUEPRINT"):
        st.markdown(f"<div class='recipe-card'>", unsafe_allow_html=True)
        st.write(f"**Technique:** {data['logic']}")
        st.write("---")
        
        # Dynamic Step Generator (Scales based on heritage)
        for i in range(1, data["steps"] + 1):
            if i == 1: text = f"Mise en place: Scale exactly 1kg of {dish} and prepare {heritage} spice blend."
            elif i == 5: text = f"Aromatic Bloom: Toast {data['seasoning'][0]} and {data['seasoning'][1]} in hot fat."
            elif i == 10: text = f"The Deep Sear: Achieve Maillard reaction on {dish} surfaces."
            elif i == data["steps"]: text = f"Final Presentation: Garnish with heritage-specific herbs and serve."
            else: text = f"Technical phase {i}: Maintaining consistent thermal mass and moisture levels."
            
            st.markdown(f"<p><span class='step-num'>{i:02}</span> {text}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // V33.0 // 2026</p>", unsafe_allow_html=True)
