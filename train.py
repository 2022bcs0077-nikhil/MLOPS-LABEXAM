import json
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Author: Golla Nikhil - 2022BCS0077

def train_model():
    print("=" * 60)
    print("Training started | Golla Nikhil | 2022BCS0077")
    print("=" * 60)

    # Generate synthetic regression dataset
    X, y = make_regression(
        n_samples=1000,
        n_features=10,
        noise=10,
        random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train a simple Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    print(f"Model trained successfully.")
    print(f"MSE on test set: {mse:.4f}")
    print(f"Evaluated by: Golla Nikhil-2022BCS0077")

    # Save model
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Model saved to model.pkl")

    # Save metrics
    metrics = {
        "mse": mse,
        "author": "Golla Nikhil",
        "roll": "2022BCS0077"
    }
    with open("metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"Metrics saved to metrics.json: {metrics}")

    return mse

if __name__ == "__main__":
    train_model()
