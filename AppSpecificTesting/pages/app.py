from appium import webdriver

from AppSpecificTesting.pages.basepage import BasePage
from AppSpecificTesting.pages.main import Main


class App(BasePage):
    def start(self):
        if self._driver is None:
            desire_cap = {
                "platformName": "android",
                "deviceName": "S2D0219430000212",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "noReset": "true",  # 记住关闭首次启动弹窗状态，再次启动不会打开弹窗
                'chromedriverExecutable': "/Users/apple/Documents/web/chromedriver",
                'unicodeKeyBoard': True,  # 支持中文键盘输入
                'skipDeviceInitialization': True,
                'skipLogcatCapture': True,
                'skipServerInstallation': True,
                'resetKeyBoard': True
            }
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)
        return self

    def stop(self):
        self._driver.quit()

    def restart(self):
        pass

    def main(self):
        return Main(self._driver)
