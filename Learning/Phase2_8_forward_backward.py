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
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='category-cards']//div[1]//div[1]//div[2]//*[name()='svg']").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
cookies = driver.get_cookies()
for cook in cookies:
    print(cook)
# print(driver.get_cookies())

driver.close()
