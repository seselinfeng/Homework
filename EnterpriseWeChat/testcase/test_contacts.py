import pytest

from EnterpriseWeChat.common.processingdata import get_data
from EnterpriseWeChat.page.main import Main


class TestContacts():
    def setup(self):
        self.main = Main()

    @pytest.mark.parametrize(("username", "acctid", "phone"),
                             get_data('test_add_member', '../data/test_add_member.yaml'))
    def test_add_member(self, username, acctid, phone):
        add_member = self.main.goto_add_member()
        add_member.add_member(username, acctid, phone)
        assert add_member.get_member(username)
