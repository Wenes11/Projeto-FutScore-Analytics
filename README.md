<p align="center">
<img src="https://www.google.com/search?q=https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Soccer%2520Ball.png" alt="Soccer Ball" width="120" height="120" />
</p>

<h1 align="center">⚽ FutScore Analytics – Dashboard do Brasileirão</h1>

<p align="center">
<strong>Um projeto completo de Web Scraping e Visualização de Dados para análise do Campeonato Brasileiro.</strong>
</p>

<p align="center">
<img alt="Status" src="https://www.google.com/search?q=https://img.shields.io/badge/status-conclu%C3%ADdo-green%3Fstyle%3Dfor-the-badge">
<img alt="Python" src="https://www.google.com/search?q=https://img.shields.io/badge/Python-3.8%2B-blue%3Fstyle%3Dfor-the-badge%26logo%3Dpython">
<img alt="Feito com" src="https://www.google.com/search?q=https://img.shields.io/badge/feito%2520com-Dash%2520%26%2520Plotly-purple%3Fstyle%3Dfor-the-badge">
</p>

O FutScore Analytics é uma aplicação em Python que automatiza todo o fluxo de análise de dados do futebol: desde a coleta de estatísticas do site WhoScored.com até a apresentação em um dashboard interativo.

Utilizando Selenium para a extração dos dados, Pandas para a limpeza e tratamento, e Dash/Plotly para a visualização, o projeto oferece uma visão clara e objetiva sobre o desempenho das equipes e jogadores do Campeonato Brasileiro.

✨ Funcionalidades Principais
Coleta Automatizada: Busca dados atualizados do Brasileirão sem intervenção manual.

Limpeza de Dados Robusta: O script de análise está preparado para lidar com inconsistências e formatos inesperados dos dados extraídos.

Dashboard Interativo e Informativo:

Gráfico com o Top 10 Artilheiros do campeonato.

Gráfico com o Top 10 Jogadores por Rating de desempenho.

Tabela de Classificação completa e atualizada.

Design limpo para uma análise rápida e eficiente.

📊 Tecnologias Utilizadas
Linguagem: Python 3.8+

Web Scraping: Selenium

Manipulação de Dados: Pandas

Dashboard Web: Dash & Plotly

Interface do Navegador: ChromeDriver

📂 Estrutura do Projeto
A arquitetura do projeto foi desenhada para separar as responsabilidades, facilitando a manutenção e escalabilidade.

Projeto-FutScore-Analytics/
├── scraping/
│   ├── scraper.py          # Script para extrair os dados do WhoScored
│   └── __init__.py
├── data/
│   └── *.xlsx              # Arquivos Excel com os dados brutos coletados
├── analysis/
│   ├── analise_Dados.py    # Script para limpar os dados e criar o dashboard
│   └── __init__.py
├── main.py                 # Ponto de entrada para iniciar a aplicação
├── requirements.txt        # Lista de dependências do projeto
└── README.md               # Esta documentação

🚀 Como Executar o Projeto
Siga os passos abaixo para ter o dashboard rodando em seu ambiente local.

1. Pré-requisitos
Python 3.8 ou superior instalado.

Navegador Google Chrome instalado.

2. Instalação
Primeiro, clone o repositório. Depois, abra o terminal na pasta raiz do projeto e instale todas as bibliotecas necessárias com um único comando:

pip install -r requirements.txt

3. Coleta de Dados
Antes de visualizar o dashboard, execute o script de scraping para obter os dados mais recentes.

# O script está dentro da pasta 'scraping'
python scraping/scraper.py

Este comando abrirá uma janela do Chrome, coletará as informações e salvará os arquivos .xlsx na pasta data/.

4. Visualização do Dashboard
Com os dados coletados, inicie o servidor local:

python main.py

O terminal exibirá uma mensagem de confirmação. Agora, abra seu navegador e acesse o seguinte endereço para ver o dashboard em ação:

➡️ http://127.0.0.1:8050/

🔮 Próximos Passos e Melhorias
Adicionar mais gráficos (ex: posse de bola, chutes por jogo).

Implementar filtros interativos no dashboard (ex: filtrar por time).

Criar um executável (.exe) para facilitar o uso por pessoas sem conhecimento de programação.

Portar a extração de dados para uma API, se disponível, para maior estabilidade.
