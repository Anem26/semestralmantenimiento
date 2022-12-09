from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Prueba de automatización para el CU22 para descargar la tabla de posiciones
driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.get("http://localhost/qatar/paginap.php")
# Buscamos en el menu la pagina de posiciones y la abrimos
driver.find_element("id", "pos").click()
driver.get("http://localhost/qatar/posiciones.php")
driver.find_element("id", "descargartabla").click()

#url para validar las pruebas
url_error = "http://localhost/qatar/error.html"
url_true = "http://localhost/qatar/posiciones.php"

def registroDescargarContenido():
    if(driver.current_url == url_true):
        return True
    else:
        return False

time.sleep(5)
# cerramos el navegador
