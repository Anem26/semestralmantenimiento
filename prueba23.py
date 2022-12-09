from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("http://localhost/qatar/paginap.php")

#Caso de prueba 15- VER RESULTADOS

driver.find_element(By .XPATH, '//*[@href="resultados.php"]  ').click()
time.sleep(2)
driver.find_element(By.NAME, "20_nov").click()
time.sleep(1)
driver.find_element(By.NAME, "21_nov").click()
time.sleep(1)
driver.find_element(By.NAME, "22_nov").click()
time.sleep(1)
driver.find_element(By.NAME, "23_nov").click()

time.sleep(2)

url_true = "http://localhost/qatar/resultados.php"

def verResultados():
    if (driver.current_url == url_true):
        return True
    else:
        return False
