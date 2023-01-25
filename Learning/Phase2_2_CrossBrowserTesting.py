from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.firefox import GeckoDriverManager

browser_name = "chrome"
if browser_name == "chrome":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com/")
    # driver.maximize_window()
    time.sleep(3)
    driver.close()

elif browser_name == "firefox":
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.google.com/")
    # driver.maximize_window()
    time.sleep(3)
    driver.close()

elif browser_name == "safari"
    driver = webdriver.safari()