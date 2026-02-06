from sklearn.linear_model import LogisticRegression
import joblib
import os


def train_model(X, y):
    model = LogisticRegression(max_iter=500)
    model.fit(X, y)

    os.makedirs("models/candidate", exist_ok=True)

    joblib.dump(model, "models/candidate/model.pkl")

    return model