import numpy as np
from sklearn.linear_model import LinearRegression

from my_qiskit.impl import get_qrc_features

# --- BEISPIEL ANWENDUNG ---

# Beispiel-Daten (X: Zeitreihen-Fenster, y: Zielwert)
X_raw = [[0.1, 0.2], [0.2, 0.3], [0.3, 0.4]]
y_train = [0.5, 0.6, 0.7]

# Features durch das Quanten-Reservoir generieren
X_quantum = np.array([get_qrc_features(seq,3) for seq in X_raw])

# Klassische Lineare Regression auf den Quanten-Features
model = LinearRegression()
model.fit(X_quantum, y_train)

print("Quanten-Features Shape:", X_quantum.shape)
print("Vorhersage für neue Daten:", model.predict(X_quantum[:1]))