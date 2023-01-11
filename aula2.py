#https://www.youtube.com/watch?v=UG5RwrtkiL4
import pandas as pd #necessário instalar o pandas
# pip install pandas
# pip install numpy
# pip install openpyxl



#Para fazer o download do Arquivo da Aula: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs

# Passo 1: Importar a base de dados
tabela = pd.read_csv("Aula2/telecom_users.csv")
print(tabela)

# Passo 2: Visualizar a base de dados
    # - Entender as informações que você tem disponível
    # - Descobrir as cagas da base de dados

tabela.drop("Unnamed: 0", axis=1) #Para eliminar uma coluna. Se quisesse excluir a linha 3, então seria: tabela.drop("3", axis=0)
        # Se quiser excluir mais de uma coluna ou linha, faça uma lista como o exemplo ao lado para colunas: tabela.drop(["Unnamed: 0","Casado","Churn"], axis=1)
        # axis -> 0 = Linha | axis -> 1 = coluna



print(tabela)

# Passo 3: Tratamento de Dados
print(tabela.info()) # Fazer um micro resumo da tabela (informações)
    # resolver os valores que estão sendo reconhecidos de forma errada (conforme visto em tabela.info())
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce" ) #converte a coluna para numérico
        # errors="ignore" - Ignorar o erro
        # errors="raize" - Mostrar o erro
        # errors="coerce" - Força a mudança

    # resolver valorez vazios

        # colunas em que TODOS os valores são vazios, eu vou excluir
tabela.dropna(how="all", axis=1) # Verificar a sua tabela e exclui o que estão vazios

        # linhas que tem PELO MENOS 1 valor vazio (que possuem ALGUM valor vazio)
tabela.dropna(how="any", axis=0)

# Passo 4: Análise Inicial
print(tabela["Churn"].value_counts()) # Para contar os valores
print(tabela["Churn"].value_counts(normalize=True)) # Vai mostrar os valores em percentual e para deixar no formato percentual, use map("{:.1%}".format)) como abaixo:
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))


# Passo 5: Análise detalhada - descobrir as causas do cancelamento
    # Comparar cada coluna da base de dados com a coluna Churn
import plotly.express as px # Para criar gráfico
        # pip install plotly
        # Cria o gráfico
coluna = "TipoContrato"
grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
        # Outros gráficos
        # px.barplot - Gráfico de barras
        # px.piechart - Gráfico de Pizza

            # exibe o gráfico
grafico.show()

    # Para cada coluna da minha tabela, eu quero criar um gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    grafico.show()

