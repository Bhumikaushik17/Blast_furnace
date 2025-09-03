# Blast_furnace
Blast Furnace Throughput Optimization using ML
# 🚀 Blast Furnace Throughput Optimization & Fuel Reduction using Machine Learning  

This project focuses on **increasing blast furnace throughput** and **reducing fuel consumption** using **Machine Learning (ML)** and **Data Analysis**.  
The solution integrates **data cleaning, exploratory analysis, ML model training, scenario simulation, and an interactive Streamlit app** for real-time decision-making.

---

## 📌 Project Motivation  

Blast Furnaces are critical for iron production, where optimizing **throughput** (production rate) and minimizing **fuel consumption** directly impacts efficiency and cost.  
However, several operational parameters influence these outcomes, making manual tuning difficult.  

**This project answers the questions:**  
- **What** factors influence throughput and fuel consumption?  
- **How** can we predict future performance based on current parameters?  
- **What changes** in parameters will increase throughput while reducing fuel usage?  

---

## 🎯 Project Objectives  

1. **Data Analysis (EDA)**: Understand parameter relationships using heatmaps, correlations, and distributions.  
2. **Model Building**: Predict throughput and fuel rate using ML models:  
   - Linear Regression (baseline model)  
   - Random Forest Regressor (robust model)  
3. **Feature Importance**: Use **SHAP Analysis** for explainability – see how parameters influence results.  
4. **Scenario Simulation**: Suggest parameter changes for optimization.  
5. **Deployment**: Create a **Streamlit-based GUI** for real-time predictions & recommendations.  

---

## 🧠 Methodology  

### 1️⃣ Data Preprocessing  
- Handle missing values  
- Convert string % values to numeric  
- Normalize data for better model accuracy  

### 2️⃣ Exploratory Data Analysis (EDA)  
- Heatmaps for correlation  
- Distribution plots for variables  
- Identification of key features  

### 3️⃣ Machine Learning Models  
- **Linear Regression** → Simple baseline model  
- **Random Forest** → Captures non-linear relationships, better accuracy  
- **SHAP Analysis** → Explainable AI for decision transparency  

### 4️⃣ Scenario Simulation  
- Top 3 parameters identified using feature importance  
- Test different % changes → Find best throughput & lowest fuel rate  

### 5️⃣ Deployment using Streamlit  
- Real-time input for parameters  
- Get predictions + recommendations instantly  

---

## 📂 Project Structure  

blast_furnace/
│
├── data/
│ └── Raigarh BF Data From 1st Jan 2025.xlsx # Input Dataset
│
├── models/
│ ├── rf_prod_model.joblib # Throughput Model
│ ├── rf_fuel_model.joblib # Fuel Model
│ ├── scaler_prod.joblib # Scaler for Throughput
│ └── scaler_fuel.joblib # Scaler for Fuel Rate
│
├── app/
│ └── app.py # Streamlit App for GUI
│
├── notebooks/
│ └── training_script.ipynb # Data Analysis & ML Training
│
├── reports/
│ ├── EDA_Report.pdf # Data Analysis Report
│ └── Project_Presentation.pptx # Project PPT
│
├── requirements.txt # Dependencies
└── README.md # Project Documentation

---

## ⚙️ Tech Stack  

- **Python** → Main Programming Language  
- **Pandas, NumPy** → Data Handling  
- **Matplotlib, Seaborn** → Data Visualization  
- **Scikit-learn** → Machine Learning Models  
- **SHAP** → Explainable AI  
- **Streamlit** → Web App for Deployment  

---
🚀 How to Run
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit App
streamlit run app/app.py

3️⃣ Use the Interface

Enter parameter values

Get Throughput and Fuel Rate predictions

View recommendations for optimization

📊 Key Outputs

Correlation Heatmap → Shows relationships between variables

Feature Importance Plots → Parameters affecting throughput & fuel rate

SHAP Summary Plots → Explainable AI insights

Scenario Tables → Recommendations for parameter tuning

Streamlit App → Interactive prediction tool

🏆 Results

Identified Top 3 Parameters influencing throughput & fuel rate

Simulated scenarios → Achieved higher throughput with lower fuel consumption

Built a user-friendly Web App for real-time decision support

🔮 Future Enhancements

Integrate real-time sensor data from blast furnace

Add Reinforcement Learning for auto-parameter tuning

Deploy on cloud platforms for remote access

## 📈 Workflow Diagram  

```text
Data Collection → Data Preprocessing → EDA → Model Training → SHAP Analysis
        ↓                  ↓                  ↓          ↓
    Scenario Simulation → Streamlit Deployment → Recommendations
