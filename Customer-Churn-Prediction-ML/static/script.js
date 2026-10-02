const form = document.getElementById("predictionForm");

const predictButton =
    document.getElementById("predictButton");

const loading =
    document.getElementById("loading");

const resultSection =
    document.getElementById("resultSection");

const finalResult =
    document.getElementById("finalResult");


form.addEventListener("submit", async function(event) {

    // Stop normal form submission
    event.preventDefault();


    // Show loading
    loading.classList.remove("hidden");

    resultSection.classList.add("hidden");

    predictButton.disabled = true;

    predictButton.textContent =
        "Predicting...";


    // Get input values

    const data = {

        Age:
            parseFloat(
                document.getElementById("Age").value
            ),

        Tenure_Months:
            parseFloat(
                document.getElementById(
                    "Tenure_Months"
                ).value
            ),

        Monthly_Usage_Hours:
            parseFloat(
                document.getElementById(
                    "Monthly_Usage_Hours"
                ).value
            ),

        Support_Tickets:
            parseFloat(
                document.getElementById(
                    "Support_Tickets"
                ).value
            ),

        Satisfaction_Score:
            parseFloat(
                document.getElementById(
                    "Satisfaction_Score"
                ).value
            ),

        Monthly_Charges:
            parseFloat(
                document.getElementById(
                    "Monthly_Charges"
                ).value
            ),

        Data_Usage_GB:
            parseFloat(
                document.getElementById(
                    "Data_Usage_GB"
                ).value
            ),

        Payment_Delay_Days:
            parseFloat(
                document.getElementById(
                    "Payment_Delay_Days"
                ).value
            ),

        Contract_Months:
            parseFloat(
                document.getElementById(
                    "Contract_Months"
                ).value
            ),

        Avg_Login_Days:
            parseFloat(
                document.getElementById(
                    "Avg_Login_Days"
                ).value
            ),

        Service_Count:
            parseFloat(
                document.getElementById(
                    "Service_Count"
                ).value
            ),

        Discount_Percent:
            parseFloat(
                document.getElementById(
                    "Discount_Percent"
                ).value
            )
    };


    try {

        // Send data to Flask

        const response = await fetch(
            "/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify(data)
            }
        );


        // Convert Flask response to JSON

        const result =
            await response.json();


        // Display final result

        finalResult.textContent =
            result.final_result;


        // Change result style

        finalResult.classList.remove(
            "churn",
            "no-churn"
        );


        if (result.final_prediction === 1) {

            finalResult.classList.add(
                "churn"
            );

        } else {

            finalResult.classList.add(
                "no-churn"
            );

        }


        // Display individual models

        document.getElementById(
            "model1Result"
        ).textContent =
            result.model1 === 1
                ? "Churn"
                : "Not Churn";


        document.getElementById(
            "model2Result"
        ).textContent =
            result.model2 === 1
                ? "Churn"
                : "Not Churn";


        document.getElementById(
            "model3Result"
        ).textContent =
            result.model3 === 1
                ? "Churn"
                : "Not Churn";


        document.getElementById(
            "model4Result"
        ).textContent =
            result.model4 === 1
                ? "Churn"
                : "Not Churn";


        // Show result

        resultSection.classList.remove(
            "hidden"
        );


        // Scroll to result

        resultSection.scrollIntoView({
            behavior: "smooth"
        });


    } catch (error) {

        console.error(error);

        alert(
            "Something went wrong. " +
            "Please check your Flask server."
        );

    }


    // Stop loading

    loading.classList.add("hidden");

    predictButton.disabled = false;

    predictButton.textContent =
        "Predict Customer Churn";

});