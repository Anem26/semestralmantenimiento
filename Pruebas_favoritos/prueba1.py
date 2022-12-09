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
contrasena.send_keys("contraseña1")


#presionar enter para validar
contrasena.send_keys(Keys.ENTER)

driver.get("http://localhost/qatar/paginap.php")

driver.find_element("id", "equi").click()
driver.get("http://localhost/qatar/equipos.php")
driver.find_element("id", "arg").click()
driver.get("http://localhost/qatar/argentina.php")
driver.find_element("id", "like").click()
driver.get("http://localhost/qatar/favorito.php")

url_true = "http://localhost/qatar/favorito.php"
url_false = "http://localhost/qatar/favoritoerror.php"
#funcion
def equipofav():
    if(driver.current_url == url_true):
        return True
    else:
        return False
time.sleep(10)
