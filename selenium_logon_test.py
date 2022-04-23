from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
  

driver = webdriver.Chrome()
driver.get('http://localhost:8069/web/login')

driver.implicitly_wait(0.5)

time.sleep(2)

username = driver.find_element(By.NAME, 'login')
password = driver.find_element(By.NAME, 'password')

username.send_keys("admin")
password.send_keys("admin")
time.sleep(2)
password.send_keys(Keys.RETURN)


time.sleep(5)
driver.quit()
print("Done")
