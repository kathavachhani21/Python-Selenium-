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
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
driver.maximize_window()

# open a new tab
driver.execute_script("window.open('https://www.google.com/');")
time.sleep(3)
# driver.find_element(By.XPATH, "//input[@title='Search']").send_keys("flower jpg images")
# time.sleep(3)
pyautogui.press('enter')
# switch different tab
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
# move to element
driver.execute_script("window.open('https://ax-dev.ax-ss.com/users/login');")
time.sleep(3)
username = driver.find_element(By.XPATH, "//input[@id='id_email']")
cont_btn = driver.find_element(By.XPATH, "//button[@id='Continue_BTN']")
password = driver.find_element(By.XPATH, "//input[@id='id_password']")
check = driver.find_element(By.XPATH, "//input[@id='policy_check']")
login_btn = driver.find_element(By.XPATH, "//button[@id='Login_BTN']")

action = ActionChains(driver)
action.send_keys(username, "katha.v@simformsolutions.com").perform()
action.click(cont_btn).perform()
action.send_keys(password, "1234567890katha").perform()
action.click(check).perform()
action.click(login_btn).perform()
time.sleep(3)
driver.close()