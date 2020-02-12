import allure
from SeleniumFrm.BasePage import BasePage
from selenium.webdriver.common.keys import Keys

search_bar_xpath = "id('tsf')//input[@type= 'text']"


class GoogleSearchPage(BasePage):
    """Page Object of Google Search Page"""

    @allure.step
    def initiate(self, url):
        self.driver.get(url)

    @allure.step
    def search_word(self, word_to_seek):
        element = self.driver.find_element_by_xpath(search_bar_xpath)
        element.send_keys(word_to_seek)
        element.send_keys(Keys.RETURN)