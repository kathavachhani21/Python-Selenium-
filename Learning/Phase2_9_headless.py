from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from webdriver_manager.firefox import GeckoDriverManager

browser_name = "chrome"
if browser_name == "chrome":
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
elif browser_name == "firefox":
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

driver.implicitly_wait(10)
driver.get("https://demoqa.com/")
driver.maximize_window()
print(driver.title)
time.sleep(3)
driver.close()
