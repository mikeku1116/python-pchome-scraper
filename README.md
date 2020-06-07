# python-pchome-scraper #

## 專案介紹 ##

本專案以PChome網站為例，來示範開發Python動態網頁爬蟲時，常用的3種等待機制，包含Python內建time模組的sleep()方法，以及Selenium套件的Implicit Wait(隱含等待)與Explicit Wait(明確等待)方法，其中也包含使用Explicit Wait(明確等待)時，需指定的Expected Conditions(預期條件)範例程式，如下：

* title_is
* title_contains
* presence_of_element_located
* presence_of_all_elements_located
* invisibility_of_element_located
* visibility_of_element_located
* visibility_of
* text_to_be_present_in_element_value
* element_to_be_clickable
* alert_is_present

可以搭配[[Python爬蟲教學]3個建構Python動態網頁爬蟲重要的等待機制](https://www.learncodewithmike.com/2020/06/python-selenium-waits.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境，就可以執行各個範例程式：

`$ pipenv shell`

