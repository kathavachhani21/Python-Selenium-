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
campaign = driver.find_element(By.CSS_SELECTOR,
                               "div[class='d-flex align-items-center'] i[class='dripicons-chevron-right']")
campaign.click()
tactic = driver.find_element(By.XPATH, '//*[@id="reporting_ad_groupiipsgmn"]/tbody/tr/td[1]/div/a')
tactic.click()

targeting = driver.find_element(By.XPATH, '//*[@id="AdGrp_TargetOptUpdate"]/span[2]')
targeting.click()

add_button = driver.find_element(By.XPATH, '//*[@id="AddTarget"]')
search = driver.find_element(By.XPATH, '//*[@id="AddRailTacticDetailsModal"]/div/div/div[2]/div/div[1]/div/div/input')

##------------------------------------------------Frequency-----------------------------------------------------------

add_button.click()
search.send_keys("Frequency")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="AddRailTacticDetailsModal"]/div/div/div[2]/ul[2]/li/div/ul/li[3]/a/span').click()
time.sleep(3)
#close targeting modal
driver.find_element(By.CSS_SELECTOR, "#AddRailTacticDetailsModal > div > div > div.modal-footer > button").click()
driver.implicitly_wait(10)

# check mark
driver.find_element(By.CSS_SELECTOR, "#MaxFrequencyCap").click()
driver.implicitly_wait(10)
# enter data
driver.find_element(By.CSS_SELECTOR, "#maximumAdsId").click()
driver.find_element(By.CSS_SELECTOR, "#maximumAdsId").send_keys(2)
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, "#maximumAdsPerId").click()
driver.find_element(By.CSS_SELECTOR, "#maximumAdsPerId").send_keys(1)
driver.implicitly_wait(10)
#save
driver.find_element(By.CSS_SELECTOR, "#AdG_Targeting > div > div.selected_trail.trail_6 > div > div.row.justify-content-end > div:nth-child(2)").click()
time.sleep(5)
driver.quit()
