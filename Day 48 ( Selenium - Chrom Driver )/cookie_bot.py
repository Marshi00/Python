from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

CLICKING_LOOP_SEC = 5
END_TIME_SEC = 300

service = Service("chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)
cookie = driver.find_element(by="css selector", value="div #cookie")





# cookie.click()

game_stop_end_time = time.time() + END_TIME_SEC

while game_stop_end_time > time.time():
    highest_cost = 0
    clicking_end_time = time.time() + CLICKING_LOOP_SEC
    while time.time() < clicking_end_time:
        cookie.click()
    money = driver.find_element(by="css selector", value="div #money").text
    if "," in money:
        money = money.replace(",", "")
    money = int(money)
    store = driver.find_elements(by="css selector", value="#store b")
    for item in store:
        try:
            element_text = item.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                print(cost)
                if money > cost > highest_cost:
                    highest_cost = cost
        except:
            print("count2")
    for item in store:
        try:
            element_text = item.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                print(cost)
                if highest_cost == cost:
                    item.click()
        except:
            pass
    print(f"moeny:{money} , hcost {highest_cost}")
click_target = driver.find_elements(by="css selector", value="div  #store div b")
