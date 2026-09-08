# 🍱 Food Product Demand Forecasting Dashboard

## 🇮🇩 Deskripsi Proyek

Dashboard forecasting permintaan produk makanan yang dikembangkan menggunakan **Python dan Streamlit** untuk menganalisis data historis permintaan serta melakukan prediksi kebutuhan produk di masa mendatang.

Project ini menerapkan metode **Time Series Forecasting** menggunakan:

- **Single Exponential Smoothing (SES)**
- **Moving Average (MA)**

dengan optimasi parameter otomatis untuk memperoleh hasil forecasting terbaik berdasarkan evaluasi error.

Dashboard ini dirancang untuk mendukung proses **analisis data, perencanaan produksi, pengelolaan persediaan, dan pengambilan keputusan berbasis data (data-driven decision making).**

---

## 🇬🇧 Project Description

An interactive **food product demand forecasting dashboard** developed using **Python and Streamlit** to analyze historical demand data and predict future product requirements.

This project implements **Time Series Forecasting methods**, including:

- **Single Exponential Smoothing (SES)**
- **Moving Average (MA)**

with automatic parameter optimization to achieve the best forecasting performance based on error evaluation.

The dashboard is designed to support **data analysis, production planning, inventory management, and data-driven decision making.**

---

# ✨ Fitur Utama | Key Features

## 🇮🇩

- Analisis data historis permintaan produk
- Visualisasi tren permintaan
- Pemilihan produk secara interaktif
- Optimasi parameter forecasting secara otomatis
- Perbandingan hasil forecasting dengan berbagai parameter
- Evaluasi akurasi menggunakan metrik error

## 🇬🇧

- Historical demand data analysis
- Demand trend visualization
- Interactive product selection
- Automatic forecasting parameter optimization
- Forecast comparison using different parameters
- Forecast accuracy evaluation using error metrics

---

# 📊 Metode Forecasting | Forecasting Methods

## 1. Single Exponential Smoothing (SES)

### 🇮🇩
Single Exponential Smoothing merupakan metode forecasting yang memberikan bobot lebih besar pada data terbaru untuk melakukan prediksi nilai masa depan.

Pada project ini, parameter smoothing (**α**) dioptimalkan untuk mendapatkan hasil forecasting dengan error minimum.

### 🇬🇧
Single Exponential Smoothing is a forecasting method that assigns higher weights to recent observations to predict future values.

In this project, the smoothing parameter (**α**) is optimized to obtain forecasting results with minimum error.

---

## 2. Moving Average (MA)

### 🇮🇩
Moving Average merupakan metode forecasting yang melakukan perataan data historis berdasarkan rata-rata beberapa periode sebelumnya untuk mengidentifikasi pola permintaan.

Ukuran window terbaik dipilih berdasarkan hasil evaluasi error.

### 🇬🇧
Moving Average is a forecasting method that smooths historical data by calculating the average of previous periods to identify demand patterns.

The optimal window size is selected based on forecasting error evaluation.

---

# 📈 Evaluasi Forecasting | Forecasting Evaluation

## 🇮🇩

Performa forecasting dievaluasi menggunakan:

- **MAPE (Mean Absolute Percentage Error)**
- **SSE (Sum of Squared Error)**

Metrik tersebut digunakan untuk membandingkan performa setiap parameter dan menentukan konfigurasi forecasting terbaik.

## 🇬🇧

Forecasting performance is evaluated using:

- **MAPE (Mean Absolute Percentage Error)**
- **SSE (Sum of Squared Error)**

These metrics are used to compare forecasting performance and determine the optimal forecasting configuration.

---

# 🛠️ Tools & Technologies

```
Python
Streamlit
Pandas
NumPy
Data Visualization
Time Series Forecasting
Statistical Forecasting
```

---

# 📂 Project Structure

```
Food-Product-Demand-Forecasting
│
├── app.py
├── utils.py
├── cek_excel.py
├── test_loader.py
├── TEMPLATE_PRODUK.xlsx
└── requirements.txt
```

---

# 🖥️ Dashboard Preview

(Add dashboard screenshot here)

```
![Dashboard Preview](dashboard.png)
```

---

# 👤 Author

**Nabilah Safa Nur Fatimah**  
S1 Mathematics — Institut Teknologi Sepuluh Nopember
