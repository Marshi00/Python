import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

PROMISED_DOWN = 150
PROMISED_UP = 10
ACCOUNT_EMAIL = "arshiyan.mohammad48@gmail.com"
ACCOUNT_PASSWORD = "UKetTZd2th3_28i"
ACCOUNT_USERNAME = "@MoAr66129964"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.up = 0
        self.down = 0
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        time.sleep(3)

    def get_internet_speed(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
        start_test_button = self.driver.find_element(by="css selector", value=".start-button a")
        start_test_button.click()
        time.sleep(45)
        while True:
            try:

                self.down = self.driver.find_element(by="xpath", value='//*[@id="container"]/div/div['
                                                                       '3]/div/div/div/div[2]/div[ '
                                                                       '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                                       '1]/div/div[2]/span').text
                self.up = self.driver.find_element(by="xpath", value='//*[@id="container"]/div/div[3]/div/div/div/div['
                                                                     '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                                                                     '1]/div[2]/div/div[2]/span').text
                print(f"download speed is : {self.down}, upload speed is : {self.up}")
            except:
                time.sleep(5)
            else:
                break

    def tweet_at_provider(self):
        self.driver.maximize_window()
        self.driver.get("https://twitter.com/login")

        print(1)
        time.sleep(3)
        email_input = self.driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                 '2]/div[2]/div/div/div[2]/div[2]/div/div/div/div['
                                                                 '5]/label/div/div[2]/div/input')

        email_input.send_keys(ACCOUNT_EMAIL)
        print(1.5)
        next_button = self.driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                 '2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        time.sleep(2)
        print(2)
        user_name_input = self.driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                     '2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                                     '2]/label/div/div[2]/div/input')
        user_name_input.send_keys(ACCOUNT_USERNAME)
        time.sleep(1)
        print(3)
        next_button = self.driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                 '2]/div[2]/div/div/div[2]/div[2]/div['
                                                                 '2]/div/div/div/div')
        next_button.click()
        time.sleep(2)
        print(4)
        pass_input = self.driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                '2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                                '3]/div/label/div/div[2]/div[1]/input')
        pass_input.send_keys(ACCOUNT_PASSWORD)
        print(4.5)
        log_in_button = self.driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                   '2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div['
                                                                   '1]/div/div/div')
        log_in_button.click()

        time.sleep(5)
        print("log in pass")

        tweet_button = self.driver.find_element(by="xpath", value='//*[@id="react-root"]/div/div/div['
                                                                  '2]/header/div/div/div/div[1]/div[3]/a/div')
        tweet_button.click()
        print(6)

        tweet_text = self.driver.find_element(by="xpath", value='//*[@id="layers"]/div[2]/div/div/div/div/div/div['
                                                                '2]/div[2]/div/div/div/div[3]/div/div['
                                                                '1]/div/div/div/div/div[2]/div['
                                                                '1]/div/div/div/div/div/div/div/div/div/div/label'
                                                                '/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        message = f"download speed is : {self.down}, upload speed is : {self.up}. Twitter can not catch my bot :))"
        print(7)
        for letter in message:
            tweet_text.send_keys(letter)
            time.sleep(0.3)
        print(8)
        send_tweet_button = self.driver.find_element(by="xpath", value='//*[@id="layers"]/div['
                                                                       '2]/div/div/div/div/div/div[2]/div['
                                                                       '2]/div/div/div/div[3]/div/div['
                                                                       '1]/div/div/div/div/div[2]/div[3]/div/div/div['
                                                                       '2]/div[4]')
        #send_tweet_button.click()