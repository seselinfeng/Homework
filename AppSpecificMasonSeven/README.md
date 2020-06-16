## app专项测试实战1 作业
1. 通过appium完成启动APP-Me页面自动化流程
```python3
   # 切换到webview，才可以通过execute_script方法执行js脚本
   webview =driver.swith_to.context(driver.contexts[-1])
```
2. 通过js获取页面加载时间的获取工作
```javascript
    window.performance.timing
    window.performance.timing.connectStart-window.performance.timing.responseEnd
```
3. 通过bash命令获取cpu使用率
```bash
while true; do adb shell top n 1|grep xueqiu| awk '{print $3}';  done
```

