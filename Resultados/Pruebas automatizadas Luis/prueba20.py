from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Prueba de automatización para el CU2 de ver jugadores de españa


driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.get("http://localhost/qatar/paginap.php")
# Buscamos en el menu la pagina de equipos y la abrimos 
driver.find_element("id", "equi2").click()
driver.get("http://localhost/qatar/equipos.php")
# Buscamos la bandera de españa
driver.find_element("id","españa").click()
# bajamos el scroll para ver los jugadores

#url para validar las pruebas
url_error = "http://localhost/qatar/error.html"
url_true = "http://localhost/qatar/espa%C3%B1a.php"

def registroJugadores():
    if(driver.current_url == url_true):
        return True
    else:
        return False

time.sleep(5)
