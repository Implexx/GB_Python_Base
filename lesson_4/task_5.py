"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Убедиться,
 что ничего лишнего не происходит.
5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
> python task_4_5.py USD
75.18, 2020-09-05
"""
from utils import currency_rates


if __name__ == '__main__':
    import sys

    exit(print(f'Курс Евро = {currency_rates(sys.argv[1])[0]} ... Дата актуальности {currency_rates(sys.argv[1])[1]}'))
