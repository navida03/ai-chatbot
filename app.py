from flask import Flask, request, jsonify, render_template
import json
import random
import pickle
import os

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

with open("intents.json", "r") as file:
    data = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip().lower()

    if not user_message:
        return jsonify({"response": "Please enter a message."}), 400

    X = vectorizer.transform([user_message])

    predicted_tag = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]
    confidence = max(probabilities)

    if confidence < 0.50:
        return jsonify({
            "response": "I’m not fully sure I understood that. Could you rephrase?",
            "confidence": round(float(confidence), 2)
        })

    for intent in data["intents"]:
        if intent["tag"] == predicted_tag:
            return jsonify({
                "response": random.choice(intent["responses"]),
                "intent": predicted_tag,
                "confidence": round(float(confidence), 2)
            })

    return jsonify({"response": "Sorry, I didn’t understand."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)