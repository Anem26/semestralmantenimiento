from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("http://localhost/qatar/paginap.php")


#Caso de prueba 14- BUSCAR JUEGOS ONLINE

driver.find_element(By .XPATH, '//*[@href="juego.html"] ').click()
time.sleep(1)

time.sleep(2)

url_true = "http://localhost/qatar/juegos.html"

def buscarjuegos():
    if (driver.current_url == url_true):
        return True
    else:
        return False

