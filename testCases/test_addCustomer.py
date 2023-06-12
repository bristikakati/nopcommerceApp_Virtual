from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import string
import random
from selenium.webdriver.common.by import By
import pytest

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen

    @pytest.mark.sanity
    def test_addCustomer(self, setup):

        # self.logger.info("******** Test_003_AddCustomer ********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # self.logger.info("******** Login successful *********")

        # self.logger.info("******** Starting Add Customer Test *********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddNew()

        # self.logger.info("******** Providing Customer Info *********")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("bristi")
        self.addcust.setLastName("kakati")
        self.addcust.setGender("Female")
        self.addcust.setDOB("01/01/1988")
        self.addcust.setCompanyName("Samsung")
        self.addcust.setAdminComment("Welcome bristi")
        self.addcust.clickOnSave()

        # self.logger.info("***** Saving customer info ********")
        # self.logger.info("***** Add customer validation started ********")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            # self.logger.info("****** Add Customer Test Passed ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            # self.logger.erroe("**** Add customer Test Failed *****")
            assert True == False

        self.driver.close()
        # self.logger.info("****** Ending Test_003_AddCustomer Test ******")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))





