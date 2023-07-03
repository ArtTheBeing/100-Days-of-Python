from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
import os
number = os.environ.get('phonenumber')
driver = webdriver.Chrome()
driver.get('https://tinder.com/')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="u490315748"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button').click()
userint = input('Input when done: ')
driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div[1]/div[1]/div/div[2]/div/div[2]/div/div[2]/input').send_keys(number)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div[1]/div[1]/div/div[3]/button').click()


#User Captcha
userint = input('Input when done: ')

#Autoswipe
while True:
    try:
        print("called")
        driver.find_element(By.XPATH, '//*[@id="u490315748"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button').click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            print('Other Error')
    time.sleep(2)