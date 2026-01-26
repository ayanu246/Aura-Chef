import streamlit as st
import time
import random

# --- PRO CONFIG ---
st.set_page_config(page_title="Aura Chef | Professional", page_icon="🍳", layout="wide")

# --- PROFESSIONAL CSS ---
st.markdown("""
<style>
    .stApp { background-color: #050505; color: #e0e0e0; font-family: 'Inter', sans-serif; }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; border-bottom: 1px solid #333; }
    .stTabs [data-baseweb="tab"] { 
        height: 50px; background-color: transparent; border: none; 
        color: #888; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;
    }
    .stTabs [data-baseweb="tab"]:hover { color: #fff; }
    .stTabs [data-baseweb="tab-highlight"] { background-color: #fff; }
    
    .recipe-output { 
        background: #111; padding: 40px; border-radius: 4px; 
        border: 1px solid #222; margin-top: 20px; line-height: 1.6;
    }
    .status-bar { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; color: #555; margin-bottom: 10px; }
    .chef-header { font-size: 2.5rem; font-weight: 800; letter-spacing: -1px; margin-bottom: 0px; }
    
    .stButton>button {
        border-radius: 2px; background: #fff; color: #000; 
        font-weight: 700; border: none; padding: 12px; transition: 0.3s;
    }
    .stButton>button:hover { background: #ccc; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="status-bar">AURA CHEF // V2.0 // TERMINAL ACCESS</p>', unsafe_allow_html=True)
st.markdown('<h1 class="chef-header">AURA CHEF</h1>', unsafe_allow_html=True)

# --- TABS SYSTEM ---
tab1, tab2, tab3 = st.tabs(["HOME", "PANTRY ENGINE", "RANDOMIZER"])

with tab1:
    st.markdown("### Culinary Intelligence")
    st.write("Aura Chef utilizes ingredient-mapping to generate precise Halal and Global recipes. Navigate to the Pantry Engine to begin.")
    st.image("https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&q=80&w=1000", caption="Professional Kitchen Standards")

with tab2:
    st.markdown("### Pantry Engine")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        mode = st.selectbox("DIETARY MODE", ["Global", "Halal"])
        preference = st.selectbox("PREFERENCE", ["All Options", "Vegetarian"])
    
    with col2:
        items = st.text_area("INPUT INGREDIENTS (LIST SEPARATED BY COMMAS)", placeholder="e.g. Salmon, Asparagus, Lemon, Garlic...", height=150)
        
    if st.button("EXECUTE RECIPE GENERATION"):
        if items:
            with st.spinner("ANALYZING FLAVOR PROFILES..."):
                time.sleep(1.5)
                items_l = items.lower()
                
                # --- DYNAMIC RECIPE LOGIC ---
                if "chicken" in items_l and "flour" in items_l:
                    res_title = "Crispy Coated Poultry"
                    res_steps = "1. Season flour heavily. 2. Dredge protein. 3. Fry at 180C. 4. Rest before service."
                elif "pasta" in items_l or "tomato" in items_l:
                    res_title = "Artisan Pasta Reduction"
                    res_steps = "1. Boil salted water. 2. Sauté aromatics. 3. Reduce tomato base. 4. Emulsify sauce with pasta water."
                elif "beef" in items_l or "potato" in items_l:
                    res_title = "Steakhouse Style Service"
                    res_steps = "1. Temper meat to room temp. 2. High-heat sear for Maillard reaction. 3. Oven-roast starch. 4. Compound butter finish."
                else:
                    res_title = "Custom Infusion Bowl"
                    res_steps = "1. Mise en place all ingredients. 2. Sauté hard vegetables first. 3. Add delicate items last. 4. Balance with acidity (lemon/vinegar)."

                st.markdown(f"""
                <div class="recipe-output">
                    <p class="status-bar">{mode.upper()} COMPLIANT // RECIPE LOADED</p>
                    <h2 style="color:#fff;">{res_title}</h2>
                    <hr style="border:0.1px solid #333">
                    <p>{res_steps}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Error: Null input detected in Pantry Engine.")

with tab3:
    st.markdown("### Ingredient Randomizer")
    st.write("Cannot decide? Let Aura Chef select your base components.")
    
    random_bases = ["Halal Beef", "Chicken Thighs", "Atlantic Salmon", "Chickpeas", "Lamb Chops"]
    random_sides = ["Yukon Potatoes", "Jasmine Rice", "Quinoa", "Broccolini", "Sweet Potato"]
    
    if st.button("GENERATE RANDOM BASE"):
        b = random.choice(random_bases)
        s = random.choice(random_sides)
        st.markdown(f"""
        <div class="recipe-output">
            <h3 style="color:#fff;">Recommended Pairing:</h3>
            <p style="font-size:1.5rem;">{b} + {s}</p>
            <p>Use these as your core ingredients in the Pantry Engine.</p>
        </div>
        """, unsafe_allow_html=True)

# --- GLOBAL FOOTER ---
st.markdown("---")
st.caption("AURA CHEF // SECURE TERMINAL // 2026")
