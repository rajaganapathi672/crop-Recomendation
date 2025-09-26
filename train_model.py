import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample dataset (you should replace this with your actual dataset)
data = {
    'N': [90, 85, 60, 74, 78, 69, 82, 84, 64, 80],
    'P': [42, 58, 55, 35, 40, 45, 52, 39, 42, 48],
    'K': [43, 41, 44, 42, 45, 47, 48, 46, 43, 44],
    'temperature': [20.8, 21.7, 23.0, 26.5, 24.3, 26.7, 27.2, 22.7, 21.5, 25.8],
    'humidity': [82.0, 80.7, 82.3, 79.8, 81.4, 79.2, 75.2, 76.9, 80.8, 78.2],
    'ph': [6.7, 7.0, 7.2, 6.3, 6.9, 6.5, 6.1, 6.8, 7.1, 6.4],
    'rainfall': [202.9, 210.5, 215.3, 192.7, 200.7, 195.6, 187.9, 206.7, 209.8, 197.5],
    'label': ['rice', 'rice', 'maize', 'maize', 'blackgram', 'blackgram', 'mango', 'mango', 'lentil', 'lentil']
}

df = pd.DataFrame(data)

# Split data into features and target
X = df.drop('label', axis=1)
y = df['label']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
print(f"Model Accuracy: {model.score(X_test, y_test):.2f}")

# Save the model
with open('models/crop_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as crop_model.pkl")