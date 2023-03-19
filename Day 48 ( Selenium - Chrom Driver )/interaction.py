from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
service = Service("chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(by="css selector", value="div #articlecount a")
print(article_count.text)
# article_count.click()
all_portals = driver.find_element(by="link text", value="View history")
# all_portals.click()
search = driver.find_element(by="name", value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
# driver.quit()