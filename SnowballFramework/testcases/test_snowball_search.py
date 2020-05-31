from SnowballFramework.pages.App import App


class TestSnowballSearch():
    def setup(self):
        self.app = App()
        self.serach = self.app.start().main().goto_market().goto_search()

    def teardown(self):
        self.app.stop()

    def test_search(self):
        self.serach.serach('阿里巴巴', 'BABA')
        assert self.serach.is_choose('BABA')
