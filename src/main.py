import numpy as np
from sklearn.linear_model import LinearRegression
from pandas import read_csv

from platforms.my_qiskit import get_qrc_features
from data.loading.utils import load_data_from
from data.loading.geosphere import Geosphere


# --- BEISPIEL ANWENDUNG ---

# Beispiel-Daten (X: Zeitreihen-Fenster, y: Zielwert)
# X_raw = [[0.1, 0.2], [0.2, 0.3], [0.3, 0.4]]
# y_train = [0.5, 0.6, 0.7]

data = Geosphere().load_data_into_memory()
print(data.shape)
smaller_data = data[:][-10000:-1]
colnames_no_na = [x for x in smaller_data.columns if not smaller_data[x].isna().any()]
print(colnames_no_na)
smaller_data_nona = smaller_data[colnames_no_na]
smaller_data_nona_ready = (smaller_data[colnames_no_na]
                           .drop("timestamps", axis=1)
                           .drop("stationId", axis=1)
                           .drop("ffam_flag", axis=1)
                           .drop("tlmax", axis=1)
                           .drop("tlmin", axis=1))

X_raw, y_train = smaller_data_nona_ready.drop("tl", axis=1), smaller_data_nona_ready["tl"]
# X_raw, y_train = smaller_data_nona_ready["tl"], smaller_data_nona_ready["tl"]

# Features durch das Quanten-Reservoir generieren
# TODO: research how many qubits are needed for an optimal representation
QR_output = np.array([get_qrc_features(X_raw.iloc[line], len(X_raw.iloc[line])) for line in range(0,len(X_raw))])

# Klassische Lineare Regression auf den Quanten-Features
# model = LinearRegression()
# model.fit(QR_output, y_train)
#
# print("Quanten-Features Shape:", QR_output.shape)
# print("Vorhersage für neue Daten:", model.predict(QR_output[:1]))