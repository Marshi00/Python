from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
# driver.get("https://www.amazon.com/ASUS-GeForce-Processor-Keyboard-G733CX-XS97/dp/B09YN75CBF/ref=sr_1_9?qid=1660148832&refinements=p_n_size_browse-bin%3A7817234011&rnid=2242797011&s=computers-intl-ship&sr=1-9")
# price = driver.find_element(by="class name", value="a-price-whole")
# print(price.text)
driver.get("https://www.python.org/")
"""
search_bar = driver.find_element(by="name", value="q")
print(search_bar.get_attribute("placeholder"))
logo = driver.find_element(by="class name", value="python-logo")
print(logo.size)
docs_link = driver.find_element(by="css selector", value=".documentation-widget a")
print(docs_link.text)
bug_link = driver.find_element(by="xpath", value="//*[@id='site-map']/div[2]/div/ul/li[3]/a")
print(bug_link.text)
"""

event_links = driver.find_elements(by="css selector", value=".event-widget ul li a")
event_times = driver.find_elements(by="css selector", value=".event-widget ul li time")
links = [link.text for link in event_links]
times = [time.text for time in event_times]
time_link = {time.text: link.text for time, link in zip(event_links, event_times)}
# type 2
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_links[n].text,
    }
# print(time_link)
# print(events)
# *********************************************** TYPE 3 *******************************
my_dict = {i: j for i, j in zip(range(len(event_times)), [{"time": links.text, "name": times.text} for links, times in zip(event_links, event_times)])}
print(my_dict)
# driver.close()
driver.quit()
