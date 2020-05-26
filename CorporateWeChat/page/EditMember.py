from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from CorporateWeChat.page.BasePage import BasePage


class EditMember(BasePage):
    def del_member(self):
        """
        点击删除成员 ，点击确定按钮
        :return: 返回Address页面
        """
        self.find(MobileBy.ID, "com.tencent.wework:id/dve").click()
        return self

    def confirm_del(self):
        from CorporateWeChat.page.Address import Address
        self.find(MobileBy.ID, "com.tencent.wework:id/b_a").click()
        WebDriverWait(self._driver, 5).until(
            lambda x: x.find_element(MobileBy.ID, "com.tencent.wework:id/b_a")).click()
        return Address(self._driver)
