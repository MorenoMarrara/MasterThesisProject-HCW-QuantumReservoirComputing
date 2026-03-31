import numpy as np

def evaluate_model(model, data: np.ndarray) -> float:
    model.fit(data[:-1])
    return model.predict(data[:-1], 1)