import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
username = 'Zophous'
password = os.environ.get('inpass')
class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(Keys.ENTER)
        input('Confirm no Captcha')
        #Flagged as bot here, will return project once I get a proxy

        pass
    def find_followers(self):
        pass
    def follow(self):
        pass

z = InstaFollower()
z.login()