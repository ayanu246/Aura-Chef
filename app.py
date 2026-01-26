import streamlit as st
import time

# --- AURA CHEF ELITE v10.0 ---
st.set_page_config(page_title="AURA CHEF | INTELLIGENCE", page_icon="⚖️", layout="wide")

# --- PRO TERMINAL STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 50px; background-color: #000; padding: 20px; border-bottom: 2px solid #1a1a1a; }
    .stTabs [data-baseweb="tab"] { font-size: 0.9rem; font-weight: 700; color: #444; text-transform: uppercase; }
    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #222; border-radius: 4px; margin-top: 20px; line-height: 1.8; }
    .step-tag { color: #34d399; font-weight: 900; margin-right: 10px; font-family: monospace; }
    .heat-high { color: #ff4b4b; font-weight: bold; }
    .heat-med { color: #ffa500; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

t1, t2, t3 = st.tabs(["MASTERCLASS", "THE PANTRY ENGINE", "VIDEO SEARCH"])

# --- TAB 2: THE PANTRY ENGINE (FIXED LOGIC) ---
with t2:
    st.markdown("### CULINARY LOGIC ENGINE")
    dish = st.text_input("WHAT IS THE MAIN ITEM? (e.g. Chicken, Beef, Potato)", placeholder="Enter and press Enter...")
    
    if dish:
        style = st.radio("SELECT STYLE", ["Pakistani", "Mexican", "American"], horizontal=True)
        
        # --- TRUE LOGIC ENGINE ---
        if style == "Pakistani":
            title = f"DUM-STYLE {dish.upper()} CURRY"
            spices = "Garam Masala, Turmeric, Kashmiri Red Chili, Ginger/Garlic Paste."
            steps = [
                "HEATING: Set burner to <span class='heat-high'>HIGH</span>. Heat 3 tbsp oil until shimmering.",
                "BASE: Sauté finely sliced onions for 8-10 mins until deep golden brown (do not burn).",
                "INFUSION: Add Ginger/Garlic paste. Fry for 2 mins until the raw smell disappears.",
                "COOKING: Add your " + dish + " and spices. Sear for 5 mins to lock in juices.",
                "DUM: Add 1/2 cup water, cover tightly, and reduce to <span class='heat-med'>LOW</span> for 15-20 mins."
            ]
            yt_query = f"authentic+pakistani+{dish}+recipe"

        elif style == "Mexican":
            title = f"FIRE-SEARED {dish.upper()} TACOS"
            spices = "Smoked Paprika, Ground Cumin, Dried Oregano, Chili Powder."
            steps = [
                "HEATING: Set heavy skillet to <span class='heat-high'>MAX HEAT</span>. Oil should be smoking slightly.",
                "SEARING: Toss " + dish + " in spices. Place in pan. Do not move for 3 mins to get a char.",
                "ACIDITY: Squeeze fresh lime juice over the pan to deglaze the flavorful brown bits.",
                "ASSEMBLY: Warm tortillas on the open flame for 30 seconds per side.",
                "FINISH: Top with raw white onions and cilantro for authentic street-style crunch."
            ]
            yt_query = f"mexican+street+style+{dish}+tacos"

        else: # American
            title = f"CLASSIC GOURMET {dish.upper()} BASKET"
            spices = "Garlic Powder, Onion Powder, Black Pepper, Smoked Sea Salt."
            steps = [
                "PREP: Season " + dish + " heavily and let it sit for 10 mins at room temperature.",
                "HEATING: Set pan to <span class='heat-med'>MEDIUM-HIGH</span> with butter and oil mix.",
                "COOKING: Sear " + dish + " until internal temp is safe. Baste with melted butter.",
                "SIDES: Use the same pan to toast your buns or fry your potatoes in the leftover fats.",
                "SERVICE: Serve with a garlic-mayo aioli base."
            ]
            yt_query = f"gourmet+american+{dish}+recipe"

        st.markdown(f"""
        <div class="recipe-card">
            <h2 style="color:#34d399;">{title}</h2>
            <p><b>SPICES REQUIRED:</b> {spices}</p>
            <hr style="border:0.1px solid #333">
            {"".join([f"<p><span class='step-tag'>STEP {i+1}</span> {s}</p>" for i, s in enumerate(steps)])}
            <br>
            <a href="https://www.youtube.com/results?search_query={yt_query}" target="_blank" 
               style="text-decoration:none;">
               <button style="width:100%; padding:15px; background:white; color:black; font-weight:900; border:none; cursor:pointer;">
               WATCH BEST {style.upper()} {dish.upper()} TUTORIAL ↗
               </button>
            </a>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 3: VIDEO SEARCH (DYNAMIC) ---
with t3:
    st.markdown("### GLOBAL VIDEO VAULT")
    search_q = st.text_input("TYPE ANY DISH (e.g. Biryani, Pasta, Ramen)")
    if search_q:
        st.markdown(f"### Results for: {search_q.upper()}")
        # This button actually builds the perfect search string for YouTube
        final_url = f"https://www.youtube.com/results?search_query=best+professional+{search_q.replace(' ', '+')}+recipe"
        st.markdown(f"""
        <div class="recipe-card" style="text-align:center;">
            <h4>ENGINE SEARCH COMPLETE</h4>
            <p>Find the top-rated professional chef for {search_q}.</p>
            <a href="{final_url}" target="_blank">
                <button style="width:50%; padding:15px; background:#34d399; color:black; font-weight:900; border:none; cursor:pointer;">
                OPEN YOUTUBE SELECTION ↗
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 1: MASTERCLASS ---
with t1:
    st.markdown("<h1 style='text-align: center; font-weight: 900; margin-top:50px;'>SIGNATURE MASTERCLASS</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1,2,1])
    with mid:
        st.markdown("""
        <div class="recipe-card" style="text-align: center;">
            <p style="color:#888; letter-spacing:2px; font-size:0.7rem;">FEATURED: PAKISTANI CLASSIC</p>
            <h2>Chicken Karahi Masterclass</h2>
            <p style="color:#666;">High-heat, no-water traditional method.</p>
        </div>
        """, unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=eqPgJPLRutI")

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // SECURE TERMINAL // 2026</p>", unsafe_allow_html=True)
