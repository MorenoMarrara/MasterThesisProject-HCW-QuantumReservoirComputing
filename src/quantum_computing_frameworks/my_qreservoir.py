# qreservoir is a simulation framework that is built on the quantum computing simulator qulacs
# https://pypi.org/project/qulacs/
from qreservoir.abstract_base_classes import Encoder, Reservoir
from qreservoir.encoders import CHEEncoder
from qreservoir.models import RCModel
from qreservoir.reservoirs import CNOTReservoir
from qulacs import Observable
from sklearn.linear_model import LinearRegression

# found on GitHub and installed using pip.

# qreservoir is easily used but configuration will be hardest part:
# - start by constructing the RCModel object (multidim input sequences are supported):
#  . reservoir:

class BaseRCModel(RCModel):
    def __init__(self, number_of_qubits: int = 1, number_of_features: int = 1):
        observables = [Observable(number_of_qubits) for _ in range(number_of_features)]
        [observable.add_operator(1.0, f"I 0") for observable in observables]

        super().__init__(CNOTReservoir(CHEEncoder(number_of_features), number_of_qubits, 1),
                         observables,
                         LinearRegression()
        )