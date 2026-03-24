# Exchange-Rate-Prediction
---

# 📊 Forex Analytics & Trading Intelligence Platform

A full-stack, real-time **Forex analytics platform** that combines data engineering, machine learning, and cloud deployment to deliver actionable trading insights through an interactive dashboard.

---

## 🌐 Live Dashboard

🔴 **Explore the Live App**

<img width="1826" height="802" alt="image" src="https://github.com/user-attachments/assets/f75861e3-584e-4837-b206-feb23d7b97e5" />

<img width="1747" height="761" alt="image" src="https://github.com/user-attachments/assets/07956114-33c2-49cc-95c8-8e744f4f242c" />


The platform provides:

* Real-time exchange rates
* AI-based forecasts
* Automated trading signals
* Strategy performance tracking
* Market trend and volatility insights

⏱ Auto-refresh: every 60 seconds
🔄 Data updates: every hour via CI/CD pipeline

---

## 🚀 Overview

This project is designed as a **complete Forex intelligence system**, simulating a real-world FinTech product.

It integrates:

* Real-time data ingestion
* Automated ETL pipelines
* Machine learning forecasting
* Signal generation logic
* Secure authentication system
* Interactive web dashboard
* Continuous deployment & automation

---

## 🧠 System Architecture

```
Forex API
   ↓
ETL Pipeline (Extract → Transform → Load)
   ↓
Processed Dataset
   ↓
Machine Learning Model
   ↓
Forecast Engine
   ↓
Trading Signal Generator
   ↓
Streamlit Dashboard
   ↓
End Users (Login / Signup / Admin)
```

---

## 🎯 Key Features

### 🔄 Automated Data Pipeline

* Fetches real-time exchange rates via API
* Cleans and structures raw data
* Stores both raw and processed datasets
* Runs automatically every hour (GitHub Actions)

---

### 🤖 Machine Learning Forecasting

* Random Forest regression model
* Time-series feature engineering
* Predicts 7-day currency trends
* Stores predictions for dashboard use

---

### 📈 Trading Signal Engine

* Generates BUY / SELL / HOLD signals
* Calculates returns and performance
* Tracks cumulative profit strategy

---

### 🌐 Interactive Dashboard

* Live currency tracking
* Multi-currency comparison
* Volatility and trend analysis
* Forecast visualization
* Strategy performance insights
* Auto-refresh enabled

---

### 🔐 Authentication System

* Secure login and signup
* Password hashing
* Admin panel for user monitoring

---

### ⚙ DevOps & Automation

* GitHub Actions pipeline (runs hourly)
* Automates ETL + ML + signal generation
* Updates datasets and pushes to repo
* Enables continuous deployment

---

## 📁 Project Structure

```
ExchangeRate_analysis/
│
├── app.py
├── signup.py
├── auth_utils.py
├── run_pipeline.py
│
├── etl/
├── ml/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── users.csv
│
├── .github/workflows/
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/ExchangeRate_analysis.git
cd ExchangeRate_analysis
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API Key

```python
API_KEY = "your_api_key_here"
```

---

## ▶ Run Pipeline

```bash
python run_pipeline.py
```

This will:

* Fetch data
* Process it
* Train model
* Generate forecasts
* Create trading signals

---

## ▶ Run Application

```bash
streamlit run app.py
```

Open: [http://localhost:8501](http://localhost:8501)

---

## 🔐 Authentication

* User signup with secure password storage
* Login-based dashboard access
* Admin panel for managing users

---

## 🔁 CI/CD Automation

GitHub Actions handles:

* Hourly data updates
* Model retraining
* Forecast generation
* Signal updates
* Automatic deployment

---

## ☁ Deployment

* Hosted on **Streamlit Cloud**
* Auto-deploys from GitHub
* Updates on every push

---

## 📌 Future Scope

* Email verification system
* Password recovery
* Google OAuth login
* Portfolio simulation
* Trading bot integration
* PostgreSQL database migration
* User behavior analytics

---

## 👨‍💻 Author

**Subham Das**
M.Tech Graduate | Data Science & Analytics
Aspiring FinTech & AI Engineer

---

## ⭐ Why This Project Stands Out

This project reflects strong skills in:

* Data Engineering
* Machine Learning
* Backend & Frontend Integration
* DevOps & Automation
* Cloud Deployment
* Secure Authentication
* Real-world FinTech systems

👉 Not just a dashboard — a **complete trading intelligence platform**

---

With:

> “Data Scientist | FinTech & ML Enthusiast”


