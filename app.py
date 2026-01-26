import streamlit as st

# --- AURA CHEF AI v17.0: THE KINETIC FUSION ---
st.set_page_config(page_title="AURA CHEF | KINETIC", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .recipe-card { background: #0a0a0a; padding: 45px; border: 1px solid #1f1f1f; border-radius: 4px; line-height: 1.8; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; font-family: monospace; border: 1px solid #34d399; padding: 2px 8px; }
    .heat-tag { font-weight: bold; padding: 2px 8px; border-radius: 2px; font-size: 0.75rem; text-transform: uppercase; }
    .high { background: #471111; color: #ff4b4b; }
    .med { background: #473211; color: #ffa500; }
    .low { background: #112247; color: #4b96ff; }
    .fusion-header { text-align: center; border: 1px solid #333; padding: 20px; margin-bottom: 30px; background: linear-gradient(180deg, #000 0%, #0a0a0a 100%); }
</style>
""", unsafe_allow_html=True)

# --- FUSION ENGINE: LAMB MANDI x BIRYANI ---
st.markdown("""
<div class="fusion-header">
    <p style="color:#34d399; letter-spacing:5px; font-size:0.7rem;">KINETIC RENDER ACTIVE</p>
    <h1 style="font-weight:900; margin:0;">LAMB MANDI BIRYANI FUSION</h1>
    <p style="color:#666;">Yemeni Hawayij Spice Profile // Indo-Pak Dum Layering</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### THE HAWAYIJ MARINADE")
    st.info("AI Note: Hawayij provides the 'Golden' Mandi glow without the heavy chili heat of traditional Biryani.")
    st.write("* **Black Pepper:** 6 parts\n* **Cumin:** 4 parts\n* **Turmeric:** 3 parts (The glow)\n* **Cardamom:** 2 parts\n* **Cloves:** 1 part")

with col2:
    st.markdown("### THE DUM ARCHITECTURE")
    st.warning("Critical: The rice must be exactly 70% cooked (Al-Dente) before layering to prevent mushiness.")

# --- THE 15-STEP MASTERCLASS ---
steps = [
    "<b>Mise En Place:</b> Prep 1kg Lamb Shanks; soak 3 cups aged Basmati for 60 mins.",
    "<b>Aromatic Toasting:</b> Dry roast Hawayij whole spices until oils surface, then grind to a fine powder.",
    "<b>The Gold Coat:</b> Rub lamb with Hawayij, saffron water, and oil. Marinate for 4 hours.",
    "<b>Fat Initiation:</b> Heat Ghee in a Dutch oven on <span class='heat-tag high'>HIGH</span>.",
    "<b>Searing:</b> Sear lamb shanks until a dark gold crust forms (The Maillard Effect).",
    "<b>Braising:</b> Add 2 whole Loomi (dried limes) and water. Simmer on <span class='heat-tag low'>LOW</span> for 90 mins.",
    "<b>Broth Extraction:</b> Remove lamb; strain the braising liquid to use as the rice base.",
    "<b>Rice Parboiling:</b> Boil rice in salted water with cloves and cardamom until it has a 'slight snap'.",
    "<b>The First Layer:</b> Place 40% of the rice at the bottom of a heavy pot.",
    "<b>Meat Integration:</b> Place the tender lamb shanks over the first rice bed.",
    "<b>Biryani Layering:</b> Top with remaining rice, fried onions (Barista), mint, and cilantro.",
    "
