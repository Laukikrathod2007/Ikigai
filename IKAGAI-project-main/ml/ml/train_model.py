import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
data = pd.read_csv("../../data/data/mental_health_data.csv")


# Encode target labels
label_encoder = LabelEncoder()
data["stress"] = label_encoder.fit_transform(data["stress"])

# Features and target
X = data[["sleep", "study", "screen", "activity", "mood"]]
y = data["stress"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

# Save model and encoder
with open("stress_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)

print("✅ Model training completed and files saved.")
