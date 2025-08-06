from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a list of spammy keywords
SPAM_KEYWORDS = [
    "win", "won", "selected", "gift card", "click here", "claim now", "free", "$1000"
]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data.get("message", "").lower()

    # Basic keyword-based spam detection
    if any(keyword in message for keyword in SPAM_KEYWORDS):
        prediction = "spam"
    else:
        prediction = "not spam"

    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
