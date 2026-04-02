import numpy as np
import pandas as pd


def evaluate_model(model, data: np.ndarray) -> float:
    model.fit(data)
    return model.predict(data, 1)