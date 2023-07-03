from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
username = os.environ.get('LDUser')
password = os.environ.get('LDpword')
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/jobs/?focusToMoreMenuTrigger=true&showJobAlertsModal=false&showJobSeekerSafetyTipsModal=false')
time.sleep(1)
user = driver.find_element(By.ID, 'session_key')
user.send_keys(username)
passw = driver.find_element(By.ID, 'session_password')
passw.send_keys(password)
signin = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button')
signin.click()
time.sleep(2)
firstsearch = driver.find_element(By.XPATH, '//*[@id="jobs-search-box-keyword-id-ember23"]')
firstsearch.send_keys('Software Development')
time.sleep(1)
firstsearch.send_keys(Keys.ENTER)
time.sleep(5)
explevel = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/div/div/button')
explevel.click()
time.sleep(1)
intern = driver.find_element(By.XPATH, '//label[@for="advanced-filter-experience-1"]')
intern.click()
time.sleep(1)
toggle_switch = driver.find_element(By.XPATH, '//input[@id="adToggle_ember606"]')
toggle_switch.click()

time.sleep(100)