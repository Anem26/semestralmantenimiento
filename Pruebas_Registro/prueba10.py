from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("http://localhost/qatar/regis.html")

#obtener elementos
email = driver.find_element("id", "correo")
usuario = driver.find_element("id","user")
contrasena = driver.find_element("id","pass")

#enviar datos a los elementos
username = "derek"
correo = "derek@gmail.com"
email.send_keys(correo)

usuario.send_keys(username)

passw = ""
contrasena.send_keys(passw)


#presionar enter para validar
contrasena.send_keys(Keys.ENTER)

#funcion
def registroPasswordVacio():
    if(passw == ""):
        return True
    else:
        return False