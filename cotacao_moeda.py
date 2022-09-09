import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()

dolar = cotacoes['USDBRL']['bid']
euro = cotacoes['EURBRL']['bid']

print(f"Cotação do Dólar: {dolar}")
print(f"Cotação do Euro: {euro}")