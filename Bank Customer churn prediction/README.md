# Customer Churn Prediction
### Bank Customer Churn Analysis & Retention Strategy

---

## 📌 Project Overview

This project predicts customer churn for a bank using 
machine learning classification models. The goal was not 
only to build an accurate predictive model but to translate 
the findings into actionable business recommendations that 
a retention team could immediately implement.

---

## 🎯 Business Problem

Banks lose significant revenue when customers close accounts 
or stop using services. Identifying at-risk customers before 
they churn allows the business to intervene proactively — 
reducing customer acquisition costs and protecting revenue.

**Key question:** Which customers are most likely to churn 
and what should the business do about it?

---

## 🔧 Tools & Libraries

- Python (Pandas, NumPy)
- Scikit-learn (Logistic Regression, Random Forest)
- Imbalanced-learn (SMOTE)
- Matplotlib

---

## 📊 Methodology

### 1. Data Preprocessing
- Encoded categorical variables (Gender mapped to 0/1)
- Created Age Buckets (Young, Middle-aged, Senior) 
using pd.cut and one-hot encoding
- Created Balance Buckets (Very Low, Low, Medium, High) 
for better pattern visibility

### 2. Feature Engineering
Two derived features were created to capture behavioural 
patterns not visible in raw data:
- **balance_to_salary_ratio** — measures how much of a 
customer's earning potential is held in the bank
- **products_per_tenure** — measures product adoption 
relative to relationship length

### 3. Handling Class Imbalance
The dataset had significantly more non-churners than 
churners. SMOTE (Synthetic Minority Oversampling Technique) 
was applied to the training set to ensure the model learns 
from both classes equally.

### 4. Model Training & Comparison
Two models were trained and compared:

| Model | Accuracy |
|-------|----------|
| Logistic Regression (threshold tuned) | 74% |
| Random Forest | 81% |

**Selected Model: Random Forest** — achieves higher accuracy 
and captures non-linear feature relationships that Logistic 
Regression cannot model effectively.

> **Note:** An earlier model using only country as a feature 
produced a misleadingly high accuracy. This was identified 
as overfitting to a single biased feature. The full feature 
set with engineering produces more honest and generalizable 
results.

### 5. Threshold Tuning
Logistic Regression was tested at thresholds 0.3, 0.4 and 
0.5 to find the optimal precision-recall balance for a 
business context where catching churners matters more than 
overall accuracy.

### 6. Custom Churn Risk Scoring
A rule-based churn risk scoring function was developed to 
produce interpretable risk categories for business 
stakeholders:

| Risk Level | Score |
|------------|-------|
| Low Risk | 0 – 3 |
| Medium Risk | 4 – 7 |
| High Risk | 8+ |

---

## 🔍 Key Churn Drivers

Based on Random Forest feature importance analysis:

1. **Active Membership Status** — Inactive members are 
significantly more likely to churn
2. **Balance-to-Salary Ratio** — Low balance relative to 
salary indicates underutilization of banking products
3. **Products per Tenure** — Fewer products relative to 
tenure indicates weak relationship depth

---

## 💡 Business Recommendations

- **Retention Priority** — Flag High Risk customers 
(score > 7) for immediate relationship manager outreach
- **Re-engagement Campaign** — Target inactive members 
with personalized product offers before churn occurs
- **Product Cross-selling** — Proactively offer products 
to customers with only 1 product and long tenure
- **Early Warning System** — Deploy risk scoring function 
as a monthly automated report

---

## ⚠️ Limitations & Next Steps

- Model performance could be further improved with 
hyperparameter tuning using GridSearchCV
- Additional features such as customer service interactions 
and transaction frequency would likely improve accuracy
- A/B testing the retention recommendations would validate 
real-world impact

---

## 📁 Files

| File | Description |
|------|-------------|
| [`predictiion.ipynb`](https://github.com/phatudi230/Data-Analysis-Portfolio/blob/main/Bank%20Customer%20churn%20prediction/Notebook/predictiion.ipynb) | Full analysis notebook |


---

## 📬 Contact

- **LinkedIn:** [Phatudi Daniel Modiba](http://www.linkedin.com/in/phatudi-daniel-modiba)
- **Portfolio:** [Your portfolio website link]
