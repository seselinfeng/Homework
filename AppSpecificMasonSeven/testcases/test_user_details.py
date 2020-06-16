from AppSpecificMasonSeven.pages.app import App


class TestUserDetail():
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_user_detail(self):
        result =  self.main.login().goto_me().goto_user_details().get_time()
        print(result)
