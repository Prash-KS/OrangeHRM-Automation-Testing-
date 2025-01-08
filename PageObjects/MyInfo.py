from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MyInfo():
    linkMyInfo_id = (By.XPATH, "//span[normalize-space()='My Info']")
    linkPhotoChange_id = (By.XPATH, "//img[@class='employee-image']")
    linkContactDetails_link = (By.XPATH, "//a[normalize-space()='Contact Details']")
    linkEmergencyContacts_link = (By.XPATH, "//a[normalize-space()='Emergency Contacts']")
    linkDependents_link = (By.XPATH, "//a[normalize-space()='Dependents']")
    linkImmigration_link = (By.XPATH, "//a[normalize-space()='Immigration']")
    linkJob_link = (By.XPATH, "//a[normalize-space()='Job']")
    linkSalary_link = (By.XPATH, "//a[normalize-space()='Salary']")
    #linkTaxExemptions_link = "Tax Exemptions" #not exist
    linkReportto_link = (By.XPATH, "//a[normalize-space()='Report-to']")
    linkQualifications_link = (By.XPATH, "//a[normalize-space()='Qualifications']")
    linkMemberships_link = (By.XPATH, "//a[normalize-space()='Memberships']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def ClickOnMyInfo(self):
        self.wait.until(EC.presence_of_element_located(self.linkMyInfo_id))
        self.driver.find_element(*self.linkMyInfo_id).click()

    def ClickOnPhotoChange(self):
        self.wait.until(EC.element_to_be_clickable(self.linkPhotoChange_id))
        self.driver.find_element(*self.linkPhotoChange_id).click()

    def ClickOnContactDetails(self):
        self.wait.until(EC.presence_of_element_located(self.linkContactDetails_link))
        self.driver.find_element(*self.linkContactDetails_link).click()

    def ClickOnEmergencyContacts(self):
        self.wait.until(EC.presence_of_element_located(self.linkEmergencyContacts_link))
        self.driver.find_element(*self.linkEmergencyContacts_link).click()

    def ClickOnDependents(self):
        self.wait.until(EC.presence_of_element_located(self.linkDependents_link))
        self.driver.find_element(*self.linkDependents_link).click()

    def ClickOnImmigration(self):
        self.wait.until(EC.presence_of_element_located(self.linkImmigration_link))
        self.driver.find_element(*self.linkImmigration_link).click()

    def ClickOnJob(self):
        self.wait.until(EC.presence_of_element_located(self.linkJob_link))
        self.driver.find_element(*self.linkJob_link).click()

    def ClickOnSalary(self):
        self.wait.until(EC.presence_of_element_located(self.linkSalary_link))
        self.driver.find_element(*self.linkSalary_link).click()

    # def ClickOnTaxExemptions(self):
    #     self.wait.until(EC.presence_of_element_located(self.linkTaxExemptions_link))
    #     self.driver.find_element(*self.linkTaxExemptions_link).click()

    def ClickOnReportTo(self):
        self.wait.until(EC.presence_of_element_located(self.linkReportto_link))
        self.driver.find_element(*self.linkReportto_link).click()

    def ClickOnQualifications(self):
        self.wait.until(EC.presence_of_element_located(self.linkQualifications_link))
        self.driver.find_element(*self.linkQualifications_link).click()

    def ClickOnMembership(self):
        self.wait.until(EC.presence_of_element_located(self.linkMemberships_link))
        self.driver.find_element(*self.linkMemberships_link).click()