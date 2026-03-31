# 🌞 Solar Maintenance App

### ⚡ Machine Learning for Solar Fault Detection & Predictive Maintenance

## 📌 Overview

The **Solar Maintenance App** is an end-to-end machine learning system designed to monitor solar plant performance and detect faults early.

It leverages **Performance Ratio (PR)** and classification models to transform raw solar data into **actionable insights**, enabling proactive maintenance and reducing system downtime.

## 🧠 Key Highlights

* ⚡ Real-world **solar performance monitoring system**
* 🧠 ML-based **fault detection pipeline**
* ⚖️ Handles **imbalanced datasets effectively**
* 🎯 Focus on **fault recall (critical in production systems)**
* 📊 Interactive **Streamlit dashboard**

## 🚀 Features

* 📊 Performance Ratio (PR) computation
* ⚠️ Binary classification:

  * Normal
  * Abnormal
* 🔍 Abnormal classification:

  * Warning
  * Fault
* 🧠 XGBOOST for imbalance
* 📉 Threshold-based decision logic
* 📊 Visual monitoring dashboard

### Pipeline:

1. **Data Collection** → Solar operational data
2. **Preprocessing** → Cleaning & feature engineering
3. **PR Calculation** → Efficiency metric
4. **Model Training** → Binary classification
5. **Post-processing** → Warning vs Fault
6. **Visualization** → Dashboard insights

---

## 📂 Project Structure

```bash
Solar_MAintenance_App/
│
├── Plant_1_Generation_Data.csv      # Raw solar power generation data
├── Plant_1_Weather_Sensor_Data.csv  # Weather sensor readings (irradiance, temperature, etc.)
├── final_solar_dataset.csv          # Cleaned and merged dataset used for modeling
│
├── check_data.ipynb                 # Data exploration, cleaning, and preprocessing notebook
├── train_model.ipynb                # Model training, evaluation, and experimentation
│
├── streamlit_app.py                 # Streamlit dashboard for visualization & predictions
├── requirements.txt                 # Project dependencies
│
└── README.md                        # Project documentation
```

---

## ⚙️ Methodology

### 📊 Performance Ratio (PR)

Core metric used to evaluate solar efficiency.

---

### 🧠 Modeling Approach

* Binary classification:

  * Normal vs Abnormal
* Abnormal split into:

  * Warning
  * Fault

---

### ⚖️ Handling Imbalanced Data

* Implemented **XGBOOST**
* Improved learning on minority (Abnormal) class

---

### 📈 Evaluation Metrics

* Precision
* Recall
* F1-score
* 🚨 Focus: **Abnormal Recall (most critical metric)**

---

## 🛠️ Tech Stack

* **Python**
* **Scikit-learn**
* **Imbalanced-learn**
* **Pandas / NumPy**
* **Streamlit**

---

## ▶️ Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/Codaks-py/Solar_MAintenance_App.git
cd Solar_MAintenance_App
```

### 2. Setup Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Model

```bash
python src/train_model.py
```

### 5. Launch Dashboard

```bash
streamlit run dashboard/streamlit_app.py
```

## 📊 Use Cases

* 🌞 Solar farm monitoring
* ⚙️ Predictive maintenance
* 📉 Performance degradation detection
* ⚡ Energy optimization

## 📈 What Makes This Project Stand Out

* Real-world **energy + ML application**
* Focus on **imbalanced classification (industry problem)**
* Practical **threshold + ML hybrid approach**
* Designed with **deployment & monitoring in mind**

---

## 🤝 Contributions

Contributions are welcome! Feel free to fork and improve the project.
