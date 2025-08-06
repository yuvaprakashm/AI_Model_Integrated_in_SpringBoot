import joblib

# Load trained model
model = joblib.load("spam_classifier.joblib")

# Predict new message
message = input("Enter a message: ")
prediction = model.predict([message])
print(f"This message is: {prediction[0].upper()}")
