import argparse
import os
from configparser import ConfigParser
import allure
from datetime import datetime
import pytest
from selenium import webdriver
from pathlib import Path
from Source.Framework.config import Config

""" This class is used to manage Selenium driver """

""" CONS """
config = Config()


def get_project_root() -> Path:
    """ Returns project root folder. """
    return Path(__file__).parent.parent.parent


def get_img_name():
    """ Returns an unique name for screenshots based on time  """
    hora = datetime.now().time()
    root_dir = get_project_root()
    name = str(root_dir)
    name += config.SEPARATOR
    name += "results"
    if not os.path.exists(name):
        os.makedirs(name)
    name += config.SEPARATOR
    name += "images"
    if not os.path.exists(name):
        os.makedirs(name)
    name += config.SEPARATOR
    name += "screenshot_"
    name += hora.strftime("%m%d%Y_%H%M%S")
    name += ".png"
    return name


def load_configuration():
    ''' Used to read conf file + properties + ...
    order:
    1) --browser=firefox
    2) looks in myframework.config (in root folder)
    3) Take standard as defined in Config()
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--browser', help='Browser to open selenium', required=False)
    args = parser.parse_known_args()
    if args[0].__getattribute__("browser") is not None:
        config.default_browser = args[0].__getattribute__("browser")
    else:
        parser = ConfigParser()
        config_file = str(get_project_root()) + config.SEPARATOR + 'myframework.config'
        parser.read(config_file)
        if parser.has_option("SELENIUM", "default_browser"):
            config.default_browser = str(parser.get("SELENIUM", "default_browser")).replace('"', "")


@pytest.fixture(scope="session")
def setup(request):
    """ Used to initiate Selenium automatically when execute pytest, called every test """
    load_configuration()

    if config.default_browser == "firefox":
        allure.step("Starting Firefox.")
        Selenium.driver = webdriver.Firefox()
    elif config.default_browser == "chrome":
        allure.step("Starting Chrome.")
        Selenium.driver = webdriver.Chrome()
    elif config.default_browser == "chrome-local-webdriver":
        allure.step("Starting Chrome in webdriver local.")
        options = webdriver.ChromeOptions()
        capabilities = options.to_capabilities()
        Selenium.driver = webdriver.Remote(
            command_executor=config.command_executor,
            desired_capabilities=capabilities)
    elif config.default_browser == "firefox-local-webdriver":
        allure.step("Starting Firefox in webdriver local.")
        options = webdriver.FirefoxOptions()
        capabilities = options.to_capabilities()
        Selenium.driver = webdriver.Remote(
            command_executor=config.command_executor,   # 'http://127.0.0.1:4444/wd/hub'
            desired_capabilities=capabilities)
    else:
        allure.step("Using standard Browser (chrome).")
        Selenium.driver = webdriver.Chrome()
    Selenium.driver.implicitly_wait(config.implicit_wait)  # 10 seconds
    Selenium.driver.maximize_window()


def take_screenshot(driver):
    """ Function to take screenshots """
    name = get_img_name()
    driver.save_screenshot(name)
    allure.attach.file(name, name="Screenshot", attachment_type=allure.attachment_type.PNG)


def check(boolean_var, driver):
    """ Function to add extra capabilities to assert """
    if not boolean_var:
        take_screenshot(driver)
    assert boolean_var


class Selenium:
    """ Class to manage the driver """
    driver = None

    def get_selenium_frm(self):
        """ Getter """
        return self.driver

    def __set__(self, newdriver):
        """ Setter """
        self.driver = newdriver

    @classmethod
    @allure.step("Closing Webdriver")
    def close(cls):
        """ Where the driver is closed """
        take_screenshot(cls.driver)
        cls.driver.quit()
