from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Prueba de automatización para el CU1 de la tabla de posiciones

driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.get("http://localhost/qatar/paginap.php")
# Buscamos en el menu la pagina de tabla de posiciones y la abrimos
driver.find_element("id", "pos").click()

#url para validar las pruebas
url_error = "http://localhost/qatar/error.html"
url_true = "http://localhost/qatar/posiciones.php"

def registroTablaPosiciones():
    if(driver.current_url == url_true):
        return True
    else:
        return False

time.sleep(5)
