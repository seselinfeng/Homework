from AppSpecificTesting.pages.transcation import Transcation
from FrameworkOptimization.pages.basepage import BasePage


class Main(BasePage):

    def goto_transcation(self):
        self.steps('../data/main.yaml')
        return Transcation(self._driver)
