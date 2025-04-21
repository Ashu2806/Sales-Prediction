# 🚗 Car Sales Price Prediction using Machine Learning

This project predicts the **Amount Paid for a Car** based on customer attributes such as age, salary, credit card debt, and net worth using a machine learning model.

---

## 📊 Problem Statement

**Objective**: Forecast the car purchase amount using historical customer data to support strategic sales and marketing decisions.

---

## 🧠 Techniques Used

- Data Cleaning & Preprocessing  
- Feature Scaling (StandardScaler)  
- Random Forest Regression  
- Model Evaluation (MAE, MSE, R² Score)  
- Visualization (Matplotlib)

---

## 📁 Dataset

- **Filename**: `car_purchasing.csv`  
- **Source**: Provided locally (originally from Kaggle)  
- **Encoding**: `ISO-8859-1` (to avoid UnicodeDecodeError)

### Sample Features:

| Age | Annual Salary | Credit Card Debt | Net Worth | Amount Paid |
|-----|----------------|------------------|------------|--------------|
| 45  | 48700          | 10000            | 200000     | 42000        |

---

## 🚀 How to Run

1. Clone this repository  
2. Make sure `car_purchasing.csv` is in the project folder  
3. Run the Python script:

```bash
python main.py
