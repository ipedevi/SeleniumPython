class BasePage(object):
    """Base class to initialize the base page that will be called from all pages,
     it also can include some specific tools"""

    def __init__(self, driver):
        self.driver = driver
