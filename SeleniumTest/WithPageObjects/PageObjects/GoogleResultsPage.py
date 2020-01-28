import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from SeleniumFrm.BasePage import BasePage

from SeleniumFrm.seleniumFrm import Selenium

first_result_xpath = "id('rso')/div[1]"


class GoogleResultPage(BasePage):
    """Page Object of Google result Page"""

    @allure.step
    def check_url(self, url_to_check):
        # wait for element to appear, then hover it
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.XPATH, first_result_xpath)))
        element = self.driver.find_element_by_xpath(first_result_xpath)
        Selenium.take_screenshot(self.driver)
        return url_to_check in element.text

