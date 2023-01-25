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
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
time.sleep(3)


driver.find_element(By.XPATH, "//button[@id='alertButton']").click()
alert = driver.switch_to.alert
alert.accept()
time.sleep(3)

driver.find_element(By.XPATH, "//button[@id='confirmButton']").click()
alert = driver.switch_to.alert
alert.dismiss()
time.sleep(3)

driver.find_element(By.XPATH, "//button[@id='confirmButton']").click()
driver.switch_to.alert.send_keys("Katha")
driver.switch_to.alert.accept()
time.sleep(3)

driver.close()
