import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    #setup
    global driver
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # Run test
    yield

    # Teardown
    driver.quit()