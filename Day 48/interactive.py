from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

#article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# article_count = driver.find_element(By.LINK_TEXT, 'English')
# article_count.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys("Python")
time.sleep(3)
search.send_keys(Keys.ENTER)

time.sleep(10)
driver.quit()
