from appium.webdriver.common.mobileby import MobileBy

from SnowballFramework.pages.BasePage import BasePage
from SnowballFramework.pages.Search import Search


class Market(BasePage):
    def goto_search(self):
        self.find(MobileBy.ID, 'com.xueqiu.android:id/action_search').click()
        return Search(self._driver)