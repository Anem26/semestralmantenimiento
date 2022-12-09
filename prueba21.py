from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("http://localhost/qatar/paginap.php")

#Caso de prueba 16- IR A INICIO DE SESIÓN DESDE FAVORITOS
driver.find_element(By .XPATH, '//*[@href="favoritoerror.php"]  ').click()
time.sleep(1)
driver.find_element(By .XPATH, '//*[@href="login.php"]  ').click()

time.sleep(2)

url_true = "http://localhost/qatar/login.php"

def crearUsuarioFavoritos():
    if(driver.current_url == url_true):
        return True
    else:
        return False
