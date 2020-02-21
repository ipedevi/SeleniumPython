import os
import allure
from datetime import datetime
from selenium import webdriver
from pathlib import Path
from Source.Framework import myconfig

""" This class is used to manage Selenium driver """

""" CONS """
SEPARATOR = os.path.sep


def get_project_root() -> Path:
    """ Returns project root folder. """
    return Path(__file__).parent.parent.parent


def get_img_name():
    """ Returns an unique name for screenshots based on time  """
    hora = datetime.now().time()
    root_dir = get_project_root()
    name = str(root_dir)
    name += SEPARATOR
    name += "results"
    if not os.path.exists(name):
        os.makedirs(name)
    name += SEPARATOR
    name += "images"
    if not os.path.exists(name):
        os.makedirs(name)
    name += SEPARATOR
    name += "screenshot_"
    name += hora.strftime("%m%d%Y_%H%M%S")
    name += ".png"
    return name


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

    def __init__(self, *args):
        """ Where the driver is initialized. Now, it only works with firefox and chrome.  """
        if len(args) == 1:
            browser = args[0]
        else:
            browser = myconfig.default_browser
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        # elif browser == "chrome":
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) # seconds
        self.get_selenium_frm()

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
        cls.driver.close()
