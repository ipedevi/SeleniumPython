from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

wordToSeek = "TestAcademy"
urlToCheck = "www.spanishtestacademy.com"
try:

    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    driver.get("https://www.google.es")

    element = driver.find_element_by_xpath("id('tsf')//input[@type= 'text']")
    element.send_keys(wordToSeek)
    element.send_keys(Keys.RETURN)

    # wait for element to appear, then hover it
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.XPATH, "id('rso')/div[1]")))
    element = driver.find_element_by_xpath("id('rso')/div[1]")

    # print(element.text)
    assert urlToCheck in element.text, "Elemento no encontrado"
    print("TEST1: URL 'www.spanishtestacademy.com' encontrada en la primera posicion.")
finally:
    driver.close()