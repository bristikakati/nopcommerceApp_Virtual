import time

from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import ExcelUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/Logindata.xlsx"

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):

        self.logger.info("************ Test_002_DDT_Login **************")
        self.logger.info("****************** Verify Login DDT Test ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver) #lp->object of class LoginPage

        self.rows=ExcelUtils.getRowCount(self.path,'Sheet1')
        print("No of rows in a Excel",self.rows)

        lst_status=[]

        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path,"Sheet1",r,1)
            self.password = ExcelUtils.readData(self.path,"Sheet1",r,2)
            self.exp = ExcelUtils.readData(self.path,"Sheet1",r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("**** Passed ****")
                    self.lp.clicklogout();
                    lst_status.append("pass")
                elif self.exp == "fail":
                    self.logger.info("**** Failed ****")
                    self.lp.clicklogout();
                    lst_status.append("fail")

            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("**** Failed ****")
                    lst_status.append("fail")
                elif self.exp == "fail":
                    self.logger.info("**** Passed ****")
                    lst_status.append("pass")

        if "fail" not in lst_status:
            self.logger.info("******* Loggin DDT test passed *********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********* Loggin DDT test failed *********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Loggin DDT test *********")
        self.logger.info("******* Completed TC Login DDT_002 *********")
