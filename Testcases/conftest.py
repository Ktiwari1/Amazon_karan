import time

from selenium import webdriver
import pytest

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--URL", action="store", default="https://www.amazon.in")



@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    url = request.config.getoption("URL")
    if url == "prod_URL":
        driver.get("https://www.amazon.in")
    elif url == "qa_URL":
        driver.get("https://www.amazon.com")
    driver.maximize_window()
    request.cls.driver = driver
    # yield
    # driver.close()
