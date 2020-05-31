from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from SnowballFramework.pages.BasePage import BasePage


class Search(BasePage):
    def serach(self, name, value):
        self.find(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(name)
        self.find(MobileBy.XPATH, f'//*[@text="{value}"]/..').click()
        self.find(MobileBy.XPATH, f"//*[@text='{value}']/../../..//*[@text='加自选']").click()

    def is_choose(self, value):
        element: WebElement = self.find(MobileBy.XPATH, f"//*[@text='{value}']/../../..//*[@text='已添加']")
        return True if element else False

        # # 用于生成xpath定位
        # toast_message = "已关注"
        # message = '//*[@text=\'{}\']'.format(toast_message)
        # # 获取toast提示框内容
        # result = WebDriverWait(self, 5).until(lambda x: x.find(MobileBy.XPATH, message)).text
        # return result == "已关注"
