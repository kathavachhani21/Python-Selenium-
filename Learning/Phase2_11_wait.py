# static wait -> time.sleep(5)
# dynamic wait -> 1. implicit wait 2. webdriver wait:- explicit wait: direct method is not available in selenium

# implicit wait: it's applicable for only elements like find element, find elements. it's not applicable for title, url, alerts. for that we have to use explicit wait.


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pyautogui

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(3)
driver.get_screenshot_as_file("screenshot1.png")

driver.close()
