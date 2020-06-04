from FrameworkOptimization.pages.basepage import BasePage
from FrameworkOptimization.pages.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps('../data/main.yaml')
        return Market(self._driver)
