import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ""
PHONE = ""
service = Service("chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3218872073&geoId=101174742&keywords=marketing%20specialist" \
      "&location=Canada&refresh=true "
driver.get(URL)
try:
    sign_in_link = driver.find_element(by="link text", value="Sign in")
    sign_in_link.click()
except:
    pass
finally:
    # Wait for the next page to load.
    time.sleep(5)
    email_input = driver.find_element(by="name", value="session_key")
    email_input.send_keys(ACCOUNT_EMAIL)
    password_input = driver.find_element(by="name", value="session_password")
    password_input.send_keys(ACCOUNT_PASSWORD)
    signIn_button = driver.find_element(by="css selector", value="form button")
    signIn_button.send_keys(Keys.ENTER)

try:
    jobs = driver.find_elements(by="css selector", value=".jobs-search-results-list ul li div .job-card-container")
    print("1")
    for job in jobs:
        try:
            job.click()
            print("2")
            time.sleep(3)
            easy_apply_button = driver.find_element(by="css selector",
                                                    value=".jobs-apply-button--top-card .jobs-apply-button")
            print("3")
            time.sleep(3)
            easy_apply_button.click()
            print("4")
            time.sleep(3)
            #phone = driver.find_element(by="name", value="fb-single-line-text__input")
            print(4.1)
            #if phone.text == "":
            #    phone.send_keys(PHONE)
            submit_button = driver.find_element(by="css selector", value="footer div button")
            print(5)
            # If the submit_button is a "Next" button, then this is a multi-step application, so skip.

            if submit_button.get_attribute("aria-label") == "continue to next step":
                print(6)
                close_button = driver.find_element(by="class", value="artdeco-modal__dismiss")

                close_button.click()
                print(7)
                time.sleep(2)

                discard_button = driver.find_element(by="name", value="artdeco-modal__confirm-dialog-btn")[1]

                discard_button.click()

                print("Complex application, skipped.")

                continue

            else:
                print("got it")


                # submit_button.click()

            # Once application completed, close the pop-up window.

            time.sleep(2)
            print(8)
            close_button = driver.find_element(by="name", value="artdeco-modal__dismiss")

            close_button.click()


        # If already applied to job or job is no longer accepting applications, then skip.

        except NoSuchElementException:

            print("No application button, skipped.")

            continue
except:
    print("failed to get job listing")
