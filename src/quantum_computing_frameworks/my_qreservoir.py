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
def build_RCModel(encoder: Encoder,
                  reservoir: Reservoir = None,
                  number_of_qubits: int = 1,
                  number_of_features: int = 1,
                  ancilla_num: int = 1,
                  depth: int = 1) \
        -> RCModel:

    if reservoir is not None:         # create Base RCModel:
        reservoir = reservoir(encoder(number_of_features), ancilla_num, depth)
        observable = Observable(number_of_qubits)
        estimator = LinearRegression()
    return RCModel(reservoir, [observable], estimator)

def build_base_RCModel(number_of_qubits: int = 1,
                       number_of_features: int = 1,
                       ancilla_num: int = 1,
                       depth: int = 1) \
    -> RCModel:
    return build_RCModel(CHEEncoder, CNOTReservoir, number_of_qubits, number_of_features, ancilla_num, depth)