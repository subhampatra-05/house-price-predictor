from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load("house_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        area = float(data["area"])
        bedrooms = int(data["bedrooms"])
        bathrooms = int(data["bathrooms"])

        if area < 300 or bedrooms <= 0 or bathrooms <= 0:
            return jsonify({"error": "Invalid input values."})

        features = [[area, bedrooms, bathrooms]]
        prediction = model.predict(features)[0]
        return jsonify({"predicted_price": f"✅ Estimated Price: ₹{prediction:,.2f}"})
    
    except Exception as e:
        return jsonify({"error": str(e)})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)