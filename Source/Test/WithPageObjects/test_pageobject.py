import allure
from Source.Framework import Selenium
from Source.Test.WithPageObjects import GoogleResultPage
from Source.Test.WithPageObjects.PageObjects.GoogleSearchPage import GoogleSearchPage

# Para ejecutar, hacerlo desde powershell/terminal segun:
#    pip install allure-pytest
#    py.test --alluredir=./results ./Test/Allure
#    allure serve C:\Users\Ivan\PycharmProjects\SeleniumAutomation\results


wordToSeek = "TestAcademy"
urlToCheck = "www.spanishtestacademy.com"
urlInicial = "https://www.google.es"


@allure.epic('EPIC PAGE OBJECTS')
@allure.description('DESCRIPTION 2b')
@allure.feature('FEATURE 2b')
@allure.story('STORY 1b')
def test():
    try:
        # Initialize the selenium browser
        # driver = Selenium().get_selenium_frm()
        driver = Selenium("firefox").get_selenium_frm()

        google_search_page = GoogleSearchPage(driver)
        google_search_page.initiate(urlInicial)
        google_search_page.search_word(wordToSeek)

        google_result_page = GoogleResultPage(driver)
        assert google_result_page.check_url(urlToCheck)
        print("TEST4: URL 'www.spanishtestacademy.com' encontrada en la primera posicion con PageObjects.")

    except Exception as e:
        print("Error en el test: ")
        print(e)

    finally:
        driver.close()


if __name__ == "__main__":
    test()
