from unittest import TestCase
from src.data.loading.geosphere import Geosphere


class TestGeosphere(TestCase):
    # TODO: add missing test cases

    def test_init(self):
        loader = Geosphere()
        assert Geosphere

    def test_load_data_into_memory(self):
        loader = Geosphere()
        all_data = loader.load_data_into_memory()
        assert not (all_data is None)

    def test_load_data_from_file(self):
        loader = Geosphere()
        all_data = loader.load_data_from_file()
        assert not (all_data is None)
