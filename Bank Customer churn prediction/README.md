# Bank Customer Churn Prediction (Machine Learning)

## 📌 Executive Summary
This project utilizes **Logistic Regression** to predict the probability of customer attrition for a retail bank. By identifying high-risk churn clusters, this analysis provides data-driven strategies to improve customer retention and maximize lifetime value.

---

## 📊 Dataset
* **Source:** Bank Customer Churn Dataset (10,000+ records)
* **Target Variable:** `Exited` (1 = Churned, 0 = Retained)
* **Key Features:** Credit Score, Geography, Age, Tenure, Balance, and Member Activity.

---

## 🛠️ Tools & Technologies
* **Language:** Python
* **Data Science Stack:** Pandas, NumPy, Scikit-learn
* **Visualization:** Matplotlib, Seaborn
* **Statistical Analysis:** SciPy (Hypothesis Testing)

---

## 🚀 Project Highlights

### 1. Statistical Hypothesis Testing
Conducted bivariate analysis to validate key drivers. Using **T-Tests**, I confirmed that variables such as **Age** and **Account Balance** have a statistically significant impact on churn ($p < 0.05$), moving beyond simple observation to statistical proof.

### 2. Robust Data Preprocessing
* **Encoding:** Transformed categorical variables using One-Hot Encoding while avoiding the Dummy Variable Trap.
* **Scaling:** Applied `StandardScaler` to normalize numerical features, ensuring the Logistic Regression coefficients were not biased by different units of measurement.

### 3. Business Insights & Drivers
* **Activity Gap:** Discovered that "Inactive Members" are twice as likely to churn, suggesting a need for automated re-engagement triggers.
* **Product Density:** Identified that customers with only a single bank product have a significantly higher churn rate compared to multi-product holders.

### 4. Model Performance
* Evaluated the model using a **Confusion Matrix** and **Classification Report**.
* Focused on **Recall** to minimize "False Negatives"—ensuring the bank identifies as many at-risk customers as possible.

---

## 📂 How to Run
1. Clone the repository: `git clone https://github.com/phatudi230/Bank Customer churn prediction`
2. Install dependencies: `pip install pandas scikit-learn seaborn`
3. Open `churn_analysis.ipynb` in Jupyter Notebook or VS Code.

---

**File**:
**Conclusion & Business Recommendation**
<img width="1371" height="753" alt="Screenshot 2026-01-31 205615" src="[https://github.com/user-attachments/assets/a8665db2-13f5-4eac-8b01-48c525c7b692](https://github.com/phatudi230/Data-Analysis-Portfolio/blob/main/Bank%20Customer%20churn%20prediction/Notebook/Conclusion%20&%20Business%20recommendaation.png?raw=true)" />
