import requests

r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

def currency_rates():
    char_code = input('Введите код валюты: ')
    ind_char_code = r.text.find(char_code.upper())
    if ind_char_code == -1:
        return None
    ind_v = r.text[ind_char_code:].find('Value')
    start = ind_v + 6
    end = start + 7
    value = r.text[ind_char_code:][start:end]
    return f'Курс {char_code.upper()} {value}'

