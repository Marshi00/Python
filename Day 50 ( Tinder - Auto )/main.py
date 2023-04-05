# For auto login
"""
https://stackoverflow.com/questions/31062789/how-to-load-default-profile-in-chrome-using-python-selenium-webdriver

Manually login to tinder using google/Facebook.
Launch google chrome using your default chrome profile. (You can read more about this here.)
This will skip your login.
Here's my code for it.

from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=Path to your chrome profile")
chrome_driver_path = "Path to your chrome driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)

driver.get("https://tinder.com/app/recs")
driver.maximize_window()
time.sleep(10)
time.sleep(10)
time.sleep(10)
reject_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')

start_time = time.time()
end_time = start_time + 60

while time.time() < end_time:
reject_button.click()
time.sleep(5)

driver.quit()`

"""



import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
ACCOUNT_EMAIL = "a"
ACCOUNT_PASSWORD = ""
MAX_ALLOW_LIKE = 100
service = Service("chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://tinder.com/"
driver.get(URL)
time.sleep(3)
log_in_button = driver.find_element(by="xpath", value="//*[@id='u-1650273590']/div/div[1]/div/main/div["
                                                      "1]/div/div/div/div/header/div/div[2]/div[2]/a")
log_in_button.click()
time.sleep(3)
fb_log_in_button = driver.find_element(by="xpath", value="//*[@id='u916312630']/div/div/div[1]/div/div/div["
                                                         "3]/span/div[2]/button")
fb_log_in_button.click()

# Switch to Facebook login window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(5)
# Login and hit enter
email_input = driver.find_element(by="name", value="email")
email_input.send_keys(ACCOUNT_EMAIL)
password_input = driver.find_element(by="name", value="pass")
password_input.send_keys(ACCOUNT_PASSWORD)
login_button = driver.find_element(by="name", value="login")
login_button.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)
# Allow location
allow_location_button = driver.find_element(by="xpath", value='//*[@id="u916312630"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
time.sleep(2)
# Disallow notifications
notifications_button = driver.find_element(by="xpath", value='/html/body/div[2]/div/div/div/div/div[3]/button[1]')
notifications_button.click()
time.sleep(2)
# Allow cookies
cookies = driver.find_element(by="xpath", value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()
time.sleep(2)
# Like click !
like_count = 1
match_count = 0
for like in range(MAX_ALLOW_LIKE + 1):
    time.sleep(3)
    try:
        print(f"first like click Try : NUM --> {like}")
        body = driver.find_element(by="css selector", value='body')
        body.send_keys(Keys.RIGHT)
        """
        changes to this after first click - fix code
        /html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button
        
        like_button = driver.find_element(by="xpath", value='/html/body/div[1]/div/div[1]/div/main/div['
                                                            '1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()
        """
        print(f"first like click passed : NUM --> {like}")
        like_count += 1
    except NoSuchElementException:
        try:
            print(f"second like click try / exit match page : NUM --> {like}")
            match_popup = driver.find_element(by="css selector", value=".itsAMatch a")
            match_popup.click()
            time.sleep(3)
            print(f"second like click try / exit match page  pass : NUM --> {like}")
            body = driver.find_element(by="css selector", value='body')
            body.send_keys(Keys.RIGHT)
            """
            like_button = driver.find_element(by="xpath", value='/html/body/div[1]/div/div[1]/div/main/div['
                                                                '1]/div/div/div[1]/div[1]/div/div[4]/div/div['
                                                                '4]/button')

            like_button.click()
            """
            print(f"second like click try pass : NUM --> {like}")
            like_count += 1
            match_count += 1
        except:
            print(f"Something is wrong, out of likes ? {like}")

print(f"like count : {like_count}, match count {match_count}")

