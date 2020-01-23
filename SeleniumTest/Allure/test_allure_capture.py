import allure
from SeleniumFrm import utils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

 # Para ejecutar, hacerlo desde powershell/terminal segun:
 #    pip install allure-pytest
 #    py.test --alluredir=./results ./SeleniumTest/test_allure.py
 #    allure serve C:\Users\Ivan\PycharmProjects\SeleniumAutomation\results

wordToSeek = "TestAcademy"
urlToCheck = "www.spanishtestacademy.com"

@allure.step
def initiate(driver):
    driver.get("https://www.google.es")

@allure.step
def searchWord(driver):
    element = driver.find_element_by_xpath("id('tsf')//input[@type= 'text']")
    element.send_keys(wordToSeek)
    element.send_keys(Keys.RETURN)

@allure.step
def checkUrl(driver):
    # wait for element to appear, then hover it
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.XPATH, "id('rso')/div[1]")))
    element = driver.find_element_by_xpath("id('rso')/div[1]")
    # print(texto)
    assert urlToCheck in element.text, "Elemento no encontrado"
    print("TEST2: URL 'www.spanishtestacademy.com' encontrada en la primera posicion con Allure.")
    # return element.text

@allure.epic('EPIC 1')
@allure.description('DESCRIPTION 1')
@allure.feature('FEATURE 1')
@allure.story('STORY 1')
def test():
    try:
        driver = webdriver.Firefox()
        # driver = webdriver.Chrome()

        utils.takeScreenshot(driver)

        initiate(driver)
        searchWord(driver)
        checkUrl(driver)
        # texto = checkUrl(driver)

    finally:
        driver.close()


if __name__ == "__main__":
    test()