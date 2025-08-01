from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Iniciar o navegador
whoscored = webdriver.Chrome()

# Acessar o site
whoscored.get('https://br.whoscored.com/statistics')
time.sleep(3)

# Aceitar cookies
clicar = whoscored.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/button')
clicar.click()
time.sleep(1)

# Pesquisar pelo Brasileirão
pesquisar = whoscored.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/input')
pesquisar.send_keys('Brasileirao')
pesquisar.send_keys(Keys.ENTER)
time.sleep(2)

# Clicar no link do Brasileirão
brasileirao = whoscored.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[1]/a')
brasileirao.click()
time.sleep(5)

# Coletar elementos
tabela_Brasileirao = whoscored.find_element(By.XPATH, '//*[@id="standings-24121"]/div[2]')
print("Tabela:\n", tabela_Brasileirao.text)

jogos_Brasileirao = whoscored.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div[4]/div[2]/div/div[4]/div/div')
print("\nJogos:\n", jogos_Brasileirao.text)

melhores_times_Brasileirao = whoscored.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div[9]')
print("\nMelhores Times:\n", melhores_times_Brasileirao.text)

artilheiros_Brasileirao = whoscored.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div[11]/table')
print("\nArtilheiros:\n", artilheiros_Brasileirao.text)

chutes_por_jogo = whoscored.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div[11]/div/div[2]')
print("\nChutes por jogo:\n", chutes_por_jogo.text)

assistencias_por_jogo = whoscored.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div[11]/div/div[3]')
print("\nAssistências por jogo:\n", assistencias_por_jogo.text)

ratings = whoscored.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div[11]/div/div[4]')
print("\nRatings:\n", ratings.text)

# Coletar as tabelas com pandas
# ...existing code...

# Coletar as tabelas com pandas
html = whoscored.page_source
tabelas = pd.read_html(html)

# Salvar a primeira tabela capturada no arquivo Dados_Brasileirao.xlsx
tabelas[0].to_excel('Dados_Brasileirao.xlsx', index=False)

# Exemplo: Exibir as tabelas capturadas
for i, tabela in enumerate(tabelas):
    print(f"\nTabela {i+1}:\n", tabela)

# Finalizar o navegador
whoscored.quit()
# ...existing code...