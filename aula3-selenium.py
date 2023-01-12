# https://www.youtube.com/watch?v=g-zVpeJtkFk
# Para fazer o download do Arquivo da Aula: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv

# Instalar o selenium e o webdriver-manager na máquina:
# pip install selenium
# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# utilizar o webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install()) # Para instalar o chormedriver conforme a versão atual do Chrome da máquina do usuário


# Rodar o navegador em background
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)


driver = webdriver.Chrome(service=servico)

driver.maximize_window()

# Passo1: Pegar a cotação do dólar
driver.get("https://www.google.com.br/")

driver.find_element(By.NAME,'q').send_keys('Cotação do dólar', Keys.ENTER)
cotacao_dolar = driver.find_element(By.XPATH,'//span[@data-name="Real brasileiro"]/preceding-sibling::span').get_attribute('data-value')

print(cotacao_dolar)

# Passo2: Pegar a cotação do euro
driver.get("https://www.google.com.br/")

driver.find_element(By.NAME,'q').send_keys('Cotação do euro', Keys.ENTER)
cotacao_euro = driver.find_element(By.XPATH,'//span[@data-name="Real brasileiro"]/preceding-sibling::span').get_attribute('data-value')

print(cotacao_euro)

# Passo3: Pegar a cotação do ouro
driver.get('https://www.melhorcambio.com/ouro-hoje')

cotacao_ouro = driver.find_element(By.CSS_SELECTOR,'.text-verde#comercial').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',','.')

print(cotacao_ouro)

driver.quit

# Passo4:Importar a base de dados e Atualizar a base
import pandas as pd
# pip install pandas
# pip install numpy
# pip install openpyxl

tabela = pd.read_excel('Aula3/Produtos.xlsx')

# Passo5: Recalcular os preços
    # atualizar a cotação
        #tabela.loc[linha, coluna] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

    # preço de compra = cotacao * preco original
tabela["Preço de Compra"] = tabela["Cotação"] * tabela["Preço Original"]

#tabela["Preço de Compra"] = tabela["Preço de Compra"].map('R${:.2f}'.format)

    # preco de venda = preco de compra * margem
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

tabela["Preço de Venda"] = tabela["Preço de Venda"].map('R${:.2f}'.format)

print(tabela)

# Passo6: Exportar a base atualizada
tabela.to_excel('Aula3/ProdutosNovo.xlsx',index=False)
