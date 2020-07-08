import requests


class TestDepartment:
    def test_token(self):
        """获取企业微信token"""
        corpid = 'wwb955cd8075e8cbe0'
        corpsecret = "RT3G7HNqgxEzMVx7JB3ZVs_ZVio3QS7wun0K4z9g0po"
        res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
        return res.json()['access_token']

    def test_create(self):
        """添加部门"""
        data = {
            "name": "广州研发中心",
            "parentid": 1
        }
        res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.test_token()}",
                            json=data)
        print(res.json())

    def test_update(self):
        """更新部门"""
        data = {
            "id": 2,
            "name": "上海研发中心"
        }
        res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.test_token()}",
                            json=data)
        print(res.json())

    def test_delete(self):
        """删除部门"""
        res = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.test_token()}&id=2")

    def test_get_department(self):
        """获取部门列表"""
        res = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.test_token()}&id={1}")
        print(res.json())
