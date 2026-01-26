import streamlit as st
import time

# --- APP CONFIG ---
st.set_page_config(page_title="Aura Chef", page_icon="🍳", layout="centered")

# --- UI STYLE ---
st.markdown("""
<style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    .recipe-card { 
        background: #161b22; 
        padding: 25px; 
        border-radius: 20px; 
        border: 1px solid #30363d;
        margin-top: 20px;
    }
    .badge { padding: 5px 15px; border-radius: 50px; font-size: 0.8rem; font-weight: bold; }
    .halal { background: #065f46; color: #34d399; }
    .global { background: #1f6feb; color: #f0f6fc; }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(90deg, #ff8c00, #ff4500);
        color: white;
        font-weight: bold;
        border: none;
        padding: 15px;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("👨‍🍳 Aura Chef")
st.markdown("### *Universal Flavor. Halal Friendly. Zero Waste.*")

# --- SIDEBAR ---
with st.sidebar:
    st.header("Chef's Settings")
    mode = st.radio("Dietary Mode", ["Global Mode", "Halal Mode 🌙"])
    diet = st.radio("Preference", ["Meat & Veg", "Vegetarian Only"])
    st.divider()
    st.caption("Aura Chef v1.0")

# --- RECIPE OF THE DAY ---
st.subheader("🌟 Aura Selection of the Day")
if mode == "Halal Mode 🌙":
    daily_name = "Aura Halal Smash Burgers & Peri Fries"
    badge = '<span class="badge halal">🌙 HALAL SELECTION</span>'
else:
    daily_name = "Classic Double Cheeseburgers & Fries"
    badge = '<span class="badge global">🌎 GLOBAL SELECTION</span>'

st.markdown(f"""
<div class="recipe-card">
    {badge}
    <h2 style="margin-top:10px;">{daily_name}</h2>
    <p>Fresh patties, melted cheese, signature Aura spice blend, and crispy fries.</p>
</div>
""", unsafe_allow_html=True)

# --- INGREDIENT INPUT ---
st.markdown("---")
st.subheader("🧺 What's in your pantry?")
items = st.text_area("List all ingredients (No limit!):", 
                     placeholder="Example: Chicken, potato, buns, garlic, mayo, paprika...", height=150)

if st.button("🚀 GENERATE AURA RECIPE"):
    if not items:
        st.warning("The Aura Chef needs ingredients to work his magic!")
    else:
        with st.spinner("Analyzing ingredients for maximum flavor..."):
            time.sleep(1.5)
            st.markdown(f"""
            <div class="recipe-card" style="border-top: 4px solid #ff4500;">
                <h4>The Aura Comfort Plate</h4>
                <p><i>Tailored for your ingredients: {items}</i></p>
                <hr style="border:0.1px solid #30363d">
                <strong>1. Preparation:</strong> Chop your veggies and prep your protein. Sliced potatoes go into cold water for extra crunch.<br><br>
                <strong>2. The Fries:</strong> Pat potatoes dry. Fry at 160°C until soft, then 190°C until golden brown.<br><br>
                <strong>3. The Main:</strong> Season your protein with the ingredients you listed. Sear on high heat for that perfect crust.<br><br>
                <strong>4. Plating:</strong> Stack it high, add your sauces, and serve with the fries.
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
