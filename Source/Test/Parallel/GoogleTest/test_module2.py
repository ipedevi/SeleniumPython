import allure
import pytest
from selenium import webdriver
from Source.Framework.seleniumFrm import Selenium
from Source.Test.Parallel import myconfig
from Source.Test.Parallel.PageObjects.GoogleResultsPage import GoogleResultPage
from Source.Test.Parallel.PageObjects.GoogleSearchPage import GoogleSearchPage
from Source.Framework.seleniumFrm import setup


wordToSeek = "expoqa"
urlToCheck = "www.expoqa.com"


@pytest.mark.usefixtures("setup")
class TestClass:

    @allure.epic('EPIC OBJECT ORIENTED')
    @allure.description('DESCRIPTION TEST 2')
    @allure.feature('FEATURE TEST 2')
    @allure.story('STORY TEST 2')
    def test(self):
        try:
            google_search_page = GoogleSearchPage(Selenium.driver)
            google_search_page.initiate(myconfig.urlInicial)
            google_search_page.search_word(wordToSeek)

            google_result_page = GoogleResultPage(Selenium.driver)
            assert google_result_page.check_url(urlToCheck)
            print("TEST5b: URL 'www.expoqa.com' encontrada en la primera posicion.")

        finally:
            Selenium.driver.close()


if __name__ == "__main__":
    # Usado para ejectar en local
    Selenium.driver = webdriver.Chrome()
    TestClass().test()
