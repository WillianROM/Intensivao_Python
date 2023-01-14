#https://www.youtube.com/watch?v=4FD6fYFGt5g
#https://drive.google.com/drive/folders/1o2lpxoi9heyQV1hIlsHXWSfDkBPtze-V

# Passo1: Entendimento do Desafio
import pandas as pd
    # pip install pandas
    # pip install numpy
    # pip install openpyxl

tabela = pd.read_csv("Aula4/advertising.csv")
"""
print(tabela)
print(tabela.info())
print(tabela.corr()) # Correlação
"""

    #Criar um gráfico
        # tem o plotly usado na aula 2, nessa aula é visto o matplotlib e seaborn
        # pip install matplotlib
        # pip install seaborn
        # pip install scikit-learn
import matplotlib.pyplot as plt
import seaborn as sns

#sns.heatmap(tabela.corr()) # Você cria o gráfico usando o seaborn
sns.heatmap(tabela.corr(), cmap="Greens", annot=True)
    # exibe o gráfico

plt.show() # Você exibe o gráfico que foi criado no seaborn através do matplotlib.pyplot

y = tabela["Vendas"]
x = tabela[["TV", "Radio", "Jornal"]]

from sklearn.model_selection import train_test_split 
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size=0.3)
    
    # Criar inteligencia artifical
        # Regressão Linear
        # RandomForest(Árvore de Decisão)
            # importar a inteligencia artificia
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

            # criar a inteligencia artificial
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

            # treinar a inteligencia artificial
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

RandomForestRegressor()

previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

from sklearn.metrics import r2_score
print(r2_score(y_teste, previsao_regressaolinear))
print(r2_score(y_teste, previsao_arvoredecisao))


tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["Previsao Arvore Decisao"] = previsao_arvoredecisao
tabela_auxiliar["Previsao Regressao Linear"] = previsao_regressaolinear

print(tabela_auxiliar)

sns.lineplot(data=tabela_auxiliar)
plt.show()

nova_tabela = pd.read_csv("Aula4/novos.csv")
print(nova_tabela)


previsao = modelo_arvoredecisao.predict(nova_tabela)
print(previsao)


# Passo2: Entendimento da Área/Empresa
# Passo3: Extração/Obtenção de Dados
# Passo4: Ajuste de Dados (Tratamento/Limpeza)
# Passo5: Análise Exploratória
# Passo6: Modelagem + Algoritmos (Aqui que entra a inteligência Artificial, se necessário)
# Passo7: Interpretação de Resultado
