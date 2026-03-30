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

# builder function for RC Model
def build_RCModel(reservoir: Reservoir = None,
                  number_of_qubits: int = 1) \
        -> RCModel:

    if reservoir is not None:         # create Base RCModel:
        observable = Observable(number_of_qubits)
        observable.add_operator(1.0, f"Y 0")
        estimator = LinearRegression()
        return RCModel(reservoir, [observable], estimator)
    else:
        raise Exception("No reservoir provided.")

def build_base_RCModel(number_of_qubits: int = 1,
                       number_of_features: int = 1) \
    -> RCModel:
    return build_RCModel(CNOTReservoir(CHEEncoder(number_of_features), number_of_qubits, 1))