from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("spam_classifier.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data.get("message", "")
    prediction = model.predict([message])[0]
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(port=5000)
