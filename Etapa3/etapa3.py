from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path="C:\Workspace\Desafios\Bemol\chromedriver.exe", chrome_options=chrome_options) 
driver.get("http://www.trivago.com.br")
driver.maximize_window()
driver.find_element("name","query").send_keys("Manaus")

time.sleep(2)

button_search = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div[3]/div/div/form/div[3]/button')
button_search.click()

time.sleep(35)

#Seleciona a ordenação
select_de_status_xpath = '//*[@id="sorting-selector"]'
select_de_status = driver.find_element(By.XPATH, select_de_status_xpath)
Select(select_de_status).select_by_value('6')
select_de_status.click()
select_de_status.click()

time.sleep(5)

#Printa no console o nome, avaliação e valor, respectivamente
resultName = driver.find_element(By.CSS_SELECTOR, '.py-1 .ItemName_nameWithFav__ijP51')
print(resultName.text)

resultEvaluation = driver.find_element(By.CSS_SELECTOR, '.py-1 .RatingPill_small__L_BAr')
print(resultEvaluation.text)

resultValue = driver.find_element(By.CSS_SELECTOR, '.py-1 .text-xl')
print(resultValue.text)


# #Salva no arquivo a resposta 
# with open("response.txt", "a") as f:
#         f.write(str(response))