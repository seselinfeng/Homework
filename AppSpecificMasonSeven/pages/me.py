from AppSpecificMasonSeven.pages.basepage import BasePage
from AppSpecificMasonSeven.pages.userdetails import UserDetails


class Me(BasePage):
    def goto_user_details(self):
        self.steps('../data/me.yaml')
        return UserDetails(self._driver)