from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.google.com")
print(driver.title)

driver.find_element(By.NAME, 'q').send_keys("Python")
time.sleep(4)
options = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li')
print(len(options))

for ele in options:
    print(ele.text)
    if ele.text == "python":
        ele.click()
        break

time.sleep(5)
driver.quit()
