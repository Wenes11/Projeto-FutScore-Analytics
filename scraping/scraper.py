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

tabale_Brasileirao = whoscored.find_element(By.XPATH,'//*[@id="standings-24121"]/div[2]')
print(tabale_Brasileirao.text)

jogos_Brasileirao = whoscored.find_element(By.XPATH,'/html/body/div[4]/div[3]/div[1]/div[4]/div[2]/div/div[4]/div/div')
print(jogos_Brasileirao.text)

melhores_timesBrsasileirao = whoscored.find_element(By.XPATH,'/html/body/div[4]/div[3]/div[1]/div[9]')
print(melhores_timesBrsasileirao.text)

artilheiros_Brasileirao = whoscored.find_element(By.XPATH,'/html/body/div[4]/div[3]/div[1]/div[11]/table')
print(artilheiros_Brasileirao.text)

chutes_por_jogo = whoscored.find_element(By.XPATH,'/html/body/div[4]/div[3]/div[1]/div[11]/div/div[2]')
print(chutes_por_jogo.text)

assisentencias_por_jogo = whoscored.find_element(By.XPATH,'//html/body/div[4]/div[3]/div[1]/div[11]/div/div[3]')
print(assisentencias_por_jogo.text)

ratings= whoscored.find_element(By.XPATH,'/html/body/div[4]/div[3]/div[1]/div[11]/div/div[4]')
print(ratings.text) 

quit= whoscored.quit()