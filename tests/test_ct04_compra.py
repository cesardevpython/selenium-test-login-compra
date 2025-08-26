import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestCT04:
    def test_ct04_compra(self):
        # --------------------------
        # Realizando o login
        # --------------------------
        driver = conftest.driver
        # Cria wait explícito
        wait = WebDriverWait(driver, 10)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # --------------------------
        # Adicionando primeiro produto ao carrinho
        # --------------------------
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
        )).click()

        # Vai até o carrinho
        driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()

        # Verifica se o primeiro produto está no carrinho
        item1 = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']")
        ))
        assert item1.is_displayed()

        # --------------------------
        # Retornando ao menu de itens
        # --------------------------
        driver.find_element(By.ID, "continue-shopping").click()

        # --------------------------
        # Adicionando outro produto ao carrinho
        # --------------------------
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bike-light']")
        )).click()

        # Vai até o carrinho de novo
        driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()

        # --------------------------
        # Verifica se os dois produtos estão no carrinho
        # --------------------------
        item1 = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']")
        ))
        item2 = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@data-test='inventory-item-name' and text()='Sauce Labs Bike Light']")
        ))

        assert item1.is_displayed()
        assert item2.is_displayed()

        # Realizando a compra
        driver.find_element(By.XPATH, "//*[@id='checkout']").click()

        # Introduzindo os dados pessoais
        driver.find_element(By.ID, "first-name").send_keys("Cesar")
        driver.find_element(By.ID, "last-name").send_keys("Henrique da Silva")
        driver.find_element(By.ID, "postal-code").send_keys("53435200")
        driver.find_element(By.ID, "continue").click()

        # Finalizando
        assert driver.find_element(By.XPATH, "//*[@data-test='title' and text()='Checkout: Overview']").is_displayed()
        driver.find_element(By.ID, "finish").click()
        assert driver.find_element(By.XPATH, "//*[@data-test='complete-header' and text()='Thank you for your order!']").is_displayed()

        print("Tudo certo, rodou tudo!")