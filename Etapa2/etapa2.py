from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path="C:\Workspace\Desafios\Bemol\chromedriver.exe", chrome_options=chrome_options) 
driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php")
driver.find_element("id","endereco").send_keys("69005-040")
driver.find_element("name","btn_pesquisar").send_keys(Keys.RETURN)

time.sleep(1)

driver.find_element("id","btn_nbusca").send_keys(Keys.RETURN)

time.sleep(1)

driver.find_element("name","endereco").send_keys("Lojas Bemol")
driver.find_element("name","btn_pesquisar").send_keys(Keys.RETURN)