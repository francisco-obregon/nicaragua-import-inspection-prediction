# Nicaragua Import Tax & Inspection Prediction

## 📌 Objective

Build a machine learning model to predict which import shipments should be inspected, using historical customs data from Nicaragua.

---

## 📊 Dataset

* Source: Import customs data (CSV)
* Records: 37,191
* Features include:

  * CIF
  * FOB
  * AJUSTE
  * CODIGO_ADUANA
  * YEAR
  * INSPECCION (target)

---

## ⚠️ Target Definition

The target variable was encoded using LabelEncoder:

* **0 → INSPECCION**
* **1 → NO INSPECCION**

This mapping is important for correctly interpreting model performance.

---

## ⚙️ Project Structure

```
nicaragua-import-tax-prediction/
│
├── data/
├── src/
├── sql/
├── visuals/
├── models/
├── reports/
├── eda/
├── feature_engineering/
├── README.md
```

---

## 🔍 Exploratory Data Analysis (EDA)

Key findings:

* Only ~13% of shipments are inspected (class imbalance)
* Most inspections occur in customs office 610
* Average taxes decreased in 2017

---

## 📈 Visualizations

* Inspection percentage distribution
* Inspections by customs office

---

## 🧠 Feature Engineering

* Created ratio: `FOB_CIF_RATIO`
* Cleaned and standardized data
* Selected key numerical features

---

## 🤖 Model

* Algorithm: Random Forest Classifier
* Task: Binary Classification (INSPECCION vs NO INSPECCION)
* Class imbalance handled using:

  * `class_weight="balanced"`

---

## 📊 Model Performance

Evaluation performed on a **20% test set (~7,400 records)**.

### Classification Report (Final Model)

* **Accuracy:** ~90%
* **Recall (INSPECCION):** ~78% ✅ (priority metric)
* **Precision (INSPECCION):** ~59%

### Confusion Matrix

```
[[ 776  222]
 [ 550 5891]]
```

### Interpretation

* The model correctly identifies most inspection cases
* Some false positives are generated, but this is acceptable in a risk-based scenario
* Improving recall was prioritized over overall accuracy

---

## ⚖️ Model Comparison

Multiple models were tested:

* Random Forest ✅ (selected)
* Gradient Boosting ❌ (lower recall for inspections)
* Logistic Regression ❌ (high false positives, low accuracy)

The final model was selected based on **recall for inspection cases**, which is the most critical metric for the business.

---

## 🗄️ SQL Analysis

Used SQLite to analyze data:

* Inspection distribution
* Average taxes by year
* Top customs offices

---

## 🚀 Pipeline

1. Load data
2. Preprocess
3. Feature engineering
4. Train model
5. Evaluate on test set
6. Predict new data
7. Export results to Excel

---

## 📦 Technologies Used

* Python
* Pandas
* Scikit-learn
* SQLite
* Matplotlib

---

## 💡 Business Impact

This model helps customs authorities:

* Prioritize high-risk shipments
* Reduce missed inspections
* Optimize operational resources

The model is intentionally tuned to **capture more inspection cases**, even at the cost of some false positives.

---

## 👤 Author

Francisco Obregón
