from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("http://localhost/qatar/paginap.php")

#Caso de prueba 13- INICIAR UN JUEGO FALLIDO

driver.find_element(By.XPATH, '//*[@href="juego.html"] ').click()
time.sleep(1)
driver.find_element(By.ID, "active").click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@src="https://games.construct.net/32795/latest"]  ').click()

time.sleep(2)

url_true = "http://localhost/qatar/juegos.html"

def iniciarjuego():
    if(driver.current_url == url_true):
        return True
    else:
        return False

