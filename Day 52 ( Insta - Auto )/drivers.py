import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

INSTA_USERNAME = ""
INSTA_PASSWORD = ""


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(service=Service(executable_path=path))

    def login(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(3)
        print(1)

        email_input = self.driver.find_element(by="name", value='username')
        email_input.send_keys(INSTA_USERNAME)
        password_input = self.driver.find_element(by="name", value='password')
        password_input.send_keys(INSTA_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(3)
        print(2)
        not_now_button = self.driver.find_element(by="xpath", value='//*[@id="react-root"]/section/main/div/div/div/div'
                                                                    '/button')
        not_now_button.send_keys(Keys.ENTER)
        print(3)
        time.sleep(3)
        not_now_button2 = self.driver.find_element(by="xpath",
                                                   value='/html/body/div[1]/div/div/div/div[2]/div/div/div['
                                                         '1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
        not_now_button2.send_keys(Keys.ENTER)

    def find_followers(self, url, taget_account):
        self.driver.maximize_window()
        self.driver.get(f"{url}{taget_account}")
        time.sleep(2)
        followers = self.driver.find_element(by="xpath", value='//*[@id="react-root"]/section/main/div/header/section'
                                                               '/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element(by="xpath", value='/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does. The method
            # can accept the script as well as a HTML element. The modal in this case, becomes the arguments[0] in
            # the script. Then we're using Javascript to say: "scroll the top of the modal (popup) element by the
            # height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(by="css selector", value="li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by="xpath", value='/html/body/div[5]/div/div/div/div['
                                                                           '3]/button[2]')
                cancel_button.click()
            finally:
                time.sleep(1)
