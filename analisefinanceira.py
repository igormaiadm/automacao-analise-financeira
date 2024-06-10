import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

ticker = input("Digite o código da ação desejada: ")
data_inicial = input("Digite a data inicial (aaaa-mm-dd): ")
data_final = input("Digite a data final (aaaa-mm-dd): ")

dados = yfinance.Ticker(ticker).history(start=data_inicial, end=data_final).round(2)
fechamento = dados.Close
grafico = fechamento.plot()

maxima = fechamento.max().round(2)
minima = fechamento.min().round(2)
valor_medio = fechamento.mean().round(2)

destinatario = "[E-MAIL DO GESTOR] emaildogestor@xxxxx.com"
assunto = "[ASSUNTO] Análises Financeiras"

mensagem = f"""
Prezado gestor,

Seguem as análises solicitadas da ação {ticker} no intervalo de data ({data_inicial} à {data_final}):

Cotação máxima: R$ {maxima}
Cotação mínima: R$ {minima}
Cotação média: R$ {valor_medio}

Qualquer dúvida, estou à disposição.

Atenciosamente,
"""

# 1. Abrir o navegador e ir para o Gmail
webbrowser.open("www.gmail.com")
time.sleep(5)

# Configurando uma pausa de 3 segundos
pyautogui.PAUSE = 3

# 2. Clicar no botão "Escrever"
pyautogui.click(x=99, y=270)

# 3. Digitar o e-mail do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# 4. Digitar o assunto do e-mail e teclar TAB
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# 5. Digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# 6. Clicar no botão Enviar
pyautogui.click(x=1234, y=977)

print("E-mail enviado com sucesso!")
