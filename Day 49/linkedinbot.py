from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/jobs/?focusToMoreMenuTrigger=true&showJobAlertsModal=false&showJobSeekerSafetyTipsModal=false')
time.sleep(10)