#conftest.py
import pytest


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', dest='env')