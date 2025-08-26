import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestCT03:
    def test_ct03_login_invalido(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("123456")
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()

        assert driver.find_element(By.XPATH, "//*[@data-test='error']").is_displayed()
        print("Não foi possível realizar o login, senha inválida")