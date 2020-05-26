import allure
from appium.webdriver.common.mobileby import MobileBy

from CorporateWeChat.page.BasePage import BasePage
from CorporateWeChat.page.MemberInfo import MemberInfo
from CorporateWeChat.page.MemberInvite import MemberInvite


class Address(BasePage):
    """团队tab-添加成员button"""
    @allure.title("跳转到添加成员界面")
    def add_member(self):
        """
        点击团队tab-点击button【添加成员】
        :return: 添加成员页面
        """
        self.find(MobileBy.XPATH, "//*[@text='添加成员...']").click()
        return MemberInvite(self._driver)

    def goto_member_info(self,name):
        """
        点击成员名称，
        :return: 个人信息页面
        """
        self.find(MobileBy.XPATH, f"//*[@text='{name}']").click()
        return MemberInfo(self._driver)
