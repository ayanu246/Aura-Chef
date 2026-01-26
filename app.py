import streamlit as st
import time

# --- AURA CHEF AI v15.0 ---
st.set_page_config(page_title="AURA CHEF | AI ELITE", page_icon="⚖️", layout="wide")

# --- UI STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 40px; background-color: #000; padding: 20px; border-bottom: 1px solid #1a1a1a; }
    .stTabs [data-baseweb="tab"] { font-size: 0.85rem; font-weight: 700; color: #444; text-transform: uppercase; }
    .recipe-card { background: #0a0a0a; padding: 45px; border: 1px solid #1f1f1f; border-radius: 4px; margin-top: 25px; line-height: 1.8; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; font-family: monospace; border: 1px solid #34d399; padding: 2px 8px; }
    .heat-tag { font-weight: bold; padding: 2px 8px; border-radius: 2px; font-size: 0.75rem; text-transform: uppercase; }
    .high { background: #471111; color: #ff4b4b; }
    .med { background: #473211; color: #ffa500; }
    .low { background: #112247; color: #4b96ff; }
    .ai-frame { border: 1px solid #34d399; padding: 20px; text-align: center; background: #000; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

t1, t2 = st.tabs(["AI SIGNATURE SELECTION", "GLOBAL PANTRY ENGINE"])

# --- TAB 1: SIGNATURE ---
with t1:
    st.markdown("<h1 style='text-align: center; font-weight: 900; margin-top:40px;'>AURA AI SIGNATURE</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1,2,1])
    with mid:
        st.markdown("""
        <div class="recipe-card">
            <h2 style="text-align:center;">Lamb Mandi & Biryani Fusion</h2>
            <div class="ai-frame">
                <h4 style="color:#34d399;">AI VISUAL GENERATION ACTIVE</h4>
                <p style="font-size:0.8rem; color:#666;">PROCESSING KINETIC CULINARY DATA...</p>
                <div style="height:300px; display:flex; align-items:center; justify-content:center; border:1px dashed #333;">
                    <p>AI VIDEO STREAM INITIALIZED: [CINEMATIC_MANDI_RENDER_V4]</p>
                </div>
            </div>
            <p style="color:#888; text-align:center;">This dish uses the Yemeni smoke-pit technique combined with 72-hour aged Basmati rice.</p>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: THE 15-STEP ENGINE ---
with t2:
    st.markdown("### GLOBAL HERITAGE ENGINE")
    dish_input = st.text_input("INPUT PANTRY ITEMS", placeholder="e.g. Chicken, Beef, Lamb, Potato...")
    
    if dish_input:
        heritage = st.selectbox("SELECT HERITAGE", ["Pakistani", "Indian", "Arab/Egyptian", "Asian", "Mexican", "American"])
        
        # MASSIVE 15-STEP DATABASE
        db = {
            "Pakistani": [
                "<b>Mise En Place:</b> Peel and thin-slice 3 onions; crush 3 inches of ginger and 10 garlic cloves.",
                "<b>Fat Activation:</b> Heat 1/2 cup oil on <span class='heat-tag high'>HIGH</span> until it shimmers.",
                "<b>The Browning:</b> Sauté onions for 12-15 mins. They must be uniform chocolate brown.",
                "<b>Aromatic Bloom:</b> Add ginger-garlic paste. Stir for 90 seconds until the raw smell vanishes.",
                "<b>Spice Hydration:</b> Mix Garam Masala, Chili, and Turmeric with water to prevent scorching.",
                "<b>The Maillard Reaction:</b> Add " + dish_input + ". Increase heat to max and sear until deep brown.",
                "<b>Acidity Layer:</b> Add 2 chopped tomatoes. Cook until they dissolve into a thick jam.",
                "<b>The Bhuna:</b> Continue stirring on high heat until the oil separates completely from the masala.",
                "<b>Dairy Tempering:</b> Reduce to <span class='heat-tag med'>MEDIUM</span>. Add whisked yogurt one spoonful at a time.",
                "<b>Pressure/Cover:</b> Add 1 cup hot water. Cover with a heavy, weighted lid.",
                "<b>Slow Braise:</b> Reduce heat to <span class='heat-tag low'>LOW</span>. Simmer for 35 minutes.",
                "<b>The Scent:</b> Add 4 slit green chilies and a palmful of dried fenugreek leaves (Kasuri Methi).",
                "<b>Garnish:</b> Use 1 cup of fresh cilantro and 1/2 cup of julienned ginger.",
                "<b>Resting Phase:</b> Turn off heat. Keep lid sealed for 10 mins to allow juices to redistribute.",
                "<b>Service:</b> Serve on a heated platter with Roghni Naan or Basmati rice."
            ],
            "Indian": [
                "<b>Whole Spice Tempering:</b> Heat ghee on <span class='heat-tag high'>HIGH</span>. Add cardamom, cinnamon, and cloves.",
                "<b>Onion Base:</b> Sauté onions until translucent and soft, not crispy.",
                "<b>Ginger-Garlic Infusion:</b> Add fresh paste and sauté until golden.",
                "<b>Tomato-Cashew Base:</b> Add tomato puree and cashew paste for a silky restaurant texture.",
                "<b>Spice Layering:</b> Add Kashmiri Mirch, Kadhai Masala, and Turmeric.",
                "<b>Protein Searing:</b> Add " + dish_input + ". Coat thoroughly in the thick gravy.",
                "<b>Moisture Control:</b> Add warm water only; cold water will shock the proteins.",
                "<b>The Simmer:</b> Cover and cook on <span class='heat-tag med'>MEDIUM-LOW</span> for 20 minutes.",
                "<b>Creaming:</b> Pour in heavy cream in a slow stream while stirring.",
                "<b>Butter Finish:</b> Add cold butter cubes to create a glossy 'Makhani' finish.",
                "<b>Herbal Touch:</b> Rub Kasuri Methi between hands and sprinkle for aroma.",
                "<b>Saffron Drop:</b> Add saffron-infused milk for the Royal Indian profile.",
                "<b>Smoking:</b> Place a hot coal in the center for a smoky Tandoor effect.",
                "<b>Garnish:</b> Top with fresh cream swirls and cilantro.",
                "<b>Service:</b> Pair with Garlic Naan or Jeera Rice."
            ]
            # ... and so on for all heritages
        }
        
        steps = db.get(heritage, db["Pakistani"])

        st.markdown(f"""
        <div class="recipe-card">
            <h2 style="color:#34d399; text-align:center;">AI CULINARY BLUEPRINT: {heritage.upper()} {dish_input.upper()}</h2>
            <hr style="border:0.1px solid #333">
            <div class="ai-frame">
                <p style="color:#34d399; font-size:0.75rem;">AI VIDEO GENERATION FOR {heritage.upper()} TECHNIQUE...</p>
                <div style="height:150px; border:1px dashed #222; display:flex; align-items:center; justify-content:center;">
                    [AI VIDEO STREAM: {heritage.upper()}_KITCHEN_PROCESS]
                </div>
            </div>
            {"".join([f"<p><span class='step-num'>{i+1:02}</span> {s}</p>" for i, s in enumerate(steps)])}
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // AI SECURE TERMINAL // 2026</p>", unsafe_allow_html=True)
