from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)


# ==============================
# LOAD MODELS
# ==============================

model1 = pickle.load(open("model1.pkl", "rb"))   # SVM
model2 = pickle.load(open("model2.pkl", "rb"))   # Random Forest
model3 = pickle.load(open("model3.pkl", "rb"))   # Decision Tree
model4 = pickle.load(open("model4.pkl", "rb"))   # Logistic Regression

sc = pickle.load(open("scaler.pkl", "rb"))


# ==============================
# HOME PAGE
# ==============================

@app.route("/")
def home():
    return render_template("index.html")


# ==============================
# PREDICTION
# ==============================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ------------------------------
        # GET USER INPUT
        # ------------------------------

        Age = float(request.form["Age"])
        Tenure_Months = float(request.form["Tenure_Months"])
        Monthly_Usage_Hours = float(request.form["Monthly_Usage_Hours"])
        Support_Tickets = float(request.form["Support_Tickets"])
        Satisfaction_Score = float(request.form["Satisfaction_Score"])
        Monthly_Charges = float(request.form["Monthly_Charges"])
        Data_Usage_GB = float(request.form["Data_Usage_GB"])
        Payment_Delay_Days = float(request.form["Payment_Delay_Days"])
        Contract_Months = float(request.form["Contract_Months"])
        Avg_Login_Days = float(request.form["Avg_Login_Days"])
        Service_Count = float(request.form["Service_Count"])
        Discount_Percent = float(request.form["Discount_Percent"])


        # ------------------------------
        # CREATE INPUT DATAFRAME
        # ------------------------------

        columns = [
            "Age",
            "Tenure_Months",
            "Monthly_Usage_Hours",
            "Support_Tickets",
            "Satisfaction_Score",
            "Monthly_Charges",
            "Data_Usage_GB",
            "Payment_Delay_Days",
            "Contract_Months",
            "Avg_Login_Days",
            "Service_Count",
            "Discount_Percent"
        ]


        user_input = pd.DataFrame([[
            Age,
            Tenure_Months,
            Monthly_Usage_Hours,
            Support_Tickets,
            Satisfaction_Score,
            Monthly_Charges,
            Data_Usage_GB,
            Payment_Delay_Days,
            Contract_Months,
            Avg_Login_Days,
            Service_Count,
            Discount_Percent
        ]], columns=columns)


        # ------------------------------
        # SCALE INPUT
        # ------------------------------

        user_input_scaled = sc.transform(user_input)


        # ------------------------------
        # PREDICTION
        # ------------------------------

        result1 = model1.predict(user_input_scaled)[0]   # SVM

        result2 = model2.predict(user_input)[0]          # Random Forest

        result3 = model3.predict(user_input)[0]          # Decision Tree

        result4 = model4.predict(user_input_scaled)[0]   # Logistic Regression


        # ------------------------------
        # CONVERT 0 / 1
        # ------------------------------

        svm_result = "Churn" if result1 == 1 else "Not Churn"

        rf_result = "Churn" if result2 == 1 else "Not Churn"

        dt_result = "Churn" if result3 == 1 else "Not Churn"

        lr_result = "Churn" if result4 == 1 else "Not Churn"


        # ------------------------------
        # FINAL RESULT
        # ------------------------------

        results = [
            result1,
            result2,
            result3,
            result4
        ]

        churn_count = sum(int(x) for x in results)

        if churn_count >= 2:
            final_result = "Churn"
        else:
            final_result = "Not Churn"


        # ------------------------------
        # SEND RESULT TO HTML
        # ------------------------------

        return render_template(
            "index.html",

            final_result=final_result,

            result1=svm_result,
            result2=rf_result,
            result3=dt_result,
            result4=lr_result
        )


    except Exception as e:

        return f"""
        <h1>Prediction Error</h1>
        <p>{str(e)}</p>
        <br>
        <a href="/">Go Back</a>
        """


# ==============================
# RUN FLASK
# ==============================

if __name__ == "__main__":
    app.run(debug=True)