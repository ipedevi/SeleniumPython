import pytest
import allure
from selenium import webdriver
from Source.Framework import myconfig
from Source.Framework.seleniumFrm import Selenium

def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    print(item)
    print("setting up!!!")

@pytest.fixture(autouse=True)
def populate_globals():
    """ Used to initiate Selenium automatically when execute pytest, called every test """
    if myconfig.default_browser == "firefox":
        allure.step("Starting Firefox.")
        Selenium.driver = webdriver.Firefox()
    elif myconfig.default_browser == "chrome":
        allure.step("Starting Chrome.")
        Selenium.driver = webdriver.Chrome()
    else:
        allure.step("Using standard Browser (chrome).")
        Selenium.driver = webdriver.Chrome()
