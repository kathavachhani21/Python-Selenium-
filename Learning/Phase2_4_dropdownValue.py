from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(10)
product = driver.find_element(By.XPATH, "//select[@id='first']")
selectoption = Select(product)
selectoption.select_by_value('Google')
time.sleep(3)
selectoption.select_by_index(2)
time.sleep(3)
driver.close()
