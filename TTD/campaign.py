from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://ax-dev.ax-ss.com/")
driver.maximize_window()
print(driver.title)

email = driver.find_element(By.CSS_SELECTOR, "#id_email")
email.send_keys("katha2@yopmail.com")
driver.find_element(By.CSS_SELECTOR, "#Continue_BTN").click()
password = driver.find_element(By.CSS_SELECTOR, "#id_password")
password.send_keys("asdfghjkl;'")
check_mark = driver.find_element(By.CSS_SELECTOR, "#policy_check")
check_mark.click()
login = driver.find_element(By.CSS_SELECTOR, "#Login_BTN")
login.click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "#AdvertiserName").send_keys("chrome")
driver.implicitly_wait(10)
campaign = driver.find_element(By.XPATH, "//div[9]//div[1]//div[1]//div[1]//div[1]//a[1]//div[1]")
driver.execute_script("arguments[0].scrollIntoView();", campaign)
time.sleep(3)

driver.quit()
