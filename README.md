# ⚽ FutScore Analytics – Coleta e Análise de Desempenho de Jogadores

O **FutScore Analytics** é um projeto em **Python** que automatiza a **coleta, tratamento e análise de desempenho de jogadores de futebol**, obtendo **notas dos últimos 10 jogos** diretamente de sites como **WhoScored** e **SofaScore** via **Selenium**.  

Após a coleta, os dados são tratados com **Pandas** e analisados, gerando **gráficos comparativos e relatórios visuais** para facilitar insights e decisões.


## 🎯 Objetivo do Projeto

- Automatizar a coleta de **estatísticas de desempenho** de jogadores.
- Registrar as **notas atribuídas por jogo**.
- Permitir **análises de evolução e tendências** individuais.
- Facilitar **comparações entre jogadores, equipes e posições**.
- Gerar **visualizações claras e intuitivas** para suporte a análises.

---

## 📊 Tecnologias Utilizadas

- **Python 3.8+**
- **Selenium** → Web scraping dinâmico
- **Pandas** → Manipulação e tratamento de dados
- **Matplotlib** / **Seaborn** → Visualizações e gráficos
- **Google Chrome + ChromeDriver**

---

## 📂 Estrutura do Projeto

```bash
jogadores_brasileirao/
├── scraping/
│   └── scraper.py          # Script Selenium para coletar os dados
├── data/
│   └── ...                 # Arquivos CSV/JSON com dados coletados
├── analysis/
│   └── analise_dados.py    # Tratamento, melhoria e análise dos dados
├── docs/
│   └── img/                # Imagens e GIFs para documentação
├── main.py                 # Execução geral do projeto
├── dependencias.txt        # Lista de bibliotecas necessárias
└── README.md               # Documentação do projeto
