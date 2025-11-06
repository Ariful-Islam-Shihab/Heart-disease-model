from fastapi import FastAPI
from schema import heartInput,heartOutput
import joblib
import numpy as np


app = FastAPI()


# Load the model once at startup
model = joblib.load("heart_disease_model.pkl")

# Heart disease class names for readability
class_names = ['No Disease', 'Disease']


@app.get("/info")
def model_info():
    """Basic model info"""
    return {
        "model_type": "RandomForestClassifier",
        "classes": class_names
    }

@app.post("/predict", response_model=heartOutput)
def predict_species(data: heartInput):
    """Make prediction from input features"""
    features = np.array([[data.age, data.sex, data.cp, data.trestbps, data.chol, data.fbs, data.thalach, data.oldpeak]])
    prediction = model.predict(features)[0]
    predicted_class = class_names[prediction]
    return {"prediction": predicted_class}


@app.get("/health")
def health_check():
    """
    Example API:
    - Simple health check endpoint.
    - Load balancers like Nginx, AWS ELB, or Kubernetes call this to check
      if the instance is alive and healthy.
    ⚙️ Use when: You deploy multiple instances and need auto-failover.
    """
    return {"status": "healthy"}
