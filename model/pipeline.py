from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from model.custom_model import CustomModel

def create_pipeline():
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', CustomModel(n_estimators=100, random_state=42))
    ])
    return pipeline
