import os
from datetime import datetime

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from pathlib import Path

SEPARATOR = os.path.sep


def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent


def get_img_name():
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


class Selenium:

    def __init__(self, *args):

        if len(args) == 1:
            browser = args[0]
        else:
            browser = "chrome"

        if browser == "firefox":
            self.python_selenium = webdriver.Firefox()
        # elif browser == "chrome":
        else:
            self.python_selenium = webdriver.Chrome()
        self.get_selenium_frm()

    def get_selenium_frm(self):
        return self.python_selenium

    @allure.step
    def take_screenshot(driver):
        # self.python_selenium.save_screenshot(name)
        name = get_img_name()
        driver.save_screenshot(name)
        # allure.attach("Screenshot")
        allure.attach.file(name, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        # allure.attach(driver.save_screenshot(get_img_name()), name="Screenshot", attachment_type=AttachmentType.PNG)
