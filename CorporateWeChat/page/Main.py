import allure
from appium.webdriver.common.mobileby import MobileBy

from CorporateWeChat.page.Address import Address
from CorporateWeChat.page.BasePage import BasePage


class Main(BasePage):
    """主页面"""

    def goto_message(self):
        pass

    def goto_dates(self):
        pass

    def goto_docs(self):
        pass

    @allure.title("跳转到团队界面")
    def goto_team(self):
        self.find(MobileBy.XPATH, "//*[@text='团队']").click()
        return Address(self._driver)
