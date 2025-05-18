import gradio as gr
from predict import predict_single

def predict_interface(**kwargs):
    prediction, probability = predict_single(kwargs)
    return f"Prediction: {prediction}, Probability: {probability}"

demo = gr.Interface(
    fn=predict_interface,
    inputs=[gr.Textbox(label=key) for key in [
        "gender", "SeniorCitizen", "Partner", "Dependents", "tenure",
        "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity",
        "Contract", "MonthlyCharges", "TotalCharges", "PaymentMethod"
    ]],
    outputs="text",
    title="Customer Churn Prediction",
)

if __name__ == "__main__":
    demo.launch()
