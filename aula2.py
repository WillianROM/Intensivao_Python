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

# Passo 5: Análise detalhada - descobrir as causas do cancelamento
