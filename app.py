import streamlit as st
import datetime

# --- AURA CHEF | THE COMPLETE ELITE TERMINAL v29.0 ---
st.set_page_config(page_title="AURA CHEF | GLOBAL ELITE", page_icon="⚖️", layout="wide")

# --- UI STYLING: THE BLACK ROOM ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 50px; background-color: #000; padding: 25px; border-bottom: 1px solid #1a1a1a; }
    .stTabs [data-baseweb="tab"] { font-size: 0.9rem; font-weight: 900; color: #555; text-transform: uppercase; letter-spacing: 2px; }
    .recipe-card { background: #0a0a0a; padding: 50px; border: 1px solid #1f1f1f; border-radius: 4px; margin-top: 20px; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; font-family: monospace; border: 1px solid #34d399; padding: 4px 10px; }
    .video-container { border: 3px solid #34d399; border-radius: 12px; overflow: hidden; background: #000; }
</style>
""", unsafe_allow_html=True)

# --- DAILY MENU LOGIC ---
menu = {
    0: "Lamb Mandi Biryani Fusion", 1: "Wagyu Garlic Steak", 2: "Royal Butter Chicken",
    3: "Mexican Birria Tacos", 4: "Thai Green Curry", 5: "Authentic Nihari", 6: "Truffle Pasta"
}
day_idx = datetime.datetime.now().weekday()
featured_food = menu[day_idx]

# --- TABS REINSTATED ---
tab1, tab2 = st.tabs(["MASTERCLASS PORTAL", "GLOBAL HERITAGE ENGINE"])

with tab1:
    st.markdown(f"<h1 style='text-align: center; font-weight: 900; letter-spacing:-2px;'>{featured_food.upper()}</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 4, 1])
    with mid:
        st.markdown('<div class="video-container">', unsafe_allow_html=True)
        # THE YETI IS GONE: Replacing with a professional direct-link culinary stream
        # This link is a direct HQ MP4 file.
        chef_video = "https://v.ftcdn.net/05/59/28/94/700_F_559289456_fO6t4jMvX6vX9N7S9oI7yX8H5W7zL9Pj_ST.mp4"
        st.video(chef_video, format="video/mp4", start_time=0)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#34d399; font-weight:bold; margin-top:10px;'>4K KINETIC DATA: ACTIVE</p>", unsafe_allow_html=True)

with tab2:
    st.markdown("### THE GLOBAL ENGINE")
    target_food = st.text_input("WHAT ARE YOU DREAMING OF MAKING?", placeholder="e.g. Ribeye, Prawns, Lamb...")
    
    if target_food:
        heritage = st.selectbox("SELECT CULINARY HERITAGE", ["Pakistani", "Arab/Egyptian", "Indian", "Asian", "Mexican", "American"])
        
        # THE 15-STEP WORLD-CLASS LOGIC
        steps = [
            f"<b>Mise En Place:</b> Organize all dry spices and prep 1kg of {target_food}.",
            "<b>Fat Prep:</b> Heat oil or ghee until a cumin seed sizzles instantly.",
            "<b>Onion Excellence:</b> Sauté onions for 15 mins until deep mahogany brown.",
            "<b>Aromatic Bloom:</b> Add fresh ginger-garlic paste; sauté for 2 mins.",
            "<b>Spice Hydration:</b> Mix heritage spices with water before adding to prevent scorching.",
            f"<b>Maillard Reaction:</b> Add {target_food}. Flash-sear on max heat for a deep crust.",
            "<b>Deglazing:</b> Add tomato reduction and scrape the flavor from the bottom.",
            "<b>The Bhuna:</b> Cook intensely until the oil separates from the spice paste.",
            "<b>Dairy Tempering:</b> Reduce heat; slowly whisk in yogurt or cream.",
            "<b>Liquid Balance:</b> Add boiling water to reach your desired gravy consistency.",
            "<b>The Seal:</b> Cover with a foil-wrapped lid to trap all micro-aromas.",
            "<b>Slow Braise:</b> Simmer on LOW for 35 mins until tender.",
            "<b>Final Infusion:</b> Add slit green chilies and fresh heritage herbs.",
            "<b>Resting Phase:</b> Turn off all heat. Let the pot sit for 12 mins unopened.",
            "<b>The Reveal:</b> Garnish and serve with hot, aged Basmati rice."
        ]

        st.markdown(f"""
        <div class="recipe-card">
            <h2 style="color:#34d399; text-align:center;">{heritage.upper()} {target_food.upper()}</h2>
            {"".join([f"<p><span class='step-num'>{i+1:02}</span> {s}</p>" for i, s in enumerate(steps)])}
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // GLOBAL ELITE // 2026</p>", unsafe_allow_html=True)
