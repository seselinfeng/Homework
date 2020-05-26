from appium.webdriver.common.mobileby import MobileBy

from CorporateWeChat.page.BasePage import BasePage
from CorporateWeChat.page.EditMember import EditMember


class MemberInfoOperation(BasePage):
    def edit_member(self):
        """
        点击编辑成员按钮，进入编辑成员页面
        :return:编辑成员页面
        """
        self.find(MobileBy.ID,"com.tencent.wework:id/azk").click()
        return EditMember(self._driver)