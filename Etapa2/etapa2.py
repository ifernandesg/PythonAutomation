from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

#Modify PATH to chromedriver location
PATH = "~/chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#Initialize webdriver and go to url
driver = webdriver.Chrome(executable_path="PATH", chrome_options=chrome_options) 
driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php")
driver.maximize_window()

#Search for the ZIP Code and click search button
time.sleep(2)
driver.find_element("id","endereco").send_keys("69005-040")
time.sleep(1)
driver.find_element("name","btn_pesquisar").send_keys(Keys.RETURN)
time.sleep(1)
#Return to home page
driver.find_element("id","btn_nbusca").send_keys(Keys.RETURN)
time.sleep(1)
#Search for Company name and click search button
driver.find_element("name","endereco").send_keys("Lojas Bemol")
time.sleep(1)
driver.find_element("name","btn_pesquisar").send_keys(Keys.RETURN)

#Preparing to shutdown
time.sleep(5)
driver.close()