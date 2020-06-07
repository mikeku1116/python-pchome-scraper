from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://shopping.pchome.com.tw/")  # 前往PChome網站

browser.implicitly_wait(20)  # 隱含等待20秒

search_input = browser.find_element_by_id("keyword")  # 查詢文字框
search_input.send_keys("藍芽耳機")  # 輸入文字

search_button = browser.find_element_by_id("doSearch")  # 找商品按鈕
search_button.click()  # 點擊

titles = browser.find_elements_by_class_name("prod_name")  # 取得商品標題
for title in titles:
    print(title.text)
