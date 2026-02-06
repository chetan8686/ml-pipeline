from fastapi import FastAPI
from service.model_loader import load_model
from service.schemas import PredictRequest, PredictResponse

app = FastAPI()

model = load_model()


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/readyz")
def readyz():
    return {"status": "ready"}


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    prediction = model.predict([[req.feature1, req.feature2]])[0]
    return {"prediction": int(prediction)}