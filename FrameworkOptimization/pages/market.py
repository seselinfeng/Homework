import yaml
from appium.webdriver.common.mobileby import MobileBy

from FrameworkOptimization.pages.basepage import BasePage
from FrameworkOptimization.pages.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../data/market.yaml")
        return Search(self._driver)
