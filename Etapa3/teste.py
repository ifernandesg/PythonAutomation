from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.headless = True
browser = webdriver.Chrome(executable_path="C:\Workspace\Desafios\Bemol\chromedriver.exe", options=options)
browser.get("http://random-name-generator.info/")
names = browser.find_elements(By.CSS_SELECTOR, '.nameList li')
for name in names:
    print(name.text)
browser.close()