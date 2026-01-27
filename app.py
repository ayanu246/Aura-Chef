import streamlit as st
import datetime

# --- AURA CHEF WORLD-CLASS TERMINAL v21.0 ---
st.set_page_config(page_title="AURA CHEF | GLOBAL ELITE", page_icon="⚖️", layout="wide")

# --- ULTIMATE UI DESIGN ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 50px; background-color: #000; padding: 25px; border-bottom: 1px solid #1a1a1a; }
    .stTabs [data-baseweb="tab"] { font-size: 0.9rem; font-weight: 900; color: #555; text-transform: uppercase; letter-spacing: 2px; }
    .stTabs [data-baseweb="tab-highlight"] { background-color: #34d399; }
    .recipe-card { background: #0a0a0a; padding: 50px; border: 1px solid #1f1f1f; border-radius: 4px; margin-top: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.5); }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; font-family: 'Courier New', monospace; border: 1px solid #34d399; padding: 4px 10px; font-size: 0.9rem; }
    .heat-tag { font-weight: bold; padding: 3px 10px; border-radius: 2px; font-size: 0.7rem; text-transform: uppercase; margin-left: 10px; }
    .high { background: #471111; color: #ff4b4b; }
    .med { background: #473211; color: #ffa500; }
    .low { background: #112247; color: #4b96ff; }
    .video-frame { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px; border: 2px solid #222; margin: 20px 0; }
    .video-frame iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
</style>
""", unsafe_allow_html=True)

# --- DYNAMIC MASTER ENGINE ---
menu = {
    0: "Lamb Mandi Biryani Fusion", 
    1: "Wagyu A5 Steak Masterclass",
    2: "Royal Butter Chicken",
    3: "Mexican Street Birria",
    4: "Japanese Wagyu Ramen",
    5: "Authentic Pakistani Nihari",
    6: "Truffle Lobster Pasta"
}
day_idx = datetime.datetime.now().weekday()
food_of_day = menu[day_idx]

tab1, tab2 = st.tabs(["MASTERCLASS PORTAL", "GLOBAL HERITAGE ENGINE"])

# --- TAB 1: DYNAMIC DAILY MASTERCLASS ---
with tab1:
    st.markdown(f"<h1 style='text-align: center; font-weight: 900; font-size: 3.5rem; letter-spacing: -2px;'>{food_of_day.upper()}</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 2, 1])
    with mid:
        # SEARCH LOGIC: This finds a high-quality video for the daily dish
        search_query = food_of_day.replace(" ", "+")
        st.markdown(f"""
            <div class="video-frame">
                <iframe src="https://www.youtube.com/embed?listType=search&list={search_query}+professional+recipe" frameborder="0" allowfullscreen></iframe>
            </div>
            <p style='text-align:center; color:#34d399; font-weight:bold; letter-spacing:2px;'>LIVE AI VIDEO STREAMING ENABLED</p>
        """, unsafe_allow_html=True)

# --- TAB 2: GLOBAL HERITAGE ENGINE ---
with tab2:
    st.markdown("### THE GLOBAL ENGINE")
    target_food = st.text_input("NAME ANY DISH OR INGREDIENT", placeholder="e.g. Ribeye Steak, Prawns, Lamb...")
    
    if target_food:
        heritage = st.selectbox("CHOOSE CULINARY HERITAGE", 
                                ["Pakistani", "Arab/Egyptian", "Indian", "Asian", "Mexican", "American"])
        
        # 15-STEP WORLD-CLASS LOGIC
        steps = [
            f"<b>Mise En Place:</b> Organize all dry spices and prep 1kg of {target_food}.",
            f"<b>Fat Prep:</b> Heat oil or ghee to <span class='heat-tag high'>HIGH</span> until a cumin seed sizzles instantly.",
            f"<b>Onion Excellence:</b> Sauté onions for 12-15 mins until deep mahogany brown. This is your flavor foundation.",
            f"<b>Aromatic Bloom:</b> Add fresh ginger-garlic paste. Sauté for 2 mins to release the essential oils.",
            f"<b>Spice Hydration:</b> Mix your heritage spices with 2 tbsp water before adding to prevent scorching.",
            f"<b>Searing Phase:</b> Add {target_food}. Flash-sear on max heat to trigger the Maillard reaction for a deep crust.",
            f"<b>Deglazing:</b> Add tomato reduction and scrape the caramelized bits (fond) from the bottom of the pot.",
            f"<b>The Bhuna:</b> Cook intensely until the oil 'breaks' and separates from the spice paste.",
            f"<b>Dairy Tempering:</b> Reduce to <span class='heat-tag med'>MEDIUM</span>. Fold in whisked yogurt or cream slowly.",
            f"<b>Liquid Balance:</b> Add boiling water (never cold) to reach your desired gravy consistency.",
            f"<b>The Seal:</b> Cover with a foil-wrapped lid to trap all micro-aromas.",
            f"<b>Slow Braise:</b> Drop heat to <span class='heat-tag low'>LOW</span>. Simmer for 35 mins until fibers are butter-soft.",
            f"<b>Final Infusion:</b> Add slit green chilies and heritage herbs (Cilantro/Mint/Fenugreek).",
            f"<b>Resting Phase:</b> Turn off all heat. Let the pot sit for 10-12 minutes. Do not open the lid.",
            f"<b>The Reveal:</b> Garnish with fresh ginger matchsticks and serve with aged Basmati rice."
        ]

        # DYNAMIC SEARCH FOR THE CHOSEN DISH
        custom_search = f"{heritage}+{target_food}".replace(" ", "+")
        
        st.markdown(f"""
        <div class="recipe-card">
            <h2 style="color:#34d399; text-align:center;">{heritage.upper()} {target_food.upper()}</h2>
            <div class="video-frame">
                <iframe src="https://www.youtube.com/embed?listType=search&list={custom_search}+pro+chef+recipe" frameborder="0" allowfullscreen></iframe>
            </div>
            <hr style="border:0.1px solid #222; margin: 30px 0;">
            {"".join([f"<p><span class='step-num'>{i+1:02}</span> {s}</p>" for i, s in enumerate(steps)])}
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // GLOBAL ELITE // 2026</p>", unsafe_allow_html=True)
