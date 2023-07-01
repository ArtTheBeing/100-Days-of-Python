from selenium import webdriver
from selenium.webdriver.common.by import By
import time
c_d_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome()
driver.get('https://orteil.dashnet.org/cookieclicker/')
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]').click()
time.sleep(5)


timeout = 60 * 5   # [seconds]

timeout_start = time.time()
start = time.time()
while time.time() < timeout_start + timeout:
    cookie = driver.find_element(By.ID, 'bigCookie')
    cookie.click()
    cookie.click()
    time.sleep(.1)
    if time.time() > start+5:
        unlocked = driver.find_elements(By.CSS_SELECTOR, '#products div.content span.price')
        #Clean Loop
        for item in unlocked:
            if item.text == "":
                unlocked.remove(item)
        #Generate Valid Dictionary
        start += 5
        prices = {}
        for i in range(len(unlocked)):
            if unlocked[i].text == "":
                pass
            else:
                prices[(int(unlocked[i].text.replace(',', '')))] = driver.find_element(By.ID, f'product{i}')
        #Get Cookie Amount
        #List of Prices to Buy
        reversed_dict = {key: value for key, value in reversed(prices.items())}
        for item in reversed_dict:
            amount = int(driver.find_element(By.XPATH, '//*[@id="cookies"]').text.split(" ")[0])
            if amount > item:
                reversed_dict[item].click()
                break
        

print(unlocked)

#products > div:nth-child(2) > div.content > span.price