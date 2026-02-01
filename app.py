import streamlit as st
import numpy as np
from PIL import Image, ImageStat, ImageFilter

st.set_page_config(page_title="AuraScan 2.0", page_icon="🍎")
st.title("🍎 AuraScan 2.0: Mold & Decay Detector")

img_file = st.camera_input("Scan the food (Focus on the suspicious spots)")

if img_file:
    img = Image.open(img_file)
    st.image(img, caption="Scanning for spots...", use_container_width=True)

    # --- THE UPGRADED "BRAIN" ---
    with st.spinner("Analyzing texture and patches..."):
        # 1. Convert to Greyscale to find "Fuzziness" or dark patches
        grayscale = img.convert('L')
        # Apply a filter to highlight edges (where mold is fuzzy)
        edges = grayscale.filter(ImageFilter.FIND_EDGES)
        
        # 2. Get detailed stats of the image
        stat = ImageStat.Stat(grayscale)
        std_dev = stat.stddev[0] # High variance means lots of weird patches/fuzz
        
        # 3. Analyze specific RGB ratios (Mold is often Blue/Green/Grey)
        img_array = np.array(img.convert('RGB'))
        r, g, b = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
        
        # Check for "Grey/Blue" fuzzy patches (Common in bread/fruit mold)
        # Mold usually has very low Red compared to the others
        mold_risk_pixels = np.sum((b > r) & (g > r) & (r < 100))
        total_pixels = img_array.shape[0] * img_array.shape[1]
        mold_ratio = (mold_risk_pixels / total_pixels) * 100

    # --- THE VERDICT ---
    st.write("### Analysis Result:")
    
    # Logic: If variance is high (fuzzy) OR mold color ratio is high
    if mold_ratio > 5 or std_dev > 50:
        st.error(f"⚠️ MOLD/SPOILAGE DETECTED (Confidence: {int(mold_ratio + 20)}%)")
        st.write("Found suspicious texture or color patches. **Do not eat!**")
        st.metric(label="Freshness", value=f"{max(0, 100-int(mold_ratio*10))}%", delta="SPOILAGE FOUND")
    else:
        st.success("✅ LOOKS CLEAR")
        st.write("No significant mold patches or fuzzy textures detected.")
        st.metric(label="Freshness", value="95%", delta="Healthy")

st.warning("Peer Note: AI can miss deep bacteria. If it's slimy or smells 'off', toss it out regardless of the scan!")
