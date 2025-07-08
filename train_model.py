# train_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Step 1: Create a small sample dataset
data = {
    'area': [1000, 1500, 2000, 2500, 3000],
    'bedrooms': [2, 3, 3, 4, 4],
    'bathrooms': [1, 2, 2, 3, 3],
    'price': [150000, 200000, 250000, 300000, 350000]
}

df = pd.DataFrame(data)

# Step 2: Define features and label
X = df[['area', 'bedrooms', 'bathrooms']]  # input
y = df['price']                            # output

# Step 3: Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Step 4: Save the model to a .pkl file
joblib.dump(model, 'house_model.pkl')

print("✅ Model trained and saved as house_model.pkl")