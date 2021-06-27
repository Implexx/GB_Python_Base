import requests
from datetime import datetime
from decimal import Decimal


def currency_rates(code):
    """
    Вычисляет по введенному коду страны курс к рублю
    :param code: str, код страны вида 'XXX'
    :return: decimal, курс валюты в рублях
    """
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    request = requests.get(url)
    text = request.text
    # находим индекс в тексте введенного кода валюты
    code_index = text.find(code.upper())
    # Если нашлось
    if code_index != -1:
        # ищем индекс тега value следующий за тегом нужного кода
        value_index = text.find('<Value>', code_index)
        # получаем значение value
        value = text[value_index + 7:value_index + 14]
        # получаем дату из текста
        date_index = text.find('Date="')
        date_temp = text[date_index + 6:date_index + 16]
        date = datetime.strptime(date_temp, '%d.%m.%Y').date()
        # возвращаем результат в Decimal и объект datetime.date
        return Decimal(value.replace(',', '.')), date
    # если кода нет в тексте возвращаем None
    else:
        return None
