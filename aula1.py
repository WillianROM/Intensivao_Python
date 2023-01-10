# Instalar o  pyautogui (biblioteca de automação de comandos do mouse e do teclado) - pip install pyautogui

"""
https://www.youtube.com/watch?v=JKOLBw5sHCw
Na live do youtube foi usado o Jupyter
Como instalar o Jupyter?
https://youtu.be/_eK0z5QbpKA
"""
# import tabula (Para converter PDF em Pandas)
import pyautogui
import pyperclip
import time
"""
# pyautogui.click -> clicar
# pyautogui.write -> escrever
# pyautogui.press -> pressionar
# pyautogui.hotkey -> atalho
"""
"""
pyautogui.PAUSE = 1
time.sleep(4)
print(pyautogui.position())
"""
# Passo 1: Entrar no sistema da empresa (https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga)
pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(2)
pyautogui.hotkey("enter")
time.sleep(8)
#print(pyautogui.position()) # Para ver qual é a posição do mouse - Point(x=-886, y=450)
pyautogui.click(x=-886, y=450)

pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

# Passo 2: Navegar até o local do relatório (entrar na pasta Esportar)
time.sleep(10)
pyautogui.click(x=-1583, y=120, clicks=2)

# Passo 3: Esportar o relatório (fazer o download)
time.sleep(5)
pyautogui.click(x=-1602, y=120)
time.sleep(5)
pyautogui.click(x=-210, y=20)
time.sleep(5)
pyautogui.click(x=-445, y=467)
time.sleep(5)

# Passo 4: Calcular os indicadores (faturamento e quantidade de produtos)
import pandas as pd
# pip install pandas
# pip install numpy
# pip install openpyxl

tabela = pd.read_excel(r"C:\Users\willr\Downloads\Vendas - Dez.xlsx")
print(tabela)

faturamento = tabela["Valor Final"].sum() #Contar: tabela["Valor Final"].count() | Média: tabela["Valor Final"].mean() | Soma: tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

print(faturamento)
print(quantidade)


# Passo 5: Enviar um e-mail para a diretoria
    #  abrir aba e entrar no e-mail
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

    # clicar no botão escrever
pyautogui.click(x=134, y=238)

    # preencher as informações do e-mail
        # destinatário
pyautogui.write("opythonimpressionador@gmail.com")
pyautogui.hotkey("tab") # seleciona o email
pyautogui.hotkey("tab") # Pula para o campo assuntp

        # assuntos
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab") 

        # corpo
texto = """Prezados, bom dia!

O faturamento de ontem foi de: {faturamento}
A quantidade de oridytis foi de: {quantidade}
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab") 

    # enviar o e-mai
pyautogui.hotkey("ctrl", "enter")

