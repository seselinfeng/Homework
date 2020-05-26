from appium.webdriver.common.mobileby import MobileBy

from CorporateWeChat.page.BasePage import BasePage
from CorporateWeChat.page.MemberInfoOperation import MemberInfoOperation


class MemberInfo(BasePage):
    def member_info_detail(self):
        """
        点击右上角〓图标，进入个人信息操作页面
        :return: 个人信息操作页面
        """
        self.find(MobileBy.ID,"com.tencent.wework:id/gvd").click()
        return MemberInfoOperation(self._driver)