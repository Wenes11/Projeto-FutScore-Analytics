from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import time
from io import StringIO
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
time.sleep(3)

# Clicar no link do Brasileirão
brasileirao = whoscored.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[1]/a')
brasileirao.click()
time.sleep(5)

# Coletar elementos
tabela_Brasileirao = whoscored.find_element(By.XPATH, '//*[@id="standings-24121"]/div[2]')
print("Tabela:\n", tabela_Brasileirao.text)

#Melhora a captura de dados, ou outra forma de pegar esse tipo de dados
jogos_Brasileirao = whoscored.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div[4]/div[2]/div/div[4]/div/div')
print("\nJogos:\n", jogos_Brasileirao.text)

#Entender melhor sobre esse dados coletados
melhores_times_Brasileirao = whoscored.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div[9]')
print("\nMelhores Times:\n", melhores_times_Brasileirao.text)

artilheiros_Brasileirao = whoscored.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div[11]/table')
print("\nArtilheiros:\n", artilheiros_Brasileirao.text)

chutes_por_jogo = whoscored.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div[9]/div/div[2]/div[1]')
print("\nChutes por jogo:\n", chutes_por_jogo.text)

assistencias_por_jogo = whoscored.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div[11]/div/div[3]')
print("\nAssistências por jogo:\n", assistencias_por_jogo.text)

ratings = whoscored.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div[11]/div/div[4]')
print("\nRatings:\n", ratings.text)

# Coletar as tabelas com pandas
# ...existing code...

# Coletar as tabelas com pandas
# Função para salvar HTML de um elemento como tabela
def salvar_tabela_elemento(elemento, nome_arquivo):
    """
    Salva a tabela de um elemento Selenium em um arquivo Excel dentro da pasta 'data' na raiz do projeto.
    Se não houver tabela, salva como CSV com o texto do elemento.
    """
    html_tabela = elemento.get_attribute("outerHTML")

    pasta_destino = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(pasta_destino, exist_ok=True)
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

    try:
        # Tenta ler como tabela HTML
        tabelas = pd.read_html(StringIO(html_tabela))
        if tabelas:
            tabelas[0].to_excel(caminho_arquivo, index=False)
            print(f"Tabela salva: {caminho_arquivo}")
            return
    except ValueError:
        pass  # Não encontrou tabela HTML

    # Se não encontrou tabela, salva como CSV com o texto bruto
    texto = elemento.text.strip()
    if texto:
        caminho_csv = caminho_arquivo.replace(".xlsx", ".csv")
        with open(caminho_csv, "w", encoding="utf-8") as f:
            f.write(texto)
        print(f"Nenhuma tabela encontrada. Texto salvo em: {caminho_csv}")
    else:
        print(f"Nenhum dado encontrado para {nome_arquivo}")


# Salvar cada dado em sua tabela
salvar_tabela_elemento(assistencias_por_jogo, "assistencia_por_jogo.xlsx")
salvar_tabela_elemento(tabela_Brasileirao, "Dados_brasileirao.xlsx")
salvar_tabela_elemento(melhores_times_Brasileirao, "melhores_equipes_brasileirao.xlsx")
salvar_tabela_elemento(artilheiros_Brasileirao, "artilheiros.xlsx")
salvar_tabela_elemento(ratings, "ratings_Brasileirao.xlsx")
salvar_tabela_elemento(jogos_Brasileirao, "jogos_da_rodada.xlsx")
salvar_tabela_elemento(chutes_por_jogo, "finalizacoes.xlsx")