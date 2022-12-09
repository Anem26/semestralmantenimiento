from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.get("http://localhost/qatar/login.php")

#obtener elementos
email = driver.find_element("id", "email")
contrasena = driver.find_element("id","pass")

#enviar datos a los elementos
correo = "prueba1@gmail.com"
email.send_keys(correo)
contrasena.send_keys("contraseña11")


#presionar enter para validar
contrasena.send_keys(Keys.ENTER)

#url para validar las pruebas
url_error = "http://localhost/qatar/error.html"
url_true = "http://localhost/qatar/paginap.php"

#funcion
def iniciaSesion_ContraseñaInvalida():
    if(driver.current_url == url_true):
        return True
    else:
        return False
time.sleep(1)