import joblib

def load_model():
    return joblib.load("models/production/model.pkl")