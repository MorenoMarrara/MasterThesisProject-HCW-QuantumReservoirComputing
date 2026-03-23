from unittest import TestCase
from src.data.loading.geosphere import Geosphere


class TestGeosphere(TestCase):
    def test_init(self):
        loader = Geosphere()
        assert Geosphere

    def test_load(self):
        loader = Geosphere()
        all_data = loader.load_data()
        assert all_data

    def test_load_data_from_file(self):
        loader = Geosphere()
        all_data = loader.load_data_from_file()
        assert all_data
