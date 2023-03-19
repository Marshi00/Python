from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
service = Service("chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://secure-retreat-92358.herokuapp.com")
first_name = driver.find_element(by="name", value="fName")
first_name.send_keys("M")
last_name = driver.find_element(by="name", value="lName")
last_name.send_keys("A")
email_name = driver.find_element(by="name", value="email")
email_name.send_keys("Hakonamatat@gmail.com")
signUp_button = driver.find_element(by="css selector", value="form button")
signUp_button.send_keys(Keys.ENTER)