from selenium import webdriver
from selenium.webdriver.common.by import By

c_d_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://www.python.org/')
#title = driver.title
#price = driver.find_element(By.CLASS_NAME, 'a-price-whole')
#print (price.get_attrivute('attribute of element'))


#How to find like I usually do

#search = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')


elements = driver.find_elements(By.CSS_SELECTOR, "#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li")
#print(elements)

list = {element.find_element(By.TAG_NAME, 'a').text: element.find_element(By.TAG_NAME, 'time').text for element in elements}
new_list = {index : {event: date} for index, (event, date) in enumerate(list.items())}
print(new_list)