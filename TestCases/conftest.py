from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium import webdriver
import pytest
import os
import sys

current_directory = os.path.abspath("../")
sys.path.append(current_directory)


@pytest.fixture()
def setup(browser):
    # if str.lower(browser) == "chrome":
    #     driver = webdriver.Chrome(executable_path="D:/Drivers/chromedriver-win64/")
    # elif str.lower(browser) == "firefox":
    #     driver = webdriver.Firefox(executable_path="path/to/geckodriver")
    # elif str.lower(browser) == "opera":
    #     driver = webdriver.Opera(executable_path="path/to/operadriver")
    # elif str.lower(browser) == "ie":
    #     driver = webdriver.Ie(executable_path="path/to/iedriver")
    # elif str.lower(browser) == "edge":
    #     driver = webdriver.Edge(executable_path="path/to/msedgedriver")
    if str.lower(browser) == "chrome":
        driver = webdriver.Chrome()
    elif str.lower(browser) == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# HTML Report

def pytest_configure(config):
    # config._metadata["Project name"] = "OrangeHRM"
    # config._metadata["Module Name"] = "Login"
    # config._metadata["Tester"] = "Rares"
    pass