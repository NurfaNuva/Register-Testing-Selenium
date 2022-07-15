import time
from selenium import webdriver

# use your own path for chromedriver
driver = webdriver.Chrome('C:\\Development\\soft_test\\chromedriver.exe')

# link address for register pages
driver.get('https://ukmads.lepak.xyz/register')

# insert details based on element id
driver.find_element_by_id("name").send_keys("rtc450gmail.com")
driver.find_element_by_id("email").send_keys("rtc45@gmail.com")
driver.find_element_by_id("password").send_keys("Tsmbest3!")
driver.find_element_by_id("password-confirm").send_keys("Tsmbest3!")

# check whether successfully register or not
try:
    driver.find_element_by_id("user-register").click()
    # give time for system to respond
    time.sleep(3)
    if driver.find_elements_by_class_name("alert-success"):
        print("Successful")
    else:
        print("Failed")
except:
    pass

time.sleep(5)
driver.quit()