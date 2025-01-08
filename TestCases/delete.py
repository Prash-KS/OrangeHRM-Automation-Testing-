import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.implicitly_wait(30)
time.sleep(3)
driver.find_element(By.XPATH, "//input[@placeholder='username']").send_keys('Admin')
driver.find_element(By.XPATH, "(//input[@placeholder='password'])[1]").send_keys('admin123')
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='My Info']").click()
time.sleep(3)

element = driver.find_element(By.XPATH, "(//input)[5]")
element.send_keys(Keys.CONTROL + "a")
element.send_keys("uuu")
time.sleep(3)
