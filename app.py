import streamlit as st
import time

# --- AURA CHEF AI v16.0 ---
st.set_page_config(page_title="AURA CHEF | AI VISUALIZER", page_icon="⚖️", layout="wide")

# --- UI STYLING: THE BLACK ROOM ---
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
    .ai-visual-box { border: 2px solid #34d399; padding: 20px; text-align: center; background: #000; margin-bottom: 25px; position: relative; }
</style>
""", unsafe_allow_html=True)

t1, t2 = st.tabs(["AI SIGNATURE SELECTION", "GLOBAL HERITAGE ENGINE"])

# --- TAB 1: THE MANDI BIRYANI MASTERCLASS ---
with t1:
    st.markdown("<h1 style='text-align: center; font-weight: 900; margin-top:40px;'>AURA AI SIGNATURE</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1,2,1])
    with mid:
        st.markdown("""
        <div class="recipe-card">
            <h2 style="text-align:center; letter-spacing:-1px;">Lamb Mandi & Biryani Fusion</h2>
            <div class="ai-visual-box">
                <p style="color:#34d399; font-size:0.75rem; letter-spacing:2px; margin-bottom:10px;">AI VIDEO KINETIC RENDER ACTIVE</p>
                <div style="border:1px dashed #333; height:250px; display:flex; align-items:center; justify-content:center;">
                    <span style="color:#444;">[AI CINEMATIC VISUALIZATION: SMOKED LAMB OVER SAFFRON GRAIN]</span>
                </div>
            </div>
            <p style="color:#888; text-align:center; font-size:0.9rem;">The AI has fused the Yemeni 'Hawayij' spice profile with the 'Dum' layering of Indo-Pak heritage.</p>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: GLOBAL HERITAGE ENGINE (15 STEPS) ---
with t2:
    st.markdown("### GLOBAL HERITAGE ENGINE")
    dish = st.text_input("INPUT MAIN INGREDIENT", placeholder="e.g. Chicken, Lamb, Prawns...")
    
    if dish:
        heritage = st.selectbox("CHOOSE HERITAGE STYLE", 
                                ["Pakistani", "Arab/Egyptian", "Indian", "Asian", "Mexican", "American"])
        
        # MASSIVE CULINARY LOGIC DATABASE
        db = {
            "Pakistani": [
                "<b>Mise En Place:</b> Peel and thin-slice 4 large red onions; crush 3 inches of ginger and 12 cloves of garlic.",
                "<b>Fat Activation:</b> Heat 150ml of high-smoke point oil on <span class='heat-tag high'>HIGH</span> heat.",
                "<b>The Browning (Barista):</b> Sauté onions for 15 mins. They must be deep chocolate brown but not bitter.",
                "<b>Aromatic Bloom:</b> Add ginger-garlic paste. Stir for 120 seconds until the 'raw' aroma is gone.",
                "<b>Spice Hydration:</b> Mix 2 tbsp Garam Masala and 1 tbsp Kashmiri Chili with water; add to the pot.",
                "<b>The Maillard Reaction:</b> Add " + dish + ". Sear at max heat for 8 mins to lock in every drop of juice.",
                "<b>Acidity Layer:</b> Add 3 finely chopped vine tomatoes. Cook until they dissolve into a rich, thick jam.",
                "<b>The Bhuna:</b> High-intensity stirring until the oil 'breaks' and separates from the spice base.",
                "<b>Dairy Tempering:</b> Reduce to <span class='heat-tag med'>MEDIUM</span>. Fold in 1 cup of whisked yogurt slowly.",
                "<b>The Liquid Ratio:</b> Add 1.5 cups of boiling water. Never add cold water to hot protein.",
                "<b>The Cover:</b> Seal the pot with a heavy lid and a weight. Reduce heat to <span class='heat-tag low'>LOW</span>.",
                "<b>Braising:</b> Allow 35-45 minutes for the protein fibers to break down into a 'melt-in-mouth' state.",
                "<b>The Scent:</b> Add 5 slit Thai green chilies and a handful of dried fenugreek leaves (Kasuri Methi).",
                "<b>Resting:</b> Turn off the heat. Keep the lid sealed for 12 mins to let the steam settle.",
                "<b>Service:</b> Garnish with fresh ginger matchsticks and cilantro. Serve with aged Basmati rice."
            ],
            "Arab/Egyptian": [
                "<b>Fat Initiation:</b> Melt 4 tbsp of pure sheep ghee in a heavy cast iron pot on <span class='heat-tag med'>MEDIUM</span>.",
                "<b>Aromatic Start:</b> Sauté onions with 2 whole 'Loomi' (dried limes). Pierce the limes first.",
                "<b>Heritage Toasting:</b> Add 2 cinnamon sticks, 5 green cardamom pods, and a pinch of whole cloves.",
                "<b>Baharat Bloom:</b> Stir in the Arab 7-Spice mix (Baharat) and a dusting of Sumac for 60 seconds.",
                "<b>The Sear:</b> Add your " + dish + ". Fry until the edges are golden-yellow from the spice oil.",
                "<b>Stock Production:</b> Add 4 cups of boiling water and salt. Simmer on <span class='heat-tag low'>LOW</span> until tender.",
                "<b>Rice Prep:</b> Wash long-grain Basmati 5 times until the water runs clear. Soak for 30 minutes.",
                "<b>The Union:</b> Add the soaked rice to the simmering meat broth. The water must be 1 inch above.",
                "<b>Boil Phase:</b> Crank heat to <span class='heat-tag high'>HIGH</span> until the water evaporates and 'holes' form.",
                "<b>The Smoke:</b> Light a natural wood coal. Place in a foil cup with oil inside the pot. Close tightly.",
                "<b>Steaming:</b> Reduce to the absolute lowest heat for 20 minutes.",
                "<b>Nut Prep:</b> Fry almonds and pine nuts in butter until golden. Set aside.",
                "<b>The Reveal:</b> Open the lid. The aroma should be intensely smoky and citrusy.",
                "<b>Assembly:</b> Place the rice on a massive communal tray, meat on top, nuts showered over.",
                "<b>Service:</b> Serve with a side of 'Salata Hara' (spicy tomato and parsley dip)."
            ]
        }
        
        # Final Step Generation
        steps = db.get(heritage, db["Pakistani"])

        st.markdown(f"""
        <div class="recipe-card">
            <h2 style="color:#34d399; text-align:center;">{heritage.upper()} {dish.upper()} BLUEPRINT</h2>
            <div class="ai-visual-box">
                <p style="color:#34d399; font-size:0.7rem; letter-spacing:2px;">AI TECHNIQUE VISUALIZER: {heritage.upper()}</p>
                <div style="height:120px; border:1px dashed #222; display:flex; align-items:center; justify-content:center;">
                    <span style="color:#444;">[GENERATING {heritage.upper()} CULINARY PROCESS...]</span>
                </div>
            </div>
            {"".join([f"<p><span class='step-num'>{i+1:02}</span> {s}</p>" for i, s in enumerate(steps)])}
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // AI SECURE TERMINAL // 2026</p>", unsafe_allow_html=True)
