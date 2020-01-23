import datetime
import allure

@allure.attach
def takeScreenshot(driver):
    name = "screenshot_"+datetime.datetime.now().time()
    driver.save_screenshot(name)
