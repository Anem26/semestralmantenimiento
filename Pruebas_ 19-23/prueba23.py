from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Prueba de automatización para el CU23 ver el cierre de sesion

driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.get("http://localhost/qatar/paginap.php")
# Iniciamos sesion en la pagina de login
driver.find_element(By.XPATH, "/html/body/nav/ul/li[6]/a").click()
time.sleep(5)

#obtener elementos
email = driver.find_element("id", "email")
contrasena = driver.find_element("id","pass")

#enviar datos a los elementos
correo = "prueba1@gmail.com"
email.send_keys(correo)
contrasena.send_keys("contraseña1")

#presionar enter para validar
contrasena.send_keys(Keys.ENTER)
time.sleep(3)

# Buscamos en el menu la pagina de cerrar sesion y la abrimos
driver.find_element(By.XPATH, "/html/body/nav/ul/li[1]/a").click()

url_error = "http://localhost/qatar/error.html"
url_true = "http://localhost/qatar/paginap.php"

#funcion
def CerrarSesion_Correcto():
    if(driver.current_url == url_true):
        return True
    else:
        return False
time.sleep(5)