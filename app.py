import streamlit as st

# --- AURA CHEF AI v18.0 ---
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
    .ai-visual-frame { border: 1px solid #34d399; padding: 20px; text-align: center; background: #000; margin-bottom: 25px; }
</style>
""", unsafe_allow_html=True)

t1, t2 = st.tabs(["AI SIGNATURE SELECTION", "GLOBAL HERITAGE ENGINE"])

# --- TAB 1: AI SIGNATURE (FIXED) ---
with t1:
    st.markdown("<h1 style='text-align: center; font-weight: 900; margin-top:40px;'>AURA AI SELECTION</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1,2,1])
    with mid:
        st.markdown(f"""
        <div class="recipe-card">
            <h2 style="text-align:center;">Lamb Mandi & Biryani Fusion</h2>
            <div class="ai-visual-frame">
                <p style="color:#34d399; font-size:0.75rem; letter-spacing:2px;">AI KINETIC STREAM: ACTIVE</p>
                <div style="height:200px; display:flex; align-items:center; justify-content:center; border:1px dashed #333;">
                    <span style="color:#444;">[CINEMATIC_MANDI_RENDER_V5]</span>
                </div>
            </div>
            <p style="color:#888; text-align:center;">Technique: Yemeni Hawayij Spicing x Indo-Pak Dum Steam</p>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: THE 15-STEP ENGINE ---
with t2:
    st.markdown("### GLOBAL HERITAGE ENGINE")
    dish = st.text_input("INPUT PANTRY ITEMS", placeholder="e.g. Chicken, Beef, Lamb...")
    
    if dish:
        heritage = st.selectbox("CHOOSE HERITAGE", 
                                ["Pakistani", "Arab/Egyptian", "Indian", "Asian", "Mexican", "American"])
        
        # We use triple quotes for every step to prevent SyntaxErrors
        db = {
            "Pakistani": [
                f"<b>Mise En Place:</b> Prepare all aromatics; thin-slice 3 onions and crush 3 inches of ginger-garlic.",
                f"<b>Fat Activation:</b> Heat 1/2 cup oil on <span class='heat-tag high'>HIGH</span> until shimmering.",
                f"<b>The Barista:</b> Sauté onions for 12-15 mins until deep chocolate brown for base flavor.",
                f"<b>Aromatic Bloom:</b> Add ginger-garlic paste; sauté for 2 mins to remove raw bite.",
                f"<b>Spice Hydration:</b> Mix spices with a splash of water to prevent scorching in the hot oil.",
                f"<b>Maillard Reaction:</b> Add {dish}. Sear on high heat to develop a rich protein crust.",
                f"<b>Tomato Reduction:</b> Add 2 chopped tomatoes. Cook until they dissolve into a jam-like paste.",
                f"<b>The Bhuna:</b> High-intensity stirring until the oil separates from the masala base.",
                f"<b>Dairy Tempering:</b> Reduce to <span class='heat-tag med'>MEDIUM</span>. Fold in 1 cup whisked yogurt slowly.",
                f"<b>Liquid Ratio:</b> Add 1 cup of boiling water. Never add cold water to hot protein.",
                f"<b>The Seal:</b> Cover with a foil-sealed lid to trap all aromatic steam.",
                f"<b>Slow Braise:</b> Reduce heat to <span class='heat-tag low'>LOW</span>. Simmer for 35 minutes.",
                f"<b>The Scent:</b> Add slit green chilies and dried fenugreek leaves (Kasuri Methi).",
                f"<b>Resting Phase:</b> Turn off heat. Let the pot sit for 10 mins to relax the meat fibers.",
                f"<b>Service:</b> Garnish with fresh ginger and cilantro. Serve over long-grain Basmati."
            ],
            "Arab/Egyptian": [
                f"<b>Ghee Initiation:</b> Melt 4 tbsp of sheep ghee in a heavy pot over <span class='heat-tag med'>MEDIUM</span> heat.",
                f"<b>Aromatic Start:</b> Sauté onions with whole cinnamon sticks and 2 pierced 'Loomi' (dried limes).",
                f"<b>Heritage Toasting:</b> Add 1 tbsp of Baharat and a pinch of Sumac. Toast for 60 seconds.",
                f"<b>Protein Coating:</b> Add {dish}. Fry until the edges are golden-yellow from the spice oils.",
                f"<b>Stock Creation:</b> Add 4 cups of boiling water. Simmer on <span class='heat-tag low'>LOW</span> until tender.",
                f"<b>Rice Prep:</b> Wash Basmati 5 times until water is clear; soak for 30 minutes.",
                f"<b>The Union:</b> Add soaked rice to the simmering meat broth; liquid should be 1 inch above.",
                f"<b>Absorption:</b> Bring to boil on <span class='heat-tag high'>HIGH</span> until water-holes form in the rice.",
                f"<b>The Smoke:</b> Place a hot coal in a foil cup with oil inside the pot; close lid for 5 mins.",
                f"<b>The Dum:</b> Reduce to lowest possible heat and steam for 20 minutes.",
                f"<b>Nut Prep:</b> Fry almonds or pine nuts in butter until golden-brown.",
                f"<b>Meat Resting:</b> Carefully remove the {dish} and keep warm under foil.",
                f"<b>Rice Fluffing:</b> Use a fork to fluff the rice from the edges—never stir the center.",
                f"<b>Assembly:</b> Spread rice on a communal platter; arrange {dish} on top.",
                f"<b>Service:</b> Shower with toasted nuts and fresh parsley. Serve with spicy tomato dip."
            ]
        }
        
        # Fallback for styles not yet fully written out in this specific code version
        steps = db.get(heritage, db["Pakistani"])

        st.markdown(f"""
        <div class="recipe-card">
            <h2 style="color:#34d399; text-align:center;">{heritage.upper()} {dish.upper()} BLUEPRINT</h2>
            <div class="ai-visual-frame">
                <p style="color:#34d399; font-size:0.7rem; letter-spacing:2px;">AI TECHNIQUE VISUALIZER: ACTIVE</p>
                <div style="height:120px; border:1px dashed #222; display:flex; align-items:center; justify-content:center;">
                    <span style="color:#444;">[AI RENDERING {heritage.upper()} PROCESS...]</span>
                </div>
            </div>
            {"".join([f"<p><span class='step-num'>{i+1:02}</span> {s}</p>" for i, s in enumerate(steps)])}
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // AI SECURE TERMINAL // 2026</p>", unsafe_allow_html=True)
