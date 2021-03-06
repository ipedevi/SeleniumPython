import allure
from selenium import webdriver
from Source.Framework.seleniumFrm import Selenium
from Source.Test.Module.PageObjects.GoogleResultsPage import GoogleResultPage
from Source.Test.Module.PageObjects.GoogleSearchPage import GoogleSearchPage
from Source.Test.Module import myconfig

# Para ejecutar, hacerlo desde powershell/terminal segun:
#    pip install allure-pytest
#    py.test --alluredir=./results ./Test/Allure
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
