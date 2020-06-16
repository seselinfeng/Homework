from AppSpecificTesting.pages.app import App


class TestTransaction:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_transaction(self):
        self.main.goto_transcation().get_time()
