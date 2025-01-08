import time

from PageObjects.LoginPage import loginpage
from PageObjects.PersonalDetails import PersonalDetails
from PageObjects.MyInfo import MyInfo
from utilities.customlogger import logGen
from utilities.ReadProperties import ReadConfig
import pytest


class Test_003_Edit_Personal_Details():
    baseurl = ReadConfig.GetAplicationUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = logGen.logger()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Personal_Details(self, setup):
        self.logger.info("*** Test_003_Edit_Personal_Details ***")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()

        self.logger.info("*** Succesfully logged ***")
        self.logger.info("*** Started Edit Personal Details Test ***")
        self.opencategory = MyInfo(self.driver)
        self.opencategory.ClickOnMyInfo()
        self.editpersdetails = PersonalDetails(self.driver)
        self.logger.info("*** Modifying Personal Details ***")

        # Personal Details
        self.editpersdetails.set_first_name("Andrei")
        self.editpersdetails.set_middle_name("Ionut")
        self.editpersdetails.set_last_name("Popescu")
        # self.editpersdetails.set_nick_name("Andrew")
        self.editpersdetails.set_employee_id("5467")
        self.editpersdetails.set_other_id("31321")
        self.editpersdetails.set_driver_licence("123523")
        self.editpersdetails.set_licence_expire_date("2027-02-27")
        # self.editpersdetails.set_ssn("405")
        # self.editpersdetails.set_sin("332")
        self.editpersdetails.set_nationality()
        self.editpersdetails.set_marital_status()
        self.editpersdetails.set_dob("2001-01-29")
        self.editpersdetails.set_gender("Male")
        # self.editpersdetails.set_military_service("Active Guard")
        # self.editpersdetails.set_smoker("Yes")
        time.sleep(10)
        self.editpersdetails.click_on_save_personal_details()

        self.logger.info("*** Saving info ***")
        self.logger.info("*** Personal Details Validation Started ***")

        # Verifying if the details have been modified
        self.msg = self.editpersdetails.confirm_msg()

        if self.msg == "Successfully Updated":
            self.logger.info("*** Edit Personal Details Test Passed ***")
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_personal_details.png")
            self.logger.error("*** Edit Personal Details Test Failed ***")
            assert False

        # Custom Fields
        self.editpersdetails.set_blood_type()
        self.editpersdetails.set_test_field(450)
        self.editpersdetails.click_on_save_custom_fields()

        self.logger.info("*** Saving info ***")
        self.logger.info("*** Custom Fields Validation Started ***")

        # Verifying if the details have been modified
        self.msg = self.editpersdetails.confirm_msg()

        if self.msg == "Successfully Saved":
            self.logger.info("*** Edit Custom Fields Test Passed ***")
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_custom_fields.png")
            self.logger.error("*** Edit Custom Fields Test Failed ***")
            assert False

        self.driver.close()
        self.logger.info("*** Ending Personal Details test ***")

