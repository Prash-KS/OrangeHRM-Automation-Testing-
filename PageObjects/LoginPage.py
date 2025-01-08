from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class loginpage():
    textbox_username_id = (By.XPATH, "//input[@placeholder='Username']")
    textbox_password_id = (By.XPATH, "//input[@placeholder='Password']")
    btn_login_id = (By.XPATH, "//button[normalize-space()='Login']")
    link_logout = "https://opensource-demo.orangehrmlive.com/index.php/auth/logout"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def setusername(self, username):
        self.wait.until(EC.presence_of_element_located(self.textbox_username_id))
        self.driver.find_element(*self.textbox_username_id).clear()
        self.driver.find_element(*self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.wait.until(EC.presence_of_element_located(self.textbox_password_id))
        self.driver.find_element(*self.textbox_password_id).clear()
        self.driver.find_element(*self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.wait.until(EC.presence_of_element_located(self.btn_login_id)).click()

