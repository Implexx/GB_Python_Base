"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере,
посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
"""
# На ум приходит много решений, можно использовать для парсинга какой то модуль xml, можно словарем,
# можно просто поиском в строках. Так как в условии сказано, что нужно реить только при помощи строк то:

# сначала решение используя только str
import requests
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
        # возвращаем результат в Decimal
        return Decimal(value.replace(',', '.'))
    # если кода нет в тексте возвращаем None
    else:
        return None


print(f'Курс Евро = {currency_rates("AUD")}')
print(f'Курс Доллара = {currency_rates("usd")}')
print(f'Тест None = {currency_rates("БЛАБЛАБЛА")}')






# # решение с использованием словаря
# import requests
# from decimal import Decimal
#
# # делаем запрос и получаем результат в виде строки
# url = 'http://www.cbr.ru/scripts/XML_daily.asp'
# request = requests.get(url)
# text = request.text
# # print(text)
# # убираем лишние теги в начале и конце для удобного парсинга
# xml_list = text.split('><')[2:-1]
#
# # print(xml_list)
# # print(len(xml_list))
#
#
# def currency_rates(code):
#     """
#     Вычисляет по введенному коду страны курс к рублю
#     :param code: str, код страны вида 'XXX'
#     :return: decimal, курс валюты в рублях
#     """
#     number_of_curr = round(len(xml_list) / 7)
#     # print(number_of_curr)
#     currencies = {}
#     for i in range(number_of_curr):
#         # print(i)
#         char_code = xml_list[i * 7 + 2].split('>')[1][:3]
#         value = xml_list[i * 7 + 5].split('>')[1].split('<')[0]
#         currency = {char_code: value}
#         # print(currency)
#         currencies.update(currency)
#     # print(currencies)
#     if code in list(currencies.keys()):
#         return Decimal(currencies[code].replace(',', '.'))
#     else:
#         return None
#
#
# print(f'Курс Евро = {currency_rates("EUR")}')
# print(f'Курс Доллара = {currency_rates("USD")}')


