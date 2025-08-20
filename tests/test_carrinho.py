from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicia o navegador Edge
driver = webdriver.Edge()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Cria wait explícito
wait = WebDriverWait(driver, 10)

# Realizando o login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Adicionando primeiro produto ao carrinho
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

# Retornando ao menu de itens
driver.find_element(By.ID, "continue-shopping").click()

# Adicionando outro produto ao carrinho
wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bike-light']")
)).click()

# Vai até o carrinho de novo
driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()

# Verifica se os dois produtos estão no carrinho
item1 = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//*[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']")
))
item2 = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//*[@data-test='inventory-item-name' and text()='Sauce Labs Bike Light']")
))

assert item1.is_displayed()
assert item2.is_displayed()

print("Teste finalizado com sucesso!")
driver.quit()
