from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://shopping.pchome.com.tw/")  # 前往PChome網站

# 明確等待
locator = (By.ID, "keyword")  # 定位器
search_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located(locator),
    "找不到指定的元素"
)

search_input.send_keys("藍芽耳機")  # 輸入文字
