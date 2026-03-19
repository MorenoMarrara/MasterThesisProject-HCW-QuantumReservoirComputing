import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def get_qrc_features(input_sequence, n_qubits=4):
    """
    Wandelt eine Zeitreihe in einen hochdimensionalen Quantenzustand um
    und extrahiert die Erwartungswerte als Features.
    """
    qc = QuantumCircuit(n_qubits)

    # 1. Daten sukzessive einspeisen (Temporal Processing)
    for val in input_sequence:
        for i in range(n_qubits):
            qc.ry(val * np.pi, i)  # Input Encoding

        for i in range(n_qubits - 1):
            qc.cx(i, i + 1)  # Dynamik / Verschränkung

    # 2. Messung vorbereiten (Snapshot der Dynamik)
    qc.measure_all()

    # 3. Simulation ausführen
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1024).result()
    counts = result.get_counts()

    # 4. Feature-Vektor berechnen (Erwartungswert <Z> pro Qubit)
    # Wir berechnen hier vereinfacht die Wahrscheinlichkeit, dass ein Qubit '1' ist
    features = np.zeros(n_qubits)
    for bitstring, count in counts.items():
        for i, bit in enumerate(reversed(bitstring)):  # Qiskit Bit-Order beachten
            if bit == '1':
                features[i] += count

    return features / 1024  # Normalisierung auf [0, 1]

