from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

class PredictionRequest(BaseModel):
    time_feature: int
    trt: int
    age: int
    wtkg: float
    hemo: int
    homo: int
    drugs: int
    karnof: int
    oprior: int
    z30: int
    zprior: int
    preanti: int
    race: int
    gender: int
    str2: int
    strat: int
    symptom: int
    treat: int
    offtrt: int
    cd40: int
    cd420: int
    cd80: int
    cd820: int



@app.post("/predict")
def predict(request: PredictionRequest):
    features = np.array(request.features).reshape(1, -1)
    #prediction = model.predict(features).tolist()
    return {"prediction": features}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
