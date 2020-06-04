import inspect

import pytest
import yaml

from FrameworkOptimization.common.processingdata import get_data
from FrameworkOptimization.pages.app import App


class TestSearch():
    def setup(self):
        self.app = App()
        self.search = self.app.start().main().goto_market().goto_search()

    @pytest.mark.parametrize(("name", "value"), get_data('test_search', '../data/test_search.yaml'))
    def test_search(self, name, value):
        self.search.search(name, value)
        if self.search.is_choose(value):
            self.search.del_custom(value)
        self.search.add_custom(value)
        assert self.search.is_choose(value)
