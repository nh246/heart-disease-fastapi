import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# 1. Download (Kaggle CSV) – put the file in the repo root as heart.csv
df = pd.read_csv("heart.csv")

# 2. Features / target
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Train a simple Random Forest
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# 4. Save
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/heart_model.joblib")
print(f"Model saved – accuracy on test: {model.score(X_test, y_test):.3f}")