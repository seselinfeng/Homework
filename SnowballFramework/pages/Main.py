from appium.webdriver.common.mobileby import MobileBy

from SnowballFramework.pages.BasePage import BasePage
from SnowballFramework.pages.Market import Market


class Main(BasePage):
    def goto_market(self):
        self.find(MobileBy.XPATH,
                  '//*[@resource-id="android:id/tabs"]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]').click()
        return Market(self._driver)
