from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#Modify PATH to chromedriver location
PATH = "~/chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#Initialize webdriver and go to url
driver = webdriver.Chrome(executable_path="PATH", chrome_options=chrome_options) 
driver.get("http://www.trivago.com.br")
driver.maximize_window()

#Search for Manaus and click search button
driver.find_element("name","query").send_keys("Manaus")
time.sleep(2)
buttonSearchXpath = '//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div[3]/div/div/form/div[3]/button'
buttonSearch = driver.find_element(By.XPATH, buttonSearchXpath)
buttonSearch.click()

#Wait for elements to load
time.sleep(35)

#Select the dropdown option
selectStatusXpath = '//*[@id="sorting-selector"]'
selectStatus = driver.find_element(By.XPATH, selectStatusXpath)
Select(selectStatus).select_by_value('6')
selectStatus.click()
selectStatus.click()
time.sleep(10)

#Print name, evaluation and result of the first result after the filter
resultNameCssSelector = '.py-1 .ItemName_nameWithFav__ijP51'
resultName = driver.find_element(By.CSS_SELECTOR, resultNameCssSelector)
print(resultName.text)
resultEvaluationCssSelector = '.py-1 .RatingPill_small__L_BAr'
resultEvaluation = driver.find_element(By.CSS_SELECTOR, resultEvaluationCssSelector)
print(resultEvaluation.text)
resultValueCssSelector = '.py-1 .text-xl'
resultValue = driver.find_element(By.CSS_SELECTOR, resultValueCssSelector)
print(resultValue.text)

#Preparing to shutdown
time.sleep(5)
driver.close()