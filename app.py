import streamlit as st


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Food Product Demand Forecasting",
    page_icon="📊",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>


/* GLOBAL */

html, body, [class*="css"] {

    font-family:
    "Inter",
    "Segoe UI",
    sans-serif;

}


.stApp {

    background:#F8FAFC;

}


/* Hide Streamlit menu */

#MainMenu {
    visibility:hidden;
}


footer {
    visibility:hidden;
}



/* HEADER */

.hero {

    background:white;

    padding:40px;

    border-radius:22px;

    border:1px solid #E2E8F0;

    box-shadow:
    0 10px 30px rgba(15,23,42,0.05);

    margin-bottom:25px;

}



.hero-title {

    font-size:38px;

    font-weight:800;

    color:#0F172A;

}


.hero-subtitle {

    font-size:18px;

    color:#475569;

    line-height:1.6;

}




/* TAG */

.tag {

    display:inline-block;

    background:#EFF6FF;

    color:#2563EB;

    padding:7px 16px;

    border-radius:20px;

    margin-right:8px;

    font-size:14px;

    font-weight:600;

}



/* CARD */

.dashboard-card {

    background:white;

    padding:25px;

    border-radius:18px;

    border:1px solid #E2E8F0;

    height:220px;

    box-shadow:
    0px 8px 25px rgba(15,23,42,0.05);

}



.card-icon {

    width:55px;

    height:55px;

    border-radius:15px;

    background:#EFF6FF;

    display:flex;

    align-items:center;

    justify-content:center;

    font-size:28px;

}



.card-title {

    margin-top:18px;

    font-size:21px;

    font-weight:700;

    color:#0F172A;

}



.card-description {

    margin-top:10px;

    font-size:14px;

    color:#64748B;

    line-height:1.6;

}



/* BUTTON */

.stButton button {


    width:100%;


    margin-top:15px;


    background:#2563EB;


    color:white;


    border:none;


    border-radius:12px;


    height:45px;


    font-weight:600;


}



.stButton button:hover {


    background:#1D4ED8;


    color:white;


}



/* METRIC */

[data-testid="stMetric"] {


    background:white;


    padding:20px;


    border-radius:16px;


    border:1px solid #E2E8F0;


}



</style>

""",
unsafe_allow_html=True)



# ==================================================
# HERO SECTION
# ==================================================


st.markdown("""
<div class="hero">


<div class="hero-title">

📊 Food Product Demand Forecasting Dashboard

</div>


<p class="hero-subtitle">

An interactive analytics platform for forecasting product demand
using <b>Single Exponential Smoothing</b> and
<b>Moving Average</b> methods.

Designed for time series analysis,
demand prediction, and forecasting evaluation.

</p>


<span class="tag">
Python
</span>


<span class="tag">
Streamlit
</span>


<span class="tag">
Time Series
</span>


<span class="tag">
Data Analytics
</span>


</div>

""",
unsafe_allow_html=True)



# ==================================================
# PROJECT OVERVIEW
# ==================================================


st.subheader("📌 Project Overview")


st.write(
"""
This dashboard provides an end-to-end workflow for food product demand forecasting.

Users can upload demand datasets, analyze historical patterns,
generate forecasts, and evaluate model performance using forecasting metrics.
"""
)



# ==================================================
# KPI INFORMATION
# ==================================================


st.write("")


col1,col2,col3 = st.columns(3)


with col1:

    st.metric(
        "Forecast Model",
        "SES & MA"
    )


with col2:

    st.metric(
        "Evaluation Metric",
        "MAPE & SSE"
    )


with col3:

    st.metric(
        "Application",
        "Streamlit Dashboard"
    )



# ==================================================
# MODULE SECTION
# ==================================================


st.divider()


st.subheader("🚀 Dashboard Modules")



def create_module(
        icon,
        title,
        description,
        button,
        key,
        page):


    st.markdown(
    f"""

    <div class="dashboard-card">


    <div class="card-icon">

    {icon}

    </div>


    <div class="card-title">

    {title}

    </div>


    <div class="card-description">

    {description}

    </div>


    </div>


    """,

    unsafe_allow_html=True
    )


    if st.button(button,key=key):

        st.switch_page(page)




col1,col2,col3 = st.columns(3)



with col1:


    create_module(

        "📈",

        "Forecasting",

        """
        Generate future demand predictions using
        Single Exponential Smoothing and Moving Average
        with parameter optimization.
        """,

        "Open Forecasting",

        "forecast",

        "1_Forecasting.py"

    )



with col2:


    create_module(

        "📊",

        "Product Analysis",

        """
        Explore historical demand trends and analyze
        product-level demand patterns through visualization.
        """,

        "Open Analysis",

        "analysis",

        "2_Grafik_Per_Produk.py"

    )



with col3:


    create_module(

        "📂",

        "Data Management",

        """
        Upload and validate Excel datasets before
        performing forecasting analysis.
        """,

        "Open Upload",

        "upload",

        "3_Upload_Data.py"

    )



# ==================================================
# SYSTEM INFORMATION
# ==================================================


st.divider()


st.subheader("⚙️ System Information")


a,b,c = st.columns(3)


with a:

    st.metric(
        "Data Input",
        "Excel (.xlsx)"
    )


with b:

    st.metric(
        "Forecast Type",
        "Time Series"
    )


with c:

    st.metric(
        "Model Evaluation",
        "Error Analysis"
    )



# ==================================================
# GUIDE
# ==================================================


with st.expander("📚 User Guide"):


    st.markdown(
    """

## Workflow

1. Upload product demand dataset
2. Select product data
3. Run forecasting analysis
4. Evaluate forecasting performance


## Supported Dataset

Excel format (.xlsx)

Required columns:

- product
- date
- demand


## Forecasting Methods


### Single Exponential Smoothing (SES)

A forecasting method using smoothing parameters
to predict future demand.


### Moving Average (MA)

A forecasting method based on historical demand windows.


## Evaluation Metrics

- MAPE (Mean Absolute Percentage Error)
- SSE (Sum of Squared Error)


"""
)



# ==================================================
# FOOTER
# ==================================================


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
