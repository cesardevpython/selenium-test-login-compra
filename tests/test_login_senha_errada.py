from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.XPATH, "//*[@id='login-button']").click()

assert driver.find_element(By.XPATH, "//*[@data-test='error']").is_displayed()
print("Não foi possível realizar o login, senha inválida")