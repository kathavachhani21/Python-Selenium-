from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.maximize_window()
print(driver.title)
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='justAnInputBox']").click()
time.sleep(3)
drop_list = driver.find_element(By.CSS_SELECTOR, 'span.comboTreeItemTitle')

for ele in drop_list:
    print(ele.text)
