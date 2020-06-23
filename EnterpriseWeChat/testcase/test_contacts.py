from time import sleep

import pytest

from EnterpriseWeChat.common.log import Log
from EnterpriseWeChat.common.processingdata import get_data
from EnterpriseWeChat.page.main import Main


class TestContacts():
    def setup(self):
        self.main = Main()
        self.log = Log()

    @pytest.mark.parametrize(("username", "acctid", "phone"),
                             get_data('test_add_member', '../data/test_add_member.yaml'))
    def test_add_member(self, username, acctid, phone):
        contacts = self.main.goto_contacts()
        if contacts.get_member(username):
            if contacts.del_member(username):
                contacts.goto_add_member().add_member(username, acctid, phone)
            else:
                self.log.error("{}添加失败".format(username))
        else:
            contacts.goto_add_member().add_member(username, acctid, phone)
        assert contacts.get_member(username)
