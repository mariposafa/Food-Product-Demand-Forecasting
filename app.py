import streamlit as st


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Food Product Demand Forecasting",
    page_icon="📊",
    layout="wide"
)


# =========================
# GLOBAL STYLE
# =========================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: "Inter", "Segoe UI", sans-serif;
}


.stApp {
    background-color: #F8FAFC;
}


/* Hide default menu */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* Title */

h1 {
    color: #0F172A;
    font-weight: 800;
}


h2 {
    color: #1E293B;
}


/* Cards */

.dashboard-card {

    background:white;
    padding:25px;
    border-radius:18px;

    border:1px solid #E2E8F0;

    box-shadow:
    0px 8px 24px rgba(15,23,42,0.06);

    height:230px;

}


.card-icon {

    width:55px;
    height:55px;

    background:#EFF6FF;

    border-radius:14px;

    display:flex;
    align-items:center;
    justify-content:center;

    font-size:28px;

}


.card-title {

    margin-top:15px;

    font-size:20px;

    font-weight:700;

    color:#0F172A;

}


.card-text {

    color:#64748B;

    font-size:14px;

    line-height:1.6;

}


/* Button */

.stButton button {

    width:100%;

    border-radius:12px;

    background:#2563EB;

    color:white;

    border:none;

    height:45px;

    font-weight:600;

}


.stButton button:hover {

    background:#1D4ED8;

    color:white;

}


/* Metrics */

[data-testid="stMetric"] {

    background:white;

    padding:20px;

    border-radius:16px;

    border:1px solid #E2E8F0;

}


</style>

""", unsafe_allow_html=True)



# =========================
# HERO SECTION
# =========================


st.markdown(
"""
<div style="
background:white;
padding:35px;
border-radius:20px;
border:1px solid #E2E8F0;
margin-bottom:30px;
">

<h1>
📊 Food Product Demand Forecasting Dashboard
</h1>


<p style="
font-size:18px;
color:#475569;
">

Interactive analytics platform for demand forecasting
using <b>Single Exponential Smoothing</b> and
<b>Moving Average</b> methods.

</p>


</div>
""",
unsafe_allow_html=True
)



# =========================
# KPI
# =========================


c1,c2,c3 = st.columns(3)


with c1:
    st.metric(
        "Forecasting Method",
        "SES & MA"
    )


with c2:
    st.metric(
        "Data Processing",
        "Automated"
    )


with c3:
    st.metric(
        "Platform",
        "Streamlit"
    )



st.write("")



# =========================
# MODULE SECTION
# =========================


st.subheader("🚀 Dashboard Modules")


col1,col2,col3 = st.columns(3)



def module_card(icon,title,text,button,key,page):

    st.markdown(
    f"""
    <div class="dashboard-card">

    <div class="card-icon">
    {icon}
    </div>

    <div class="card-title">
    {title}
    </div>

    <div class="card-text">
    {text}
    </div>


    </div>

    """,
    unsafe_allow_html=True
    )


    if st.button(button,key=key):
        st.switch_page(page)



with col1:

    module_card(
        "📈",
        "Forecasting",
        "Generate demand prediction using SES and Moving Average with optimized parameters.",
        "Open Forecasting",
        "forecast",
        "pages/1_Forecasting.py"
    )


with col2:

    module_card(
        "📊",
        "Product Analysis",
        "Explore historical demand trends and visualize product behavior.",
        "Open Analysis",
        "analysis",
        "pages/2_Grafik_Per_Produk.py"
    )


with col3:

    module_card(
        "📂",
        "Data Upload",
        "Upload Excel dataset for forecasting and analysis.",
        "Open Upload",
        "upload",
        "pages/3_Upload_Data.py"
    )



# =========================
# SYSTEM INFORMATION
# =========================


st.divider()


st.subheader("ℹ️ System Information")


a,b,c = st.columns(3)


with a:
    st.metric(
        "Forecast Model",
        "Time Series"
    )


with b:
    st.metric(
        "Evaluation",
        "MAPE & SSE"
    )


with c:
    st.metric(
        "Interface",
        "Interactive Dashboard"
    )



# =========================
# GUIDE
# =========================


with st.expander("📚 User Guide"):

    st.markdown("""

### Workflow

1. Upload demand dataset
2. Select product
3. Run forecasting model
4. Evaluate forecasting performance


### Supported Data Format

Excel (.xlsx)

Required columns:

- produk
- tanggal
- permintaan


### Available Methods

**Single Exponential Smoothing**

Forecasting method using smoothing parameter optimization.


**Moving Average**

Forecasting method based on historical demand window.


### Evaluation Metrics

- MAPE
- SSE

""")


# =========================
# FOOTER
# =========================


st.divider()


st.markdown(
"""
<center>

<b>
Food Product Demand Forecasting Dashboard
</b>

<br>

Built with Python & Streamlit

<br>

Data Analytics Portfolio Project

</center>

""",
unsafe_allow_html=True
)
