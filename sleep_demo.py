from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://shopping.pchome.com.tw/")  # 前往PChome網站

time.sleep(20)  # 強制等待20秒

search_input = browser.find_element_by_id("keyword")  # 查詢文字框
search_input.send_keys("藍芽耳機")  # 輸入文字
