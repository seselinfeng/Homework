## 跳过登录实现步骤
1. 打开复用模式
```python3
    options = Options()
    options.debugger_address = "127.0.0.1:9222"
    self.driver = webdriver.Chrome('/Users/apple/Documents/web/chromedriver', options=options)
```
2. 访问企业微信并获取cookies，将cookies通过shelve模块存储，该模块等价于小型db数据库
```python3
    self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    db = shelve.open('cookies')
    db['cookie'] = self.driver.get_cookies()
```
3. 关闭复用模式
```python3
    self.driver = webdriver.Chrome('/Users/apple/Documents/web/chromedriver')
```
4. 访问企业微信并添加cookie
```
 self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
 db = shelve.open('cookies')
 cookies = db['cookie']
    for cookie in cookies:
        if 'expiry' in cookie.keys():
            cookie.pop("expiry")
        self.driver.add_cookie(cookie)
```
5. 再次访问企业微信，此时页面已经是登录态，可以操作登录后的element了
```python3
 self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
 self.driver.find_element_by_id('menu_contacts').click()
```
6. 关闭shelve
```python3
 db.close()
```
