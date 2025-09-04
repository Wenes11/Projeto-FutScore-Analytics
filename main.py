#Onde vai ser rodado o projeto
#O projeto será rodado em um ambiente local utilizando Python e bibliotecas como Selenium para automação de navegador.

from analysis.analise_Dados import app

if __name__ == '__main__':
    print("Iniciando o dashboard... Acesse http://127.0.0.1:8050/ no seu navegador.")
    # CORREÇÃO FINAL: Usar app.run() em vez de app.run_server()
    app.run(debug=True)