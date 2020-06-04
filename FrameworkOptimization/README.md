## UI自动化测试框架2 作业
1. 实现测试步骤的数据驱动 pages - steps
2. 实现测试数据的数据驱动 common - processingdata.py get_data
3. 基于scrcpy实现录像功能
4. 集成log日志 screenshot截图功能
5. 使用allure生成测试报告
   ```
   pytest test_allure.py --alluredir=./result
   allure serve ./result/
   ```