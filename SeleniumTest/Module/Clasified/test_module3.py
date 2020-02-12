import allure
from selenium import webdriver
from SeleniumFrm.seleniumFrm import Selenium
from SeleniumTest.WithPageObjects.PageObjects.GoogleResultsPage import GoogleResultPage
from SeleniumTest.WithPageObjects.PageObjects.GoogleSearchPage import GoogleSearchPage
from SeleniumTest.Module import myconfig

# Para ejecutar, hacerlo desde powershell/terminal segun:
#    pip install allure-pytest
#    py.test --alluredir=./results ./SeleniumTest/Allure
#    allure serve C:\utils\workspace\Python\SeleniumPython\results


wordToSeek = "microsoft"
urlToCheck = "www.microsoft.com"


class TestClass:

    @allure.epic('EPIC OBJECT ORIENTED')
    @allure.description('DESCRIPTION TEST 3')
    @allure.feature('FEATURE TEST 3')
    @allure.story('STORY TEST 3')
    def test(self):
        try:
            google_search_page = GoogleSearchPage(Selenium.driver)
            google_search_page.initiate(myconfig.urlInicial)
            google_search_page.search_word(wordToSeek)

            google_result_page = GoogleResultPage(Selenium.driver)
            assert google_result_page.check_url(urlToCheck)
            print("TEST5c: URL 'www.expoqa.com' encontrada en la primera posicion.")

        finally:
            Selenium.driver.close()


if __name__ == "__main__":
    # Usado para ejectar en local
    Selenium.driver = webdriver.Chrome()
    TestClass().test()