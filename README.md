# 📊 Food Product Demand Forecasting Dashboard

## 🇬🇧 English Version

An interactive dashboard for food product demand forecasting using time series analysis with Python and Streamlit.

This project implements forecasting methods:

- Single Exponential Smoothing (SES)
- Moving Average (MA)

The system is designed to analyze historical demand data and generate future demand predictions with optimized parameters.

### Features

- Upload product demand dataset
- Data preprocessing and validation
- Interactive demand visualization
- Automatic parameter optimization
- Forecast generation
- Forecast evaluation using MAPE and SSE


---

# 🇮🇩 Versi Bahasa Indonesia

Dashboard interaktif untuk melakukan peramalan permintaan produk makanan menggunakan analisis time series berbasis Python dan Streamlit.

Project ini menerapkan metode forecasting:

- Single Exponential Smoothing (SES)
- Moving Average (MA)

Sistem ini digunakan untuk menganalisis data permintaan historis dan menghasilkan prediksi permintaan di masa mendatang dengan parameter yang telah dioptimasi.


## ✨ Fitur Utama

- Upload dataset permintaan produk
- Validasi dan preprocessing data
- Visualisasi pola permintaan produk
- Optimasi parameter forecasting otomatis
- Prediksi permintaan periode berikutnya
- Evaluasi performa model menggunakan MAPE dan SSE


---

# 🛠️ Technology Stack

| Technology | Description |
|---|---|
| Python | Programming Language |
| Streamlit | Dashboard Development Framework |
| Pandas | Data Processing |
| NumPy | Numerical Computation |
| Matplotlib | Data Visualization |
| Time Series Analysis | Forecasting Approach |


---

# 📂 Project Structure

```
Food-Product-Demand-Forecasting

│
├── app.py
│
├── 1_Forecasting.py
│
├── 2_Grafik_Per_Produk.py
│
├── 3_Upload_Data.py
│
├── utils.py
│
├── TEMPLATE_PRODUK.xlsx
│
└── requirements.txt
```


---

# 📈 Forecasting Methods

## 1. Single Exponential Smoothing (SES)

Single Exponential Smoothing is used to forecast future demand by applying weighted smoothing to historical demand data.

The optimal smoothing parameter (alpha) is selected based on forecasting error evaluation.


## 2. Moving Average (MA)

Moving Average predicts future demand based on the average value of historical demand within a selected time window.

The optimal window size is determined by comparing forecasting performance.


---

# 📊 Model Evaluation

The forecasting performance is evaluated using:

## MAPE (Mean Absolute Percentage Error)

Measures forecasting accuracy based on the percentage difference between actual and predicted values.


## SSE (Sum of Squared Errors)

Measures the total squared difference between actual demand and forecast results.


---

# 🚀 How to Run

Install required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```


---

# 📌 Project Purpose

This project demonstrates the implementation of time series forecasting methods into an interactive analytics dashboard.

The project combines data processing, forecasting modeling, visualization, and application development using Python.


---

# 👩‍💻 Author
Nabilah Safa Nur Fatimah
**Mathematics Undergraduate Student**  
Institut Teknologi Sepuluh Nopember

Interest:

- Data Analytics
- Forecasting
- Machine Learning
- Optimization
- Computational Modeling
