from AppSpecificMasonSeven.pages.basepage import BasePage


class UserDetails(BasePage):
    def get_time(self):
        print("context:{}".format(self._driver.contexts))
        webview = self._driver.contexts[-1]
        self._driver.switch_to.context(webview)
        performance = self._driver.execute_script("return window.performance.timing")
        print(performance)
        result = performance['connectStart'] - performance['responseEnd']
        return result
