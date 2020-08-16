import json
import requests

def request_dolar_from_api():
    request = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    price = request.json()
    actual_dollar_price = float(price['USD']['bid'])
    return actual_dollar_price

def convert_to_reais(reais, actual_dollar_price):
    conversion = reais / actual_dollar_price
    return conversion

print('\nReal (BRL) to Dollar (USD) converter')

reais = float(input('\nHow many R$ do you wish to convert to US$?: '))
dollars = request_dolar_from_api()

resultado = convert_to_reais(reais, dollars)

print('\nThe actual Dollar price is R${:.2f}. \nSo, with R${} it is possible to buy US${:.2f}!\n'.format(dollars, reais, resultado))
