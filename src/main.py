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

# data = load_data_from(Geosphere())

data = Geosphere().load_data_into_memory()
X_raw, y_train = data["dd", "ddx"], data["pred"]

# Features durch das Quanten-Reservoir generieren
X_quantum = np.array([get_qrc_features(seq,2) for seq in X_raw])

# Klassische Lineare Regression auf den Quanten-Features
model = LinearRegression()
model.fit(X_quantum, y_train)

print("Quanten-Features Shape:", X_quantum.shape)
print("Vorhersage für neue Daten:", model.predict(X_quantum[:1]))