from exceptions import data_loading_failed_exception
from enum import Enum

class station(Enum):
    station1 = 1
    station2 = 2
    station3 = 3


class Geosphere:
    def __init__(self, loc: station):
        fileID = "station-{}.csv".format(str(loc.value))


    def load_data_into_memory(self):
        try:
            data = self.load_data_from_file()
            if not data is None:
                return data

            data = self.download_data()
            if not data is None:
                return data

        except:
            raise data_loading_failed_exception()


    def download_data(self):
        print("Downloading data from {}".format(__name__))
        #TODO
        return []


    def load_data_from_file(self):
        print("Loading data from file")
        open()
        return []
