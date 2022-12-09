from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.get("http://localhost/qatar/login.php")

#obtener elementos
email = driver.find_element("id", "email")
contrasena = driver.find_element("id","pass")

#enviar datos a los elementos
correo = "admin@gmail.com"
email.send_keys(correo)
contrasena.send_keys("admin")


#presionar enter para validar
contrasena.send_keys(Keys.ENTER)

driver.get("http://localhost/qatar/paginap.php")

driver.find_element("id", "admi").click()
driver.get("http://localhost/qatar/admin.php")
driver.find_element("id", "eqa").click()
driver.find_element("id", "au").click()
driver.find_element("id", "eqb").click()
driver.find_element("id", "din").click()
driver.find_element("id", "gola").send_keys("1")
driver.find_element("id","golb").send_keys("0")
driver.find_element("id", "mod").click()
driver.get("http://localhost/qatar/admin.php")
driver.find_element("id", "grupo").click()
driver.find_element("id", "d").click()
driver.find_element("id", "el").click()


url_true = "http://localhost/qatar/admin.php"
url_false = "http://localhost/qatar/error.html"
#funcion
def admin():
    if(driver.current_url == url_true):
        return True
    else:
        return False
time.sleep(10)
