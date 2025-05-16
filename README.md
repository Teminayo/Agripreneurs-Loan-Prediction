# 🚀 Access to Affordable Finance for Young Agripreneurs in Nigeria

## 🔍 Problem Statement

Access to affordable finance remains a significant barrier for young Nigerians (aged 18–25) aspiring to enter the agricultural sector. Despite agriculture employing **35%** of Nigeria’s workforce, only **6%** of young individuals in this age group can access business loans. This issue is particularly pronounced in rural areas, where just **27%** of adults have access to formal financial services ([EFInA, 2020](https://www.efina.org.ng)).

### Key Challenges:
- 🌦️ Climate-related risks  
- 📉 Lack of credit history  
- 🏞️ Land tenure uncertainties  

These challenges lead traditional financial institutions to perceive young farmers as high-risk borrowers. As a result, they struggle to access the capital needed for investments in improved seeds, irrigation, and machinery—limiting both yield and income potential.

---

## 🎯 Goal

Develop a **data-driven**, **predictive**, and **decision-support** solution to:

1. ✅ Assess and improve creditworthiness of young farmers using alternative data (e.g., assets, income, education level).  
2. 🤖 Predict loan repayment probability or business success using machine learning or statistical models.  
3. 📊 Build a trustable scoring/profiling system for financial institutions, investors, and grant providers to support young agripreneurs.

---

## 📂 Data Sources

- [EFInA Access to Financial Services in Nigeria 2023](https://www.efina.org.ng)  
- [World Bank Global Findex Microdata](https://globalfindex.worldbank.org)

---

## 📊 Exploratory Data Analysis (EDA)

- Datasets were obtained in **SPSS format** with encoded responses.  
- Variables were recoded using available questionnaires (e.g., `1 = Male`, `2 = Female`).  
- Data cleaning and preprocessing steps:
  - Handling missing values  
  - Creating new features like `Total_Income` and `Income_to_Loan_Ratio`  
  - Dropping irrelevant columns  
  - Formatting and filtering for consistency  

> ⚠️ Some missing values were retained due to extensive data entry gaps, which may affect model reliability.

---

## 📈 Agripreneur Finance Dashboard

An interactive Power BI dashboard was developed to:

- Provide insights into financial accessibility for young agripreneurs  
- Support decision-making for policymakers and financial institutions  

🔗 **[View Dashboard (Power BI)](https://app.powerbi.com/view?r=eyJrIjoiYjkxOTUxNjctNTY1Mi00MzhkLTg4MzItMzlmY2NiZjNiYTU5IiwidCI6ImI4NDk0ZTk4LTI5NmQtNGJjMC1hMjIyLWY0YjM1ZTc1NjNjYyJ9)**  
*(Replace the link above with your actual dashboard URL)*

---

## 💡 Key Insights & Implications

1. 🧭 Southern states (e.g., Akwa Ibom, Abia) show higher asset ownership.  
2. 👩‍🌾 Female applicants slightly outperform males in asset scores — opportunity for women-focused finance programs.  
3. 🎓 Education strongly correlates with better access to finance.  
4. 🏠 Many respondents own homes, which may overextend financial capacity.  
5. 🌍 Northern states like Borno and Bauchi show lower asset scores — need for targeted interventions.

---
---

## 📌 Project Objective

 
**Building a Predictive Financial Risk Assessment Tool for Young Agripreneurs**

**🎯 Main Goal:**  
Develop a data-driven solution that enables **banks**, **investors**, and **microfinance institutions** to assess the creditworthiness of young farmers and predict their ability to **repay agricultural loans** or **run successful agribusinesses**.

### ✅ Key Deliverables:
- Identify key **creditworthiness factors**  
- Predict **loan repayment behavior**  
- Build **trustworthy tools** (models/visualizations) for financiers  
- **Bonus:** Prototype dashboard/app + farmer financial education tips  

---


## 🧹 Data Cleaning

### 🗂️ Dataset Description  
Columns include:
- **Personal Details:** `Gender`, `Married`, `Dependents`, `Education`, `Self_Employed`  
- **Financial Information:** `ApplicantIncome`, `CoapplicantIncome`, `LoanAmount`, `Loan_Amount_Term`, `Credit_History`  
- **Target Variable:** `Loan_Status (Y/N)`

### 🔧 Cleaning Steps (Python)
```python
# Filling missing values
df['Credit_History'] = df['Credit_History'].fillna(0)
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0])
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Married'] = df['Married'].fillna(df['Married'].mode()[0])
df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode()[0])
df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])

## 🤖 Model Prediction

- **Algorithm Used:** Random Forest Classifier  
- **Target Variable:** Loan Approval Status (based on creditworthiness)  

### Features:
- Gender  
- Marital Status
- Dependents  
- Education  
- Employment Status  
- Applicant Income  
- Coapplicant Income  
- Loan Amount  
- Loan Term  
- Credit History  
- Property Area  

---

## 📋 Model Evaluation

- **Accuracy:** `0.84`  
- **Classification Report:**

          precision    recall  f1-score   support
       0       0.00      0.00      0.00       187
       1       0.84      1.00      0.91       993
```





## 👥 Team Members

We are a team of three who collaborated on this project:

- [Ibinayo Blessing Temilade](https://www.linkedin.com/in/blessing-temilade/)
- [Mercy Erioluwa Adewusi](https://www.linkedin.com/in/mercy-erioluwa-adewusi-b22b9a281?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
- [Stephen Olusegun](https://www.linkedin.com/in/stephen0lusegun?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)


























