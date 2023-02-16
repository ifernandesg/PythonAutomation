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

select_de_status_xpath = '//*[@id="sorting-selector"]'
select_de_status = driver.find_element(By.XPATH, select_de_status_xpath)
Select(select_de_status).select_by_value('6')
select_de_status.click()
select_de_status.click()

time.sleep(5)

#nome
#Traz o resultado de outra lista
# result = driver.find_element(By.CSS_SELECTOR, '.py-1 li')
# print(result.text)

result = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/main/div[3]/div[1]/div[3]/div/ol/li[1]/div/article/div[2]/div[1]/section/h2/button')
print(result.text)

# for name in result:
#     print(name.text)
# driver.close()

# result = driver.find_element(By.CSS_SELECTOR, '.accommodation-list li')
# for name in result:
#     print(name.text)
# driver.close()

#avaliacao
# nome_xpath = '//*[@id="__next"]/div/div[1]/main/div[3]/div[1]/div[3]/div/ol/li[1]/div/article/div[2]/div[1]/section/h2/button/span'
# resultado_nome = driver.find_element(By.XPATH, nome_xpath)
# print (resultado_nome.text)
#valor

#xpath nome //*[@id="__next"]/div/div[1]/main/div[3]/div[1]/div[3]/div/ol/li[1]/div/article/div[2]/div[1]/section/h2/button
#xpath avaliacao //*[@id="__next"]/div/div[1]/main/div[3]/div[1]/div[3]/div/ol/li[1]/div/article/div[2]/div[1]/div[3]/button/span[1]/span/span[1]
#xpath valor //*[@id="__next"]/div/div[1]/main/div[3]/div[1]/div[3]/div/ol/li[1]/div/article/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/strong/span