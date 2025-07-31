from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
whoscored = webdriver.Chrome()

whoscored.get('https://br.whoscored.com/statistics')
clicar = whoscored.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/button')
clicar.click()
pesquisar = whoscored.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/input')
pesquisar.send_keys('Brasileirao')
pesquisar.send_keys(Keys.ENTER)

brasileirao = whoscored.find_element(By.XPATH,'/html/body/div[4]/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[1]/a')
brasileirao.click()

time.sleep(200) 