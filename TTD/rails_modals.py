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
print("login succeed")
check_mark = driver.find_element(By.CSS_SELECTOR, "#policy_check")
check_mark.click()
login = driver.find_element(By.CSS_SELECTOR, "#Login_BTN")
login.click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "#AdvertiserName").send_keys("chrome 1")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="all-advertisers-list1"]/div[1]/div/div/div[1]/div/div[1]/a').click()
time.sleep(5)

handles = driver.window_handles
driver.switch_to.window(handles[1])

driver.find_element(By.XPATH, '//*[@id="all-1"]/div[1]/div/a').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="CampSearchName"]').send_keys("auto")
campaign = driver.find_element(By.CSS_SELECTOR, "div[class='d-flex align-items-center'] i[class='dripicons-chevron-right']")
campaign.click()
tactic = driver.find_element(By.XPATH, '//*[@id="reporting_ad_groupiipsgmn"]/tbody/tr/td[1]/div/a')
tactic.click()

targeting = driver.find_element(By.XPATH, '//*[@id="AdGrp_TargetOptUpdate"]/span[2]')
targeting.click()

add_button = driver.find_element(By.XPATH, '//*[@id="AddTarget"]')
search = driver.find_element(By.XPATH,'//*[@id="AddRailTacticDetailsModal"]/div/div/div[2]/div/div[1]/div/div/input')

##------------------------------------------------Creatives-------------------------------------------------------------

add_button.click()
search.send_keys("Creatives")
driver.implicitly_wait(10)
## click on creative
driver.find_element(By.XPATH, '//*[@id="AddRailTacticDetailsModal"]/div/div/div[2]/ul[1]/li/div/ul/li/a/span').click()
driver.implicitly_wait(10)
## click on browse button
driver.find_element(By.XPATH, '//*[@id="UpdateCreativesofAdgroup"]/div/div[1]/div[2]/a').click()
## search creative name
driver.find_element(By.XPATH, '//*[@id="SearchCreative"]').send_keys("hosted display 1 nov")
driver.implicitly_wait(10)
## check mark on creative
driver.find_element(By.XPATH, '//*[@id="CreativeModalTable"]/tbody/tr/td[1]/div/input').click()
## save
driver.find_element(By.XPATH, '//*[@id="CreateTacticSave"]').click()
driver.implicitly_wait(10)
## save: add rail
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.find_element(By.XPATH, '//*[@id="UpdateCreativesofAdgroupbtn"]').click()
driver.implicitly_wait(10)
## message
##toast_message = driver.find_element(By.CLASS_NAME, "toast-message").text
##print(toast_message)
"""
##------------------------------------------------Time of day-----------------------------------------------------------

add_button.click()
search.send_keys("Time of Day")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="AddRailTacticDetailsModal"]/div/div/div[2]/ul[2]/li/div/ul/li[2]/a/span').click()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, '#AddRailTacticDetailsModal > div > div > div.modal-footer > button').click()
## Open the modal
driver.find_element(By.XPATH, "//div[@id='AddTimeoftheDayBtn']//button[@id='AddPrivateContract']").click()
driver.find_element(By.CSS_SELECTOR, '#AddTimeoftheDayBtn > div > a').click()
driver.implicitly_wait(10)
## add rail name
driver.find_element(By.XPATH, '//*[@id="CreateTimeOfTheDay"]/div/div[1]/div/input').send_keys("Time Rail")
## select check mark
driver.find_element(By.XPATH, "//label[@for='6']").click()
driver.find_element(By.XPATH, "//label[@for='13']").click()
## save
driver.find_element(By.XPATH, '//*[@id="CreateTimeOftheDay"]').click()
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//button[@id='AddTimeofTheDayRails']").click()
driver.implicitly_wait(10)

"""
## pyhton
driver.quit()