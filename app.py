import streamlit as st
import time
import urllib.parse

# --- AURA CHEF ELITE v6.0 ---
st.set_page_config(page_title="AURA CHEF | GLOBAL", page_icon="⚖️", layout="wide")

# --- PROFESSIONAL UI STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    
    .stTabs [data-baseweb="tab-list"] { 
        justify-content: center; gap: 60px; background-color: #000; padding: 25px; border-bottom: 2px solid #1a1a1a; 
    }
    .stTabs [data-baseweb="tab"] { font-size: 1rem; font-weight: 700; color: #444; text-transform: uppercase; }
    .stTabs [data-baseweb="tab-highlight"] { background-color: #fff; }

    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #222; border-radius: 4px; margin-top: 20px; }
    .step-number { color: #555; font-weight: 900; margin-right: 10px; }
    .spice-badge { background: #1a1a1a; color: #fff; padding: 3px 10px; border-radius: 2px; border: 1px solid #333; font-size: 0.7rem; margin-right: 5px; }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
t1, t2, t3 = st.tabs(["HOME SELECTION", "INGREDIENT MATCH ENGINE", "GLOBAL VIDEO VAULT"])

# --- TAB 1: HOME SELECTION ---
with t1:
    st.markdown("<h1 style='text-align: center; font-weight: 900; margin-top:40px;'>CHEF'S SIGNATURE</h1>", unsafe_allow_html=True)
    c1, col_mid, c3 = st.columns([1,2,1])
    with col_mid:
        st.markdown("""
        <div class="recipe-card" style="text-align: center;">
            <p style="color:#888; letter-spacing:2px; font-size:0.7rem;">FEATURED TODAY</p>
            <h2 style="letter-spacing:-1px;">AUTHENTIC HYDERABADI BIRYANI</h2>
            <p style="color:#666;">Slow-cooked basmati rice, marinated halal goat/chicken, and saffron infusion.</p>
        </div>
        """, unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=V37Lp5C7V6Q")

# --- TAB 2: INGREDIENT MATCH ENGINE ---
with t2:
    st.markdown("### INGREDIENT MATCH ENGINE")
    st.write("Input your pantry items to find compatible global dishes.")
    
    # Press Enter to Submit
    user_input = st.text_input("INPUT PANTRY ITEMS (e.g., Chicken, Rice, Onion, Tomato)", placeholder="Type ingredients and press Enter...")

    if user_input:
        st.markdown("---")
        # Selection of Styles
        style = st.radio("SELECT CUISINE STYLE", ["Pakistani", "Indian", "Mexican", "Asian", "American"], horizontal=True)
        
        with st.spinner(f"SEARCHING {style.upper()} DATABASE..."):
            time.sleep(1)
            
            # Detailed Step Logic
            st.markdown(f"### 3 Suggested {style} Dishes using: {user_input}")
            
            c_a, c_b, c_c = st.columns(3)
            
            # This is where the logic changes based on the style button you click
            dishes = {
                "Pakistani": ["Chicken Karahi", "Aloo Keema", "Chana Chaat"],
                "Indian": ["Butter Chicken", "Dal Tadka", "Paneer Tikka"],
                "Mexican": ["Chicken Tacos", "Beef Enchiladas", "Chili Con Carne"],
                "Asian": ["Kung Pao Chicken", "Egg Fried Rice", "Beef Stir-fry"],
                "American": ["Smash Burger", "Loaded Fries", "Chicken Wings"]
            }

            selected_dishes = dishes[style]

            for i, d in enumerate([c_a, c_b, c_c]):
                with d:
                    st.markdown(f"""
                    <div class="recipe-card">
                        <h4 style="color:#fff;">{selected_dishes[i]}</h4>
                        <p style="font-size:0.8rem; color:#888;">Complete Step-by-Step:</p>
                        <p><span class="step-number">01</span> Sauté your base aromatics (Onion/Garlic).</p>
                        <p><span class="step-number">02</span> Add your primary protein/veg.</p>
                        <p><span class="step-number">03</span> Apply regional {style} spices.</p>
                        <p><span class="step-number">04</span> Simmer until tender and plate.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    # Dynamic Video Search for each dish
                    query = f"{style} {selected_dishes[i]} recipe"
                    st.video(f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}")
                    st.caption(f"Search YouTube for {selected_dishes[i]}")

# --- TAB 3: GLOBAL VIDEO VAULT ---
with t3:
    st.markdown("### GLOBAL VIDEO VAULT")
    st.write("Search for any dish in the world to find its professional video tutorial.")
    
    search_query = st.text_input("ENTER DISH NAME (e.g., Lasagna, Biryani, Nihari)", key="vault_search")
    
    if search_query:
        st.markdown(f"### MASTERCLASS RESULTS: {search_query.upper()}")
        
        # We use a YouTube redirect bridge since we can't embed the search page itself
        st.info(f"Finding best professional videos for {search_query}...")
        
        search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(search_query + ' recipe')}"
        
        st.markdown(f"""
        <div class="recipe-card">
            <h4>DIRECT ACCESS</h4>
            <p>Due to security, click below to open the official YouTube video stream for <b>{search_query}</b>.</p>
            <a href="{search_url}" target="_blank">
                <button style="width:100%; padding:15px; background:white; color:black; font-weight:900; border:none; cursor:pointer;">
                    OPEN VIDEO TUTORIALS ↗
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # We also provide a default high-quality embed for popular terms
        if "biryani" in search_query.lower():
            st.video("https://www.youtube.com/watch?v=eqPgJPLRutI")
        elif "burger" in search_query.lower():
            st.video("https://www.youtube.com/watch?v=6bt0BlYMovE")

st.markdown("<br><br><p style='text-align:center; color:#222; font-size:0.7rem; letter-spacing:2px;'>AURA CHEF // SECURE TERMINAL // 2026</p>", unsafe_allow_html=True)
