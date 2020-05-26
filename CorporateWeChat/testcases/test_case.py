from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy


class TestCorporateWeChat():
    def setup_class(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "S2D0219430000212",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": "true",  # 记住关闭首次启动弹窗状态，再次启动不会打开弹窗
            'unicodeKeyBoard': True,  # 支持中文键盘输入
            'skipDeviceInitialization': True,
            'skipLogcatCapture': True,
            'skipServerInstallation': True,
            'resetKeyBoard': True
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    def teardown(self):
        pass

    def test_addmember(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='团队']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员...']").click()
        #self.driver.implicitly_wait()
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/h3a').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='姓名　']/..//*[@class='android.widget.EditText']").send_keys('李福庆1')
        self.driver.find_element(MobileBy.XPATH,"//*[@text='性别']/..//*[@resource-id='com.tencent.wework:id/av9']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/eqx").send_keys('18912345679')
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/gvk").click()