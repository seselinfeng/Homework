from AppSpecificMasonSeven.pages.dashboard import Dashboard
from FrameworkOptimization.pages.basepage import BasePage


class Main(BasePage):

    def login(self):
        self.steps('../data/main.yaml')
        return Dashboard(self._driver)
