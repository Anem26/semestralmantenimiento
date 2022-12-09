from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.get("http://localhost/qatar/paginap.php")


driver.find_element("id", "resu").click()
driver.get("http://localhost/qatar/resultados.php")
driver.find_element("id", "f2").click()

url_true = "http://localhost/qatar/resultados.php"
url_false = "http://localhost/qatar/error.html"
#funcion
def fecha2():
    if(driver.current_url == url_true):
        return True
    else:
        return False
time.sleep(10)
