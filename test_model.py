import joblib

# Load the trained model
model = joblib.load("house_model.pkl")

# Test prediction: area = 1500 sq ft, 3 bedrooms, 2 bathrooms
features = [[1500, 3, 2]]
predicted_price = model.predict(features)[0]

print(f"✅ Predicted Price: ₹{predicted_price:,.2f}")