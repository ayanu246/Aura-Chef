import streamlit as st
import random
import time

# --- PRO TERMINAL CONFIG ---
st.set_page_config(page_title="AURA CHEF | GLOBAL", page_icon="⚖️", layout="wide")

# --- ULTIMATE PROFESSIONAL CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');
    
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #ffffff; }
    
    /* Tabs at the Top */
    .stTabs [data-baseweb="tab-list"] { 
        justify-content: center; gap: 50px; background-color: #000; padding: 20px; border-bottom: 1px solid #222; 
    }
    .stTabs [data-baseweb="tab"] { 
        font-size: 0.9rem; font-weight: 700; letter-spacing: 2px; color: #666; transition: 0.4s;
    }
    .stTabs [data-baseweb="tab"]:hover { color: #fff; }
    .stTabs [data-baseweb="tab-highlight"] { background-color: #fff; height: 2px; }

    /* Recipe Display */
    .recipe-output { 
        background: #0a0a0a; padding: 40px; border-radius: 2px; border: 1px solid #1a1a1a; margin-top: 30px; 
    }
    .badge { padding: 4px 12px; font-size: 0.7rem; font-weight: 900; letter-spacing: 1px; border: 1px solid #444; margin-right: 10px; }
    
    .stButton>button {
        border-radius: 0px; background: #fff; color: #000; font-weight: 900; 
        border: none; padding: 15px 40px; text-transform: uppercase; letter-spacing: 2px;
    }
</style>
""", unsafe_allow_html=True)

# --- GLOBAL NAVIGATION (TOP TABS) ---
tab1, tab2, tab3, tab4 = st.tabs(["SELECTION OF THE DAY", "PANTRY ENGINE", "RANDOMIZER", "GLOBAL ARCHIVE"])

# --- TAB 1: SELECTION OF THE DAY ---
with tab1:
    st.markdown("<h1 style='text-align: center; letter-spacing: -2px; font-weight: 900;'>SIGNATURE SELECTION</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown(f"""
        <div class="recipe-output" style="text-align: center;">
            <span class="badge">HALAL</span><span class="badge">TRENDING</span>
            <h2 style="margin-top:20px;">PAKISTANI CHAPLI BURGER</h2>
            <p style="color: #888;">A fusion of traditional Peshawar flavors and modern American street food. Served with masala fries and mint chutney aioli.</p>
            <hr style="border: 0.1px solid #222;">
            <p style="font-size: 0.8rem; letter-spacing: 1px;">TIME: 35 MINS | DIFFICULTY: INTERMEDIATE</p>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: PANTRY ENGINE (THE CORE WORK) ---
with tab2:
    st.markdown("### PANTRY ENGINE")
    st.caption("INPUT INGREDIENTS TO FILTER GLOBAL DATABASE")
    
    items = st.text_area("LIST ALL AVAILABLE INGREDIENTS", placeholder="Chicken, Soy Sauce, Ginger, Potato, Tortilla...", height=150)
    
    # Global Cuisine Logic
    st.markdown("---")
    c1, c2, c3, c4, c5 = st.columns(5)
    pak = c1.checkbox("PAKISTANI")
    ind = c2.checkbox("INDIAN")
    mex = c3.checkbox("MEXICAN")
    asi = c4.checkbox("ASIAN")
    ame = c5.checkbox("AMERICAN")

    if st.button("EXECUTE ENGINE"):
        with st.spinner("SCANNING CULINARY MATRICES..."):
            time.sleep(1)
            items_l = items.lower()
            
            # Dynamic Cuisine Logic
            if pak or ind:
                res_title = "Aromatic Karahi Fusion"
                res_steps = "1. Temper cumin and cardamom in oil. 2. Sauté aromatics. 3. Slow-simmer protein. 4. Finish with fresh ginger."
            elif mex:
                res_title = "Street Style Street Tacos"
                res_steps = "1. Char tortillas. 2. High-heat sear protein. 3. Create lime-acid reduction. 4. Top with fresh cilantro."
            elif asi:
                res_title = "Wok-Fired Glaze Stir-fry"
                res_steps = "1. High-heat wok prep. 2. Flash-fry vegetables. 3. Deglaze with soy/ginger. 4. Serve over steamed base."
            else:
                res_title = "Standard Professional Service"
                res_steps = "1. Mise en place. 2. Pan-sear protein. 3. Deglaze for sauce. 4. Garnish and plate."

            st.markdown(f"""
            <div class="recipe-output">
                <h3 style="color:#fff;">{res_title}</h3>
                <p style="color:#888;">BASED ON DATA: {items}</p>
                <hr style="border:0.1px solid #222">
                <p>{res_steps}</p>
            </div>
            """, unsafe_allow_html=True)

# --- TAB 3: RANDOMIZER ---
with tab3:
    st.markdown("### CULINARY RANDOMIZER")
    st.write("DECISION ENGINE FOR UNDETERMINED INPUTS")
    
    if st.button("GENERATE RANDOM PROFILE"):
        cuisine_list = ["Pakistani Biryani", "Mexican Enchiladas", "American Smash Burgers", "Indian Butter Chicken", "Asian Ramen"]
        result = random.choice(cuisine_list)
        st.markdown(f"""
        <div class="recipe-output" style="text-align:center;">
            <p class="badge">SYSTEM CHOICE</p>
            <h1 style="color:#fff;">{result}</h1>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 4: GLOBAL ARCHIVE ---
with tab4:
    st.markdown("### GLOBAL CUISINE ARCHIVE")
    st.write("Browse regional food categories.")
    st.info("The archive includes Halal, Vegetarian, and Global variations for all 5 major regions.")
    st.table({
        "Region": ["Pakistani", "American", "Indian", "Asian", "Mexican"],
        "Signature": ["Karahi", "Burgers", "Paneer", "Stir-fry", "Tacos"],
        "Status": ["Halal Only", "Global", "Veg/Halal", "Global", "Halal Option"]
    })

# --- FOOTER ---
st.markdown("<br><br><p style='text-align: center; color: #333; font-size: 0.7rem;'>AURA CHEF // GLOBAL ACCESS // 2026</p>", unsafe_allow_html=True)
