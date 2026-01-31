import streamlit as st
import pandas as pd
import numpy as np

# --- ELITE TERMINAL CONFIG ---
st.set_page_config(page_title="AURUM | WEALTH TERMINAL", page_icon="💰", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .metric-card {
        background: #0a0a0a; border: 1px solid #1f1f1f; padding: 25px; border-radius: 10px;
        text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .status-online { color: #34d399; font-weight: 900; font-size: 0.8rem; }
    .gold-text { color: #fbbf24; font-weight: 900; }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
c1, c2 = st.columns([3, 1])
with c1:
    st.markdown("<h1 style='letter-spacing:-2px; font-weight:900;'>AURUM <span style='color:#34d399;'>CORE</span></h1>", unsafe_allow_html=True)
    st.markdown("<p class='status-online'>● ENCRYPTED TERMINAL ACTIVE // 2026</p>", unsafe_allow_html=True)

with c2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("SECURE LOGOUT")

st.write("---")

# --- HIGH-LEVEL METRICS ---
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown('<div class="metric-card"><h4>TOTAL LIQUIDITY</h4><h2 style="color:#34d399;">$1.24M</h2><p style="color:gray;">+12.4%</p></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="metric-card"><h4>ASSET VALUATION</h4><h2 style="color:#fbbf24;">$4.82M</h2><p style="color:gray;">STABLE</p></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="metric-card"><h4>ACTIVE VENTURES</h4><h2>14</h2><p style="color:#34d399;">3 NEW</p></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="metric-card"><h4>RISK INDEX</h4><h2 style="color:#f87171;">LOW</h2><p style="color:gray;">HEDGED</p></div>', unsafe_allow_html=True)

# --- MAIN ENGINE TABS ---
tab1, tab2, tab3 = st.tabs(["MARKET INTELLIGENCE", "ASSET ARCHITECT", "REVENUE PIPELINE"])

with tab1:
    st.markdown("### GLOBAL PERFORMANCE INDEX")
    # Generating dummy million-dollar data
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Venture A', 'Venture B', 'Crypto Index'])
    st.line_chart(chart_data)

with tab2:
    st.markdown("### BUILD NEW ASSET CLASS")
    c1, c2 = st.columns(2)
    with c1:
        asset_name = st.text_input("ASSET NAME", placeholder="e.g., Dubai Real Estate Fund")
        asset_type = st.selectbox("CATEGORY", ["Real Estate", "Tech Startup", "Commodities", "Luxury Goods"])
    with c2:
        investment = st.number_input("INITIAL CAPITAL ($)", min_value=10000, value=100000, step=10000)
        st.markdown(f"<br><h3 class='gold-text'>EST. ROI: ${investment * 1.4:,.2f}</h3>", unsafe_allow_html=True)

with tab3:
    st.markdown("### REVENUE STREAM LOGIC")
    st.table({
        "Source": ["SaaS Platform", "E-com Network", "Real Estate", "Private Equity"],
        "Monthly Yield": ["$42,000", "$18,500", "$12,000", "$95,000"],
        "Status": ["Scaling", "Optimization", "Passive", "Growth"]
    })

st.markdown("<br><p style='text-align:center; color:#333; font-size:0.7rem;'>AURUM GLOBAL SYSTEMS // PRIVATE ACCESS ONLY</p>", unsafe_allow_html=True)
