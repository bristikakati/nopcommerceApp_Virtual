from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver=webdriver.Chrome(service=serv_obj)
        print("Launching Chrome browser")
    elif browser=='edge':
        serv_obj = Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)
        print("Launching Edge browser")
    else:
        serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    return driver

def pytest_addoption(parser): #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture() #This will return browser value to setup method
def browser(request):
    return request.config.getoption("--browser")

########### Pytest HTML Report ###########
# It is hook for adding environment info to HTML report

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Bristi'

#It is hook for delete/modify environment info to HTML Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

