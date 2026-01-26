import streamlit as st
import datetime

# --- AURA CHEF AI v19.0 ---
st.set_page_config(page_title="AURA CHEF | DYNAMIC", page_icon="⚖️", layout="wide")

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
    .vid-button {
        display: block; width: 100%; padding: 20px; background: #fff; color: #000; 
        text-align: center; font-weight: 900; text-decoration: none; border-radius: 4px;
        text-transform: uppercase; letter-spacing: 2px; transition: 0.3s; margin: 20px 0;
    }
    .vid-button:hover { background: #34d399; color: #000; }
</style>
""", unsafe_allow_html=True)

# --- DYNAMIC "FOOD OF THE DAY" LOGIC ---
# This changes based on the actual date
daily_menu = {
    0: "Lamb Mandi Biryani Fusion",
    1: "Wagyu Smash Burgers",
    2: "Creamy Butter Chicken Masterclass",
    3: "Street Style Mexican Birria Tacos",
    4: "Authentic Thai Green Curry",
    5: "Slow-Cooked Nihari",
    6: "Gourmet Truffle Pasta"
}
day_of_week = datetime.datetime.now().weekday()
featured_food = daily_menu[day_of_week]

t1, t2 = st.tabs(["DAILY SIGNATURE SELECTION", "GLOBAL PANTRY ENGINE"])

# --- TAB 1: DYNAMIC DAILY SELECTION ---
with t1:
    st.markdown(f"<h1 style='text-align: center; font-weight: 900; margin-top:40px;'>{featured_food.upper()}</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1,2,1])
    with mid:
        # Build the dynamic YouTube search link
        yt_search = f"https://www.youtube.com/results?search_query=best+professional+{featured_food.replace(' ', '+')}+recipe"
        
        st.markdown(f"""
        <div class="recipe-card" style="text-align:center;">
            <p style="color:#34d399; letter-spacing:3px; font-size:0.7rem;">FEATURED MASTERCLASS</p>
            <p style="color:#666;">Our AI engine has indexed the top-rated professional video for today's selection.</p>
            <a href="{yt_search}" target="_blank" class="vid-button">WATCH BEST {featured_food.upper()} VIDEO ↗</a>
            <p style="font-size:0.8rem; color:#444;">Note: Opens in a new tab to ensure 4K playback quality.</p>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: GLOBAL PANTRY ENGINE (15 STEPS) ---
with t2:
    st.markdown("### GLOBAL PANTRY ENGINE")
    user_dish = st.text_input("WHAT DO YOU HAVE IN MIND?", placeholder="e.g. Chicken, Lamb, Prawns...")
    
    if user_dish:
        heritage = st.selectbox("SELECT HERITAGE STYLE", ["Pakistani", "Arab/Egyptian", "Indian", "Asian", "Mexican", "American"])
        
        # 15-Step logic with f-strings for variable injection
        db = {
            "Pakistani": [
                f"<b>Mise En Place:</b> Prep 1kg {user_dish}; thin-slice 4 onions and crush ginger-garlic.",
                f"<b>Fat Activation:</b> Heat 1/2 cup oil on <span class='heat-tag high'>HIGH</span> until shimmering.",
                f"<b>The Barista:</b> Sauté onions for 12 mins until they reach a deep chocolate brown.",
                f"<b>Aromatic Bloom:</b> Add ginger-garlic paste; sauté for 2 mins to remove raw bite.",
                f"<b>Spice Hydration:</b> Mix Garam Masala and Turmeric with water; add to pot.",
                f"<b>Maillard Reaction:</b> Add {user_dish}. Sear at max heat for 8 mins to lock in juices.",
                f"<b>Tomato Layer:</b> Add 3 chopped tomatoes. Cook until they dissolve into a rich jam.",
                f"<b>The Bhuna:</b> Stir on high heat until the oil separates completely from the masala.",
                f"<b>Dairy Tempering:</b> Reduce to <span class='heat-tag med'>MEDIUM</span>. Fold in whisked yogurt slowly.",
                f"<b>Liquid Balance:</b> Add 1.5 cups boiling water. Never use cold water on hot protein.",
                f"<b>The Seal:</b> Cover with a foil-sealed lid to trap all aromatic steam.",
                f"<b>Slow Braise:</b> Reduce heat to <span class='heat-tag low'>LOW</span>. Simmer for 35 minutes.",
                f"<b>The Scent:</b> Add slit green chilies and dried fenugreek leaves (Kasuri Methi).",
                f"<b>Resting Phase:</b> Turn off heat. Let the pot sit for 10 mins to relax the fibers.",
                f"<b>Final Reveal:</b> Garnish with fresh ginger and serve with aged Basmati rice."
            ]
        }
        
        steps = db.get(heritage, db["Pakistani"])
        custom_yt = f"https://www.youtube.com/results?search_query=best+professional+{heritage}+{user_dish}+recipe+tutorial"

        st.markdown(f"""
        <div class="recipe-card">
            <h2 style="color:#34d399; text-align:center;">{heritage.upper()} {user_dish.upper()} BLUEPRINT</h2>
            <hr style="border:0.1px solid #222">
            <a href="{custom_yt}" target="_blank" class="vid-button">LAUNCH {heritage.upper()} {user_dish.upper()} VIDEO ↗</a>
            {"".join([f"<p><span class='step-num'>{i+1:02}</span> {s}</p>" for i, s in enumerate(steps)])}
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // AI SECURE TERMINAL // 2026</p>", unsafe_allow_html=True)
