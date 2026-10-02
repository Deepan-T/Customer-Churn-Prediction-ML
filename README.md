# Customer Churn Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a customer is likely to **Churn** or **Not Churn** using Machine Learning classification algorithms.

The project uses customer demographic, usage, satisfaction, payment, contract, and service-related information to classify customers.

Multiple classification models are implemented and integrated into a **Flask web application**. The application uses the predictions from the models to generate a final churn prediction using a majority-voting approach.

---

## 🎯 Objective

The main objectives of this project are:

* Predict customer churn using Machine Learning.
* Implement multiple classification algorithms.
* Apply feature scaling where required.
* Save trained models using Pickle.
* Build a Flask-based prediction application.
* Combine predictions from multiple models using majority voting.

---

## 📊 Dataset Features

The project uses the following customer-related features:

* Age
* Tenure Months
* Monthly Usage Hours
* Support Tickets
* Satisfaction Score
* Monthly Charges
* Data Usage GB
* Payment Delay Days
* Contract Months
* Average Login Days
* Service Count
* Discount Percent

### Target

**Customer Churn**

The target contains two possible outcomes:

```text
Churn
Not Churn
```

---

## 🤖 Machine Learning Algorithms

The project uses four classification algorithms:

### 1. Support Vector Machine (SVM)

SVM is used to classify customers into different classes by finding a suitable decision boundary between them.

### 2. Random Forest Classifier

Random Forest combines multiple decision trees to perform classification.

### 3. Decision Tree Classifier

Decision Tree uses a tree-like structure to make classification decisions based on feature values.

### 4. Logistic Regression

Logistic Regression is a classification algorithm used to predict the probability of a customer belonging to a particular class.

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Preprocessing
   ↓
Feature Preparation
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Model Training
   ↓
SVM
Random Forest
Decision Tree
Logistic Regression
   ↓
Save Models using Pickle
   ↓
Flask Web Application
   ↓
User Input
   ↓
Model Predictions
   ↓
Majority Voting
   ↓
Final Churn / Not Churn
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* Pickle
* Jupyter Notebook
* HTML

---

## 📁 Project Structure

```text
Customer-Churn-Prediction/
│
├── Customer_ML_classification.ipynb
├── Customer_ML_Practice_20000.csv
│
├── app.py
│
├── model1.pkl
├── model2.pkl
├── model3.pkl
├── model4.pkl
├── scaler.pkl
│
├── templates/
│   └── index.html
│
├── .gitignore
└── README.md
```

---

## 💾 Saved Models

The Flask application loads four trained classification models:

| Model File   | Algorithm              |
| ------------ | ---------------------- |
| `model1.pkl` | Support Vector Machine |
| `model2.pkl` | Random Forest          |
| `model3.pkl` | Decision Tree          |
| `model4.pkl` | Logistic Regression    |

The application also loads:

```text
scaler.pkl
```

which is used to transform the input data for models that require scaled features.

---

## 🗳️ Majority Voting

The application generates predictions from all four models.

The final result is determined using a simple majority-voting approach.

```text
Model 1 → Churn / Not Churn
Model 2 → Churn / Not Churn
Model 3 → Churn / Not Churn
Model 4 → Churn / Not Churn
             ↓
       Majority Voting
             ↓
     Final Prediction
```

If at least two models predict **Churn**, the final result is:

```text
Churn
```

Otherwise:

```text
Not Churn
```

---

## 🌐 Flask Web Application

The trained models are deployed through a Flask web application.

The user enters customer information through the web interface.

The application:

1. Receives customer information.
2. Creates the required input DataFrame.
3. Scales the input using the saved scaler where required.
4. Generates predictions from the four models.
5. Converts predictions into Churn/Not Churn.
6. Applies majority voting.
7. Displays the final prediction.

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/customer-churn-prediction-ml.git
```

### Step 2: Open the Project

```bash
cd customer-churn-prediction-ml
```

### Step 3: Install Required Libraries

```bash
pip install pandas numpy scikit-learn flask
```

### Step 4: Run Flask

```bash
python app.py
```

### Step 5: Open the Application

Open the local Flask URL shown in the terminal, commonly:

```text
http://127.0.0.1:5000/
```

---

## 🔮 Future Improvements

* Add detailed model performance comparison.
* Add accuracy, precision, recall and F1-score visualization.
* Add confusion matrix visualization.
* Improve the user interface.
* Add customer churn probability.
* Deploy the application online.
* Add database integration.
* Add interactive analytics dashboard.

---

## 👨‍💻 Author

**Deepan Thangaraj**

Data Analytics | Machine Learning | Python | SQL | Power BI
