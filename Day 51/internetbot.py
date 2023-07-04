import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
email = os.environ.get("tuser")
password = os.environ.get('tpass')
class InternetSpeedBot:
    def __init__(self, down, up):
        self.driver = webdriver.Chrome()
        self.down = down
        self.up = up

    def get_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        time.sleep(80)
        self.tested_down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.tested_up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet(self, user, password):
        self.driver.get('https://www.twitter.com/')
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label').send_keys(user)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label').send_keys(Keys.ENTER)
        time.sleep(2)
        passw = self.driver.find_element(By.XPATH, '//input[@type="password" and @name="password"]')
        passw.clear()
        passw.send_keys(password)
        passw.send_keys(Keys.ENTER)
        time.sleep(2)
        input('Confirm there is no captcha, or complete captcha(type any key): ')

z = InternetSpeedBot(150,60)
z.tweet(str(email), str(password))