from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("http://localhost/qatar/paginap.php")

#Caso de prueba 15- AGREGAR UN EQUIPO FAVORITO SIN INICIAR SESIÓN [B]
driver.find_element(By.XPATH, '//*[@href="equipos.php"]  ').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@src="img/argentina.png"] ').click()
time.sleep(1)
driver.find_element(By.NAME, "pulsado").click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@href="favoritoerror.php"]  ').click()

time.sleep(2)

url_true = "http://localhost/qatar/favoritoerror.php"

def agregarFavoritoSinSesionB():
    if (driver.current_url == url_true):
        return True
    else:
        return False
