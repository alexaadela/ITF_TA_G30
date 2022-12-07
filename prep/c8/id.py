import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://signup.heroku.com/')
time.sleep((2))
driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
driver.find_element(By.ID, "first_name").send_keys(('Test'))
time.sleep((4))
driver.quit() # inchide tot browserul si toate tab-urile active
# driver.close() # inchide doar tab-ul curent