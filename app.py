import streamlit as st
import datetime

# --- AURA CHEF WORLD-CLASS TERMINAL v22.0 ---
st.set_page_config(page_title="AURA CHEF | GLOBAL ELITE", page_icon="⚖️", layout="wide")

# --- ELITE UI STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 50px; background-color: #000; padding: 25px; border-bottom: 1px solid #1a1a1a; }
    .stTabs [data-baseweb="tab"] { font-size: 0.9rem; font-weight: 900; color: #555; text-transform: uppercase; letter-spacing: 2px; }
    .recipe-card { background: #0a0a0a; padding: 50px; border: 1px solid #1f1f1f; border-radius: 4px; margin-top: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.5); }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; font-family: 'Courier New', monospace; border: 1px solid #34d399; padding: 4px 10px; font-size: 0.9rem; }
    .heat-tag { font-weight: bold; padding: 3px 10px; border-radius: 2px; font-size: 0.7rem; text-transform: uppercase; margin-left: 10px; }
    .high { background: #471111; color: #ff4b4b; }
    .med { background: #473211; color: #ffa500; }
    .low { background: #112247; color: #4b96ff; }
    .masterclass-btn {
        display: block; width: 100%; padding: 25px; background: #fff; color: #000; 
        text-align: center; font-weight: 900; text-decoration: none; border-radius: 4px;
        text-transform: uppercase; letter-spacing: 3px; transition: 0.4s; margin: 30px 0;
        font-size: 1.1rem; border: none;
    }
    .masterclass-btn:hover { background: #34d399; transform: scale(1.02); }
</style>
""", unsafe_allow_html=True)

# --- DYNAMIC DAILY MENU (Changes Every 24 Hours) ---
menu = {
    0: "Lamb Mandi Biryani Fusion", 
    1: "Wagyu A5 Garlic Steak",
    2: "Royal Mughlai Butter Chicken",
    3: "Mexican Birria Consomé Tacos",
    4: "Authentic Tonkotsu Ramen",
    5: "Slow-Braised Pakistani Nihari",
    6: "Truffle Lobster Risotto"
}
day_idx = datetime.datetime.now().weekday()
food_of_day = menu[day_idx]

tab1, tab2 = st.tabs(["MASTERCLASS PORTAL", "GLOBAL HERITAGE ENGINE"])

# --- TAB 1: DYNAMIC DAILY MASTERCLASS ---
with tab1:
    st.markdown(f"<h1 style='text-align: center; font-weight: 900; font-size: 3.5rem; letter-spacing: -2px;'>{food_of_day.upper()}</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 2, 1])
    with mid:
        # SEARCH ENGINE: This forces YouTube to find the best 4K Masterclass
        yt_link = f"https://www.youtube.com/results?search_query=best+professional+{food_of_day.replace(' ', '+')}+recipe+4k"
        
        st.markdown(f"""
            <div class="recipe-card" style="text-align:center;">
                <p style="color:#34d399; font-weight:bold; letter-spacing:2px;">AI VIDEO ENGINE: ONLINE</p>
                <p style="color:#666;">Streaming a high-priority professional guide for today's selection.</p>
                <a href="{yt_link}" target="_blank" class="masterclass-btn">WATCH 4K MASTERCLASS ↗</a>
                <p style="font-size:0.8rem; color:#444;">Bypassing restricted embeds for maximum quality.</p>
            </div>
        """, unsafe_allow_html=True)

# --- TAB 2: GLOBAL HERITAGE ENGINE (15 STEPS) ---
with tab2:
    st.markdown("### THE GLOBAL ENGINE")
    target_food = st.text_input("WHAT ARE YOU DREAMING OF MAKING?", placeholder="e.g. Ribeye, Prawns, Lamb...")
    
    if target_food:
        heritage = st.selectbox("SELECT CULINARY HERITAGE", 
                                ["Pakistani", "Arab/Egyptian", "Indian", "Asian", "Mexican", "American"])
        
        # SEARCH FOR THE SPECIFIC HERITAGE DISH
        custom_yt = f"https://www.youtube.com/results?search_query=professional+{heritage}+{target_food}+recipe+tutorial"

        # 15-STEP WORLD-CLASS LOGIC
        steps = [
            f"<b>Mise En Place:</b> Organize all heritage spices and prep 1kg of {target_food}.",
            f"<b>Fat Prep:</b> Heat oil or ghee to <span class='heat-tag high'>HIGH</span> until a cumin seed sizzles.",
            f"<b>Onion Excellence:</b> Sauté onions for 12-15 mins until deep mahogany brown. This is the flavor base.",
            f"<b>Aromatic Bloom:</b> Add fresh ginger-garlic paste. Sauté for 2 mins to release essential oils.",
            f"<b>Spice Hydration:</b> Mix spices with 2 tbsp water before adding to prevent scorching.",
            f"<b>Maillard Reaction:</b> Add {target_food}. Flash-sear on max heat to develop a rich, deep crust.",
            f"<b>Deglazing:</b> Add tomato reduction and scrape the caramelized 'fond' from the pot bottom.",
            f"<b>The Bhuna:</b> Cook intensely until the oil 'breaks' and separates from the spice paste.",
            f"<b>Dairy Tempering:</b> Reduce to <span class='heat-tag med'>MEDIUM</span>. Fold in whisked yogurt slowly.",
            f"<b>Liquid Balance:</b> Add boiling water (never cold) to reach your desired gravy consistency.",
            f"<b>The Seal:</b> Cover with a foil-wrapped lid to trap all micro-aromas and moisture.",
            f"<b>Slow Braise:</b> Drop heat to <span class='heat-tag low'>LOW</span>. Simmer for 35 mins until tender.",
            f"<b>Final Infusion:</b> Add slit green chilies and fresh heritage herbs (Cilantro/Mint).",
            f"<b>Resting Phase:</b> Turn off all heat. Let the pot sit for 10-12 minutes to relax the meat.",
            f"<b>The Reveal:</b> Garnish with fresh ginger matchsticks and serve with hot, aged Basmati rice."
        ]

        st.markdown(f"""
        <div class="recipe-card">
            <h2 style="color:#34d399; text-align:center;">{heritage.upper()} {target_food.upper()}</h2>
            <a href="{custom_yt}" target="_blank" class="masterclass-btn">LAUNCH {heritage.upper()} VIDEO ↗</a>
            <hr style="border:0.1px solid #222; margin: 30px 0;">
            {"".join([f"<p><span class='step-num'>{i+1:02}</span> {s}</p>" for i, s in enumerate(steps)])}
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // GLOBAL ELITE // 2026</p>", unsafe_allow_html=True)
