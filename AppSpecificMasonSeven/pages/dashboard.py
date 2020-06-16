from AppSpecificMasonSeven.pages.basepage import BasePage
from AppSpecificMasonSeven.pages.me import Me


class Dashboard(BasePage):
    def goto_me(self):
        self.steps('../data/dashboard.yaml')
        return Me(self._driver)
