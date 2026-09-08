import streamlit as st
from utils import load_multisheet_excel
import pandas as pd
from datetime import datetime

# ============ FOOD PRODUCT DATA UPLOAD THEME =============

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #eff6ff 100%);
    }

    h1, h2, h3 {
        color: #0F172A !important;
        font-weight: 700 !important;
    }

    .stFileUploader {
        border: 2px dashed #2563EB !important;
        border-radius: 15px !important;
        padding: 30px !important;
        background: rgba(37, 99, 235, 0.05) !important;
    }

    .stFileUploader:hover {
        background: rgba(37, 99, 235, 0.1) !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
    }

    .stats-card {
        background: white;
        border-radius: 16px;
        padding: 20px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 6px 20px rgba(15,23,42,0.06);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


# ============ HEADER =============

st.markdown("""
<div style="text-align:center; padding:20px 0;">

<h1 style="font-size:2.4rem;">
📁 Upload & Data Preview
</h1>

<p style="color:#64748B; font-size:1.05rem;">
Upload product demand dataset for forecasting analysis and visualization
</p>

</div>
""", unsafe_allow_html=True)


# ============ FILE UPLOAD =============

st.markdown("### 📤 Upload Excel Dataset")

uploaded_file = st.file_uploader(
    "Select Excel File (.xlsx)",
    type=["xlsx"],
    help="Required columns: produk, tanggal, permintaan",
    label_visibility="collapsed"
)


# ============ MAIN CONTENT =============

if uploaded_file:

    try:

        df = load_multisheet_excel(uploaded_file)

        st.success(f"✅ Dataset uploaded successfully: {uploaded_file.name}")


        col1, col2, col3 = st.columns(3)


        with col1:
            st.markdown(f"""
            <div class="stats-card">
            <div>Total Data</div>
            <h2>{len(df):,}</h2>
            </div>
            """, unsafe_allow_html=True)


        with col2:
            st.markdown(f"""
            <div class="stats-card">
            <div>Total Products</div>
            <h2>{df['produk'].nunique()}</h2>
            </div>
            """, unsafe_allow_html=True)


        with col3:

            date_range = (
                f"{df['tanggal'].min().strftime('%d/%m/%Y')} - "
                f"{df['tanggal'].max().strftime('%d/%m/%Y')}"
            )

            st.markdown(f"""
            <div class="stats-card">
            <div>Data Period</div>
            <h4>{date_range}</h4>
            </div>
            """, unsafe_allow_html=True)



        st.markdown("### 👁️ Data Preview (First 10 Rows)")

        st.dataframe(
            df.head(10),
            use_container_width=True,
            height=350
        )


        st.markdown("### 📦 Product Overview")

        produk_list = df["produk"].unique()

        for i, produk in enumerate(produk_list[:5]):

            data_produk = df[df["produk"] == produk]

            st.write(
                f"**{i+1}. {produk}** - {len(data_produk)} data points"
            )


        if len(produk_list) > 5:
            st.caption(
                f"...and {len(produk_list)-5} other products"
            )


        st.markdown("### 💾 Export Data")


        csv_data = df.to_csv(index=False).encode("utf-8")


        st.download_button(
            label="📥 Download CSV",
            data=csv_data,
            file_name=f"food_product_demand_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True
        )


        if st.button(
            "📊 Continue to Forecasting",
            use_container_width=True
        ):

            st.switch_page("1_Forecasting.py")


    except Exception as e:

        st.error(
            f"❌ Error processing dataset: {str(e)}"
        )

        st.info(
            "Ensure Excel format contains columns: produk, tanggal, permintaan"
        )


else:


    st.markdown("""
    <div style="
    text-align:center;
    padding:40px;
    background:white;
    border-radius:18px;
    border:2px dashed #2563EB;
    margin:30px 0;
    ">

    <div style="font-size:60px;">
    📁
    </div>

    <h3>
    Upload Food Product Dataset
    </h3>

    <p style="color:#64748B;">
    Drag and drop Excel file or select file manually
    </p>

    <b style="color:#2563EB;">
    Supported format: Excel (.xlsx)
    </b>

    </div>
    """, unsafe_allow_html=True)



    with st.expander("📋 Required Data Format"):

        st.markdown("""

| Column | Format | Example |
|---|---|---|
| produk | Text | Product A |
| tanggal | Date | 2024-01-01 |
| permintaan | Number | 150000 |

### Notes:
- File format must be .xlsx
- Column names must match
- Date format should be standard
- Zero demand values are allowed

        """)



# ============ FOOTER =============

st.markdown("""
<div style="
text-align:center;
margin-top:40px;
padding-top:20px;
border-top:1px solid #E2E8F0;
color:#64748B;
font-size:12px;
">

Food Product Demand Data Management © 2025

</div>
""", unsafe_allow_html=True)
