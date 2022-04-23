from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Patient creation test 

driver = webdriver.Chrome()
#hospital module id #270
driver.get('http://localhost:8069/web/login#menu_id=270')

driver.implicitly_wait(0.5)

time.sleep(2)

#find element by name
username = driver.find_element(By.NAME, 'login')
password = driver.find_element(By.NAME, 'password')

username.send_keys('admin')
password.send_keys('admin')
time.sleep(2)
password.send_keys(Keys.RETURN)

#need to make sure everything is loaded, otherwise will get element not found error
driver.implicitly_wait(2) 

#go to create patient page
#find element using CSS_SELECTOR
button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.o_list_button_add')
button.click()

driver.implicitly_wait(2)  
time.sleep(2)

#find element using XPATH
name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[4]/table[1]/tbody/tr[1]/td[2]/input')
name.send_keys('test patient4')
time.sleep(2)

age = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[4]/table[1]/tbody/tr[3]/td[2]/input')
age.send_keys(35)

time.sleep(2)

dropdown = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[4]/table[2]/tbody/tr[1]/td[2]/select'))
dropdown.select_by_index(2)

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.o_form_button_save').click()


time.sleep(5)
driver.quit()
print('Successfully created a patient.')
print('Test Completed')
