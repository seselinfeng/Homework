from appium.webdriver import WebElement

from FrameworkOptimization.pages.basepage import BasePage


class Search(BasePage):
    def search(self, name, value):
        self._params["name"] = name
        self._params["value"] = value
        self.steps("../data/search.yaml")

    def add_custom(self, value):
        self._params["value"] = value
        self.steps("../data/search.yaml")

    def is_choose(self, value):
        self._params["value"] = value
        element: WebElement = self.steps("../data/search.yaml")
        return True if element else False

    def del_custom(self, value):
        self._params["value"] = value
        self.steps("../data/search.yaml")
