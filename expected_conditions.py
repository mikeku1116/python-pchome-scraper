from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ExpectedCondition:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://shopping.pchome.com.tw/")

    def title_is_demo(self):
        title = WebDriverWait(self.driver, 10).until(
            EC.title_is("PChome 線上購物")
        )
        print(title)  # True

    def title_contains_demo(self):
        title = WebDriverWait(self.driver, 10).until(
            EC.title_contains("PChome")
        )
        print(title)  # True

    def presence_of_element_located_demo(self):
        locator = (By.ID, "keyword")

        keyword = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        keyword.send_keys("藍芽耳機")

    def presence_of_all_elements_located_demo(self):
        locator = (By.LINK_TEXT, "24h購物")

        link_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator)
        )
        print(link_text)  # 符合定位條件的所有元素

    def invisibility_of_element_located_demo(self):
        locator = (By.ID, "hello")

        non_exist = WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator)
        )
        print(non_exist)  # True

    def visibility_of_element_located_demo(self):
        locator = (By.ID, "keyword")

        keyword = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        print(keyword)  # True

    def visibility_of_demo(self):
        element = self.driver.find_element_by_id("keyword")

        keyword = WebDriverWait(self.driver, 10).until(
            EC.visibility_of(element)
        )
        keyword.send_keys("藍芽耳機")

    def text_to_be_present_in_element_value_demo(self):
        locator = (By.ID, "doSearch")

        search = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_value(locator, "找商品")
        )
        print(search)  # True

    def element_to_be_clickable_demo(self):
        locator = (By.ID, "doSearch")

        search = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        print(search)  # True

    def alert_is_present_demo(self):
        alert = WebDriverWait(self.driver, 10).until(
            EC.alert_is_present(),
            "彈出視窗不存在"
        )
