import allure
import pytest
import yaml
from CorporateWeChat.common.log import Log
from CorporateWeChat.page.App import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def teardown(self):
        self.app.stop()

    @allure.title("添加用户")
    @pytest.mark.parametrize(("name", "gender", "phone_num"), yaml.safe_load(open("../datas/add_contact_data.yaml")))
    def test_add_contact(self, name, gender, phone_num):
        with allure.step("手动添加用户"):
            invitpage = self.main.goto_team().add_member().addmember_by_manul().input_name(name).set_gender(
                gender).input_phone_num(phone_num).click_save()
        assert '成功' in invitpage.get_toast()
        Log.info('添加用户{name}成功'.format(name))

    @allure.title("删除用户")
    @pytest.mark.parametrize("name", yaml.safe_load(open("../datas/del_contact_data.yaml")))
    def test_del_contact(self, name):
        with allure.step('删除用户'):
            delcontactpage = self.main.goto_team().goto_member_info(
                name).member_info_detail().edit_member().del_member().confirm_del()
        Log.info('删除用户{name}成功'.format(name))
