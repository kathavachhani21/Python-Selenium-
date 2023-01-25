from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/")
driver.maximize_window()
print("Browser launched successfully with the given URL")
print(driver.title)
driver.find_element(By.NAME, 'q').send_keys("Amazon")
driver.implicitly_wait(5)
options = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(len(options))

for ele in options:
    print(ele.text)
    if  ele.text == 'amazon india':
        ele.click()
        break

time.sleep(3)
driver.close()