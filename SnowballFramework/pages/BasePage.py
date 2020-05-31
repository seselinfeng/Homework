from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from SnowballFramework.pages.Decorator import handle_black


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @handle_black
    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element
