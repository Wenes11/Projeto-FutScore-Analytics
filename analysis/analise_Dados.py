import os
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, dash_table
import plotly.graph_objects as go

# --- 1. FUNÇÕES DE LIMPEZA DOS DADOS ---

def carregar_e_limpar_artilheiros(caminho):
    """Carrega e limpa os dados de artilharia de forma robusta."""
    try:
        df = pd.read_excel(caminho)
        # Pega apenas as 4 primeiras colunas que contêm os dados principais
        df = df.iloc[:, :4] 
        df.columns = ['Ranking', 'Jogador', 'Time', 'Gols']
        
        # Limpeza
        df = df[pd.to_numeric(df['Ranking'], errors='coerce').notna()] # Garante que a primeira coluna seja um número
        df['Gols'] = pd.to_numeric(df['Gols'], errors='coerce')
        df.dropna(subset=['Gols'], inplace=True)
        return df
    except Exception as e:
        print(f"Erro ao processar o arquivo de artilheiros: {e}")
        return pd.DataFrame()

def carregar_e_limpar_ratings(caminho):
    """Carrega e limpa os dados de ratings de forma robusta."""
    try:
        df = pd.read_excel(caminho)
        # Pega apenas as 4 primeiras colunas que contêm os dados principais
        df = df.iloc[:, :4] 
        df.columns = ['Jogador', 'Time', 'Jogos', 'Rt']
        
        # Limpeza
        df = df[~df['Jogador'].astype(str).str.contains("Ordenado por", na=False)]
        df['Rt'] = pd.to_numeric(df['Rt'], errors='coerce')
        df.dropna(subset=['Rt'], inplace=True)
        return df
    except Exception as e:
        print(f"Erro ao processar o arquivo de ratings: {e}")
        return pd.DataFrame()

def carregar_e_limpar_classificacao(caminho):
    """Carrega e limpa os dados da tabela de classificação."""
    try:
        df = pd.read_excel(caminho)
        df.dropna(axis=1, how='all', inplace=True)
        colunas = ['Time', 'J', 'V', 'E', 'D', 'GM', 'GS', 'SG', 'Pts', 'Forma']
        df = df.iloc[:, :len(colunas)]
        df.columns = colunas
        df = df[~df['Time'].astype(str).str.contains("Time", na=False)]
        df['Time'] = df['Time'].str.replace(r'^\d+', '', regex=True).str.strip()
        df.dropna(how='all', inplace=True)
        return df
    except Exception as e:
        print(f"Erro ao processar o arquivo de classificação: {e}")
        return pd.DataFrame()


# --- 2. CARREGAMENTO DOS DADOS ---
PASTA_DADOS = os.path.join(os.path.dirname(__file__), '..', 'data')

df_artilheiros = carregar_e_limpar_artilheiros(os.path.join(PASTA_DADOS, 'artilheiros.xlsx'))
df_ratings = carregar_e_limpar_ratings(os.path.join(PASTA_DADOS, 'ratings_Brasileirao.xlsx'))
df_classificacao = carregar_e_limpar_classificacao(os.path.join(PASTA_DADOS, 'Dados_brasileirao.xlsx'))


# --- 3. CRIAÇÃO DO DASHBOARD ---
app = dash.Dash(__name__)
app.title = "Dashboard Brasileirão"

if not df_artilheiros.empty and not df_ratings.empty and not df_classificacao.empty:
    fig_artilheiros = px.bar(df_artilheiros.head(10), x='Jogador', y='Gols', title='Top 10 Artilheiros', text='Gols', hover_data=['Time'])
    fig_ratings = px.bar(df_ratings.head(10), x='Jogador', y='Rt', title='Top 10 Jogadores por Rating', text='Rt', hover_data=['Time', 'Jogos'])
    
    app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'padding': '20px', 'fontFamily': 'Segoe UI'}, children=[
        html.H1('Dashboard de Análise do Brasileirão', style={'textAlign': 'center', 'color': '#333'}),
        html.Div(className='row', style={'display': 'flex', 'justifyContent': 'center', 'gap': '20px', 'marginBottom': '40px'}, children=[
            dcc.Graph(id='grafico-artilheiros', figure=fig_artilheiros, style={'width': '48%'}),
            dcc.Graph(id='grafico-ratings', figure=fig_ratings, style={'width': '48%'})
        ]),
        html.H2('Tabela de Classificação', style={'textAlign': 'center', 'color': '#333'}),
        dash_table.DataTable(
            data=df_classificacao.to_dict('records'), columns=[{"name": i, "id": i} for i in df_classificacao.columns],
            style_cell={'textAlign': 'left', 'fontFamily': 'Segoe UI', 'padding': '10px'},
            style_header={'backgroundColor': '#e0e0e0', 'fontWeight': 'bold'},
            style_data_conditional=[{'if': {'row_index': 'odd'}, 'backgroundColor': '#f2f2f2'}],
            style_table={'width': '80%', 'margin': 'auto', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)'}
        )
    ])
else:
    app.layout = html.Div([html.H1('Erro ao Carregar Dados', style={'color': 'red'})])


# --- 4. EXECUTAR A APLICAÇÃO ---
if __name__ == '__main__':
    app.run(debug=True)

