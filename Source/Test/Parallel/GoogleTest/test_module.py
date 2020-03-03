import allure
import pytest
from selenium import webdriver
from Source.Framework.seleniumFrm import *
from Source.Test.Parallel import myconfig
from Source.Test.Parallel.PageObjects.GoogleResultsPage import GoogleResultPage
from Source.Test.Parallel.PageObjects.GoogleSearchPage import GoogleSearchPage
from Source.Framework.seleniumFrm import setup


wordToSeek = "TestAcademy"
urlToCheck = "www.spanishtestacademy.com"


@pytest.mark.usefixtures("setup")
class TestClass:

    @allure.epic('EPIC OBJECT ORIENTED')
    @allure.description('DESCRIPTION TEST 1')
    @allure.feature('FEATURE TEST 1')
    @allure.story('STORY TEST 1')
    def test(self):
        try:
            google_search_page = GoogleSearchPage(Selenium.driver)
            google_search_page.initiate(myconfig.urlInicial)
            google_search_page.search_word(wordToSeek)

            google_result_page = GoogleResultPage(Selenium.driver)
            assert google_result_page.check_url(urlToCheck)
            print("TEST5: URL 'www.spanishtestacademy.com' encontrada en la primera posicion con PageObjects.")

        finally:
            Selenium.close()


if __name__ == "__main__":
    # Usado para ejectar en local
    Selenium.driver = webdriver.Chrome()
    TestClass().test()
