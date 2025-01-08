from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PersonalDetails():
    # Personal Details
    txt_first_name = (By.XPATH, "//input[@placeholder='First Name']")
    txt_middle_name = (By.XPATH, "//input[@placeholder='Middle Name']")
    txt_last_name = (By.XPATH, "//input[@placeholder='Last Name']")
    # txt_nick_name = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[1]")
    txt_employee_id = (By.XPATH, "(//input)[5]")
    txt_other_id = (By.XPATH, "(//input)[6]")
    txt_driver_licence_number = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")
    txt_licence_expire_date = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
    # txt_SSN_number = (By.XPATH, "(//input)[10]")
    # txt_SIN_number = (By.XPATH, "(//input)[11]")
    drp_nationality = (By.XPATH, "(//div)[84]")
    select_nationality = (By.XPATH, "//span[normalize-space()='Indian']")
    drp_marital_status = (By.XPATH, "(//div)[92]")
    select_marital_status = (By.XPATH, "//span[normalize-space()='Single']")
    txt_dob = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")
    rd_male_gender = (By.XPATH, "//label[normalize-space()='Male']")
    rd_female_gender = (By.XPATH, "//label[normalize-space()='Female']")
    # txt_military_service = (By.XPATH, "(//input)[15]")
    # cb_smoker = (By.XPATH, "//label[normalize-space()='Yes']")
    btn_save_personal_details = (By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[1]")

    # Custom Fields
    drp_blood_type = (By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[3]")
    select_blood_type = (By.XPATH, "//span[normalize-space()='O+']")
    txt_test_field = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[6]")
    btn_save_custom_fields = (By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[2]")

    # Attachment
    btn_add_attachments = (By.XPATH, "//button[normalize-space()='Add']")
    btn_upload_file = (By.XPATH, "//input[@type='file']")
    cb_select_all_attachments = (By.XPATH, "//div[@role='columnheader']//label")
    btn_delete_attachments = (By.XPATH, "//button[normalize-space()='Delete Selected']")
    txt_attachment_comment = (By.XPATH, "//textarea[@placeholder='Type comment here']")
    btn_cancel_upload = (By.XPATH, "//button[normalize-space()='Cancel']")
    btn_save_attachments = (By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[3]")

    # Confirm msg
    msg_confirm = (By.XPATH, "(//div[@id='oxd-toaster_1'])[1]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Personal Details
    def set_first_name(self, fname):
        self.wait.until(EC.visibility_of_element_located(self.txt_first_name))
        element = self.driver.find_element(*self.txt_first_name)
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(fname)

    def set_middle_name(self, mdname):
        self.wait.until(EC.visibility_of_element_located(self.txt_middle_name))
        element = self.driver.find_element(*self.txt_middle_name)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(mdname)

    def set_last_name(self, lname):
        self.wait.until(EC.visibility_of_element_located(self.txt_last_name))
        element = self.driver.find_element(*self.txt_last_name)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(lname)

    # def set_nick_name(self, nick_name):
    #     self.wait.until(EC.visibility_of_element_located(self.txt_nick_name))
    #     self.driver.find_element(*self.txt_nick_name).clear()
    #     self.driver.find_element(*self.txt_nick_name).send_keys(nick_name)

    def set_employee_id(self, employee_id):
        self.wait.until(EC.visibility_of_element_located(self.txt_employee_id))
        element = self.driver.find_element(*self.txt_employee_id)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(employee_id)

    def set_other_id(self, other_id):
        self.wait.until(EC.visibility_of_element_located(self.txt_other_id))
        element = self.driver.find_element(*self.txt_other_id)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(other_id)

    def set_driver_licence(self, number):
        self.wait.until(EC.visibility_of_element_located(self.txt_driver_licence_number))
        element = self.driver.find_element(*self.txt_driver_licence_number)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(number)

    def set_licence_expire_date(self, date):
        self.wait.until(EC.visibility_of_element_located(self.txt_licence_expire_date))
        self.driver.find_element(*self.txt_licence_expire_date).clear()
        self.driver.find_element(*self.txt_licence_expire_date).send_keys(date)
        
    # def set_ssn(self, number):
    #     self.wait.until(EC.visibility_of_element_located(self.txt_SSN_number))
    #     self.driver.find_element(*self.txt_SSN_number).clear()
    #     self.driver.find_element(*self.txt_SSN_number).send_keys(number)
    #
    # def set_sin(self, number):
    #     self.wait.until(EC.visibility_of_element_located(self.txt_SIN_number))
    #     self.driver.find_element(*self.txt_SIN_number).clear()
    #     self.driver.find_element(*self.txt_SIN_number).send_keys(number)

    def set_nationality(self):
        self.wait.until(EC.visibility_of_element_located(self.drp_nationality))
        self.driver.find_element(*self.drp_nationality).click()
        self.driver.find_element(*self.select_nationality).click()

    def set_marital_status(self):
        self.wait.until(EC.visibility_of_element_located(self.drp_marital_status))
        self.driver.find_element(*self.drp_marital_status).click()
        self.driver.find_element(*self.select_marital_status).click()

    def set_dob(self, number):
        self.wait.until(EC.visibility_of_element_located(self.txt_dob))
        element = self.driver.find_element(*self.txt_dob)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(number)

    def set_gender(self, gender):
        if gender.lower() == "male":
            self.wait.until(EC.visibility_of_element_located(self.rd_male_gender))
            self.driver.find_element(*self.rd_male_gender).click()
        elif gender.lower() == "female":
            self.wait.until(EC.visibility_of_element_located(self.rd_female_gender))
            self.driver.find_element(*self.rd_female_gender).click()

    # def set_military_service(self, number):
    #     self.wait.until(EC.visibility_of_element_located(self.txt_military_service))
    #     self.driver.find_element(*self.txt_military_service).clear()
    #     self.driver.find_element(*self.txt_military_service).send_keys(number)
    #
    # def set_smoker(self, answer):
    #     if answer.lower() == "yes":
    #         self.wait.until(EC.visibility_of_element_located(self.cb_smoker))
    #         self.driver.find_element(*self.cb_smoker).click()

    def click_on_save_personal_details(self):
        self.wait.until(EC.visibility_of_element_located(self.btn_save_personal_details))
        self.driver.find_element(*self.btn_save_personal_details).click()

    # Custom Fields
    def set_blood_type(self):
        self.wait.until(EC.visibility_of_element_located(self.drp_blood_type))
        self.driver.find_element(*self.drp_blood_type).click()
        self.driver.find_element(*self.select_blood_type).click()

    def set_test_field(self, number):
        self.wait.until(EC.visibility_of_element_located(self.txt_test_field))
        element = self.driver.find_element(*self.txt_test_field)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(number)

    def click_on_save_custom_fields(self):
        self.wait.until(EC.visibility_of_element_located(self.btn_save_custom_fields))
        self.driver.find_element(*self.btn_save_custom_fields).click()

    # Attachment
    def click_on_add_attachment(self):
        self.wait.until(EC.visibility_of_element_located(self.btn_add_attachments))
        self.driver.find_element(*self.btn_add_attachments).click()

    def upload_file(self, file):
        self.wait.until(EC.visibility_of_element_located(self.btn_add_attachments))
        self.driver.find_element(*self.btn_upload_file).send_keys(file)

    def select_all_attachments(self):
        self.wait.until(EC.visibility_of_element_located(self.cb_select_all_attachments))
        self.driver.find_element(*self.cb_select_all_attachments).click()

    def click_on_delete_attachment(self):
        self.wait.until(EC.visibility_of_element_located(self.btn_delete_attachments))
        self.driver.find_element(*self.btn_delete_attachments).click()

    def set_attachment_comment(self, comment):
        self.wait.until(EC.visibility_of_element_located(self.txt_attachment_comment))
        self.driver.find_element(*self.txt_attachment_comment).send_keys(comment)

    def click_on_cancel_upload(self):
        self.wait.until(EC.visibility_of_element_located(self.btn_cancel_upload))
        self.driver.find_element(*self.btn_cancel_upload).click()

    def click_on_save_attachments(self):
        self.wait.until(EC.visibility_of_element_located(self.btn_save_attachments))
        self.driver.find_element(*self.btn_save_attachments).click()

    # Confirm msg
    def confirm_msg(self):
        msg = self.wait.until(EC.visibility_of_element_located(self.msg_confirm))
        return msg.text.split("\n")[1]




