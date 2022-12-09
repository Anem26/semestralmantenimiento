from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.get("http://localhost/qatar/paginap.php")
# Buscamos en el menu la pagina de posiciones y la abrimos
driver.find_element("id", "equi2").click()
driver.get("http://localhost/qatar/equipos.php")
driver.find_element("id", "brasil").click()

#url para validar las pruebas
url_error = "http://localhost/qatar/error.html"
url_true = "http://localhost/qatar/brasil.php"

def registroLogros():
    if(driver.current_url == url_true):
        return True
    else:
        return False

time.sleep(6)
