from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

search = input("검색 : ")

chrome_options =webdriver.ChromeOptions()
driver = webdriver.Chrome(service = Service(
    ChromeDriverManager().install()),
    options = chrome_options)

url = "https://www.auction.co.kr/"
driver.get(url)
driver.implicitly_wait(3)


e = driver.find_element(By.ID, 'txtKeyword')
e.clear()
e.send_keys(search)
e.send_keys(Keys.ENTER)
driver.implicitly_wait(3)

webpage = driver.page_source

count = driver.find_elements(By.CLASS_NAME, "itemcard")
for i in count:
    product = i.find_element(By.CLASS_NAME, "text--title")
    saleprice = i.find_element(By.CLASS_NAME, "text__price-seller")
    print("제품명 :", product.text, "\n", "할인 가격 :",saleprice.text)
    print()
