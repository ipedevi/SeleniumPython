import pytest
import allure
from selenium import webdriver
from SeleniumTest.Module import myconfig
from SeleniumFrm.seleniumFrm import Selenium


def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    print(item)
    print("setting up!!!")


@pytest.fixture(autouse=True)
def populate_globals():
    # called every test
    # Selenium.driver = Selenium(myconfig.browser)
    if myconfig.browser == "firefox":
        allure.step("Se inicia con Firefox.")
        Selenium.driver = webdriver.Firefox()
    elif myconfig.browser == "chrome":
        allure.step("Se inicia con Chrome.")
        Selenium.driver = webdriver.Chrome()
    else:
        allure.step("Browser no indicado, se inicia con chrome.")
        print("Browser no indicado, se inicia con chrome.")
        Selenium.driver = webdriver.Chrome()
