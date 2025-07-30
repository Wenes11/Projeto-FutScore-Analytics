# Projeto-FutScore-Analytics
O objetivo deste projeto é automatizar a coleta de dados de desempenho de jogadores de futebol (notas dos últimos 10 jogos) a partir de sites como WhoScored e SofaScore, utilizando a biblioteca Selenium em Python.
# ⚽ Análise de Desempenho de Jogadores de Futebol

Este projeto tem como objetivo **automatizar a coleta de dados de desempenho de jogadores de futebol**, especificamente as **notas dos últimos 10 jogos**, utilizando **Web Scraping com Selenium em Python**. Os dados são extraídos de sites como **WhoScored** e **SofaScore**, e posteriormente tratados para realizar análises estatísticas e gerar gráficos comparativos.

---

## 🎯 Objetivo

Automatizar a coleta e análise de dados esportivos, focando nas **notas atribuídas aos jogadores** em cada partida. O objetivo final é visualizar a **evolução do desempenho**, identificar **tendências individuais** e permitir **comparações** entre jogadores, times e posições.

---

## 📊 Tecnologias Utilizadas

- 🐍 Python 3.8+
- 🌐 Selenium (Web scraping)
- 📊 Pandas (Manipulação de dados)
- 📈 Matplotlib / Seaborn (Visualização)
- 💻 Google Chrome + ChromeDriver

---

## 📁 Estrutura do Projeto

```bash
jogadores_brasileirao/
├── scraping/
│   └── scraper.py         # Script Selenium para coletar os dados
├── data/
│   ├── raw/               # Dados brutos (CSV)
│   └── processed/         # Dados tratados e prontos para análise
├── analysis/
│   └── jogadores_analysis.py  # Análise estatística e visual
├── assets/                # Imagens de jogadores e gráficos gerados
├── main.py                # Execução geral do projeto
├── requirements.txt       # Bibliotecas necessárias
└── README.md              # Descrição do projeto
