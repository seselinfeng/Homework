from appium.webdriver.common.mobileby import MobileBy

from CorporateWeChat.page.BasePage import BasePage


class ContactAdd(BasePage):
    """添加成员信息"""

    def input_name(self, name):
        """
        输入成员名称
        :param name:
        :return: 本页面
        """
        self.find(MobileBy.XPATH, f"//*[@text='姓名　']/..//*[@class='android.widget.EditText']").send_keys(name)
        return self

    def set_gender(self, gender='男'):
        """
        选择性别
        :param gender:
        :return: 本页面
        """
        self.find(MobileBy.XPATH,
                  "//*[@text='性别']/..//*[@resource-id='com.tencent.wework:id/av9']").click()
        self.find(MobileBy.XPATH, f"//*[@text='{gender}']").click()
        return self

    def input_phone_num(self, phone_num):
        """
        输入电话号码
        :param phone_num:
        :return: 本页面
        """
        self.find(MobileBy.ID, "com.tencent.wework:id/eqx").send_keys(phone_num)
        return self

    def click_save(self):
        """
        保存成员
        :return:添加成员页面
        """
        from CorporateWeChat.page.MemberInvite import MemberInvite
        self.find(MobileBy.ID, "com.tencent.wework:id/gvk").click()
        return MemberInvite(self._driver)
