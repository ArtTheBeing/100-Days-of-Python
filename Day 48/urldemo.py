from selenium import webdriver
from selenium.webdriver.common.by import By
import time
c_d_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://secure-retreat-92358.herokuapp.com/')

fname = driver.find_element(By.NAME, 'fName')
lname = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')

fname.send_keys('Daniel')
lname.send_keys('McCord')
email.send_keys('beingtheartist@gmail.com')
time.sleep(5)
driver.find_element(By.CLASS_NAME, 'btn-block').click()
time.sleep(5)
driver.quit()