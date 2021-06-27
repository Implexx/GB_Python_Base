"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в
обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str,
решить поставленную задачу? Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет
в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
"""

import requests
from datetime import datetime
from decimal import Decimal

# делаем запрос и получаем результат в виде строки
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
request = requests.get(url)
text = request.text


def currency_rates(code):
    """
    Вычисляет по введенному коду страны курс к рублю
    :param code: str, код страны вида 'XXX'
    :return: decimal, курс валюты в рублях
    """
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


print(f'Курс Евро = {currency_rates("AUD")[0]} ... Дата актуальности {currency_rates("AUD")[1]}')
print(f'Курс Евро = {currency_rates("usd")[0]} ... Дата актуальности {currency_rates("usd")[1]}')
print(f'Тест None = {currency_rates("БЛАБЛАБЛА")}')