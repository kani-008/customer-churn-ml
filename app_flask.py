from flask import Flask, request, jsonify
from predict import predict_single

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction, probability = predict_single(data)
    return jsonify({
        "prediction": prediction,
        "probability": probability
    })

if __name__ == '__main__':
    app.run(debug=True)
