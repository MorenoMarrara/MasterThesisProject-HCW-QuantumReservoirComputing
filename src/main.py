import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

from quantum_computing_frameworks.my_qiskit import get_qrc_features
from data.loading.geosphere import Geosphere
from src.models.evaluation import evaluate_model
from src.quantum_computing_frameworks.my_qreservoir import build_base_RCModel

data = Geosphere().load_data_into_memory()
# print(data.shape)
smaller_data = data[:][-100:-1]
colnames_no_na = [x for x in smaller_data.columns if not smaller_data[x].isna().any()]
# print(colnames_no_na)
smaller_data_nona = smaller_data[colnames_no_na]
smaller_data_nona_ready = (smaller_data[colnames_no_na]
                           .drop("timestamps", axis=1)
                           .drop("stationId", axis=1)
                           .drop("ffam_flag", axis=1)
                           .drop("tlmax", axis=1)
                           .drop("tlmin", axis=1))

# X_raw, y_train = smaller_data_nona_ready.drop("tl", axis=1), smaller_data_nona_ready["tl"]
X_raw, y_train = pd.DataFrame(smaller_data_nona_ready["tl"]), smaller_data_nona_ready["tl"]

print(X_raw)
print(y_train)

# Features durch das Quanten-Reservoir generieren
# TODO: research how many qubits are needed for an optimal representation
QR_output = np.array([get_qrc_features(X_raw.iloc[line], len(X_raw.iloc[line])) for line in range(0,len(X_raw))])

# Klassische Lineare Regression auf den Quanten-Features
model = LinearRegression()
model.fit(QR_output, y_train)

print("Quanten-Features Shape:", QR_output.shape)
print(QR_output[:1])
print("Vorhersage für neue Daten:", model.predict(QR_output[:-1]))


print("---------------------")
model = build_base_RCModel(8, QR_output.shape[1])
print(evaluate_model(model, QR_output[:-1]))
