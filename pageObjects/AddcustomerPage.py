import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
    lnkCustomers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCutomers_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_Addnew_xpath="//a[@class='btn btn-primary']"

    txt_Email_xpath="//input[@id='Email']"
    txt_Password_xpath="//input[@id='Password']"
    txt_Firstname_xpath="//input[@id='FirstName']"
    txt_Lastname_xpath="//input[@id='LastName']"
    rd_MaleGender_xpath="//input[@id='Gender_Male']"
    rd_FemaleGender_xpath="//input[@id='Gender_Female']"
    txt_dob_xpath="//input[@id='DateOfBirth']"
    txt_Companyname_xpath="//input[@id='Company']"
    drp_Newsletter_xpath="//select[@id='SelectedNewsletterSubscriptionStoreIds'"
    drp_CustomerRoles_xpath="//select[@id='SelectedCustomerRoleIds']"
    drp_ManagerVendor_xpath="//select[@id='VendorId']"
    txt_AdminComment_xpath="//textarea[@id='AdminComment']"

    btn_Save_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCutomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btn_Addnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_Email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txt_Password_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.txt_Firstname_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.txt_Lastname_xpath).send_keys(lastname)

    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.XPATH,self.rd_MaleGender_xpath).click()
        elif gender=="Female":
            self.driver.find_element(By.XPATH,self.rd_FemaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.rd_MaleGender_xpath).click()

    def setDOB(self,dob):
        self.driver.find_element(By.XPATH,self.txt_dob_xpath).send_keys(dob)

    def setCompanyName(self,companyname):
        self.driver.find_element(By.XPATH,self.txt_Companyname_xpath).send_keys(companyname)

    def setAdminComment(self,admincomment):
        self.driver.find_element(By.XPATH,self.txt_AdminComment_xpath).send_keys(admincomment)

    def clickOnSave(self,):
        self.driver.find_element(By.XPATH,self.btn_Save_xpath).click()

    










    
