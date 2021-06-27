"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.
"""

from utils import currency_rates


if __name__ == '__main__':
    print(f'Курс Евро = {currency_rates("EUR")[0]} ... Дата актуальности {currency_rates("EUR")[1]}')
    print(f'Курс Евро = {currency_rates("usd")[0]} ... Дата актуальности {currency_rates("usd")[1]}')
    print(f'Курс Евро = {currency_rates("gBp")[0]} ... Дата актуальности {currency_rates("gBp")[1]}')
    print(f'Тест None = {currency_rates("БЛАБЛАБЛА")}')