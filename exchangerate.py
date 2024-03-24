# 使用sys.argv传入日期和货币代码作为参数。
import sys
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# 读取命令行参数中的日期和货币代码
date = sys.argv[1]
# 从json文件中读取货币代码对应的汇率基础信息
data = json.load(open('data.json', 'r', encoding='utf-8'))
hb = data[sys.argv[2]]
# 定义要访问的银行网站汇率查询URL
url = 'https://srh.bankofchina.com/search/whpj/search_cn.jsp'
# 设置Chrome浏览器的选项
options = webdriver.ChromeOptions()
service = Service(r'chromedriver.exe')
options.binary_location = r'Google\\Chrome\\Application\\chrome.exe'
# 创建Chrome浏览器实例
driver = webdriver.Chrome(options=options, service=service)
# 访问银行网站
driver.get(url)
# 格式化日期为yyyy-mm-dd格式，以适应网站的日期输入字段
date = date[:4] + '-' + date[4:6] + '-' + date[6:8]
# 在网页中输入查询日期
driver.find_element(By.XPATH, '//*[@id="historysearchform"]/div/table/tbody/tr/td[4]/div/input').send_keys(date)
# 从下拉列表中选择货币代码
s1 = Select(driver.find_element(By.XPATH, '//*[@id="pjname"]'))
s1.select_by_value(hb)
# 等待页面加载完成
time.sleep(1)
# 点击搜索按钮
driver.find_element(By.XPATH, '//*[@id="historysearchform"]/div/table/tbody/tr/td[7]/input').click()
# 获取查询结果并打印
data = driver.find_element(By.XPATH, '/html/body/div/div[4]/table//tr[2]/td[4]').text
print(data)
# 将查询结果写入到结果文件中
open('result.txt', 'w', encoding='utf-8').write(data)
