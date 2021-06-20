"""
5. Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]
* Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
(например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
(должно быть 07 коп или 00 коп).

* Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).
* Создать новый список, содержащий те же цены, но отсортированные по убыванию.
* Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""

import random

# создаем список из случайных чисел
numbers = list(round(random.uniform(0, 10), 2) for i in range(10))
print(f'Исходный список:\n{numbers}')


# Было много повторяющегося кода, поэтому вынес кусок с приведением списка в строку в функцию.
# Знаю, пока рано, но не хотелось увеличивать количество строк кода
def prices_in_string(some_list):
    """
    Преобразует из исходного списка в красивую строку с ценами
    :param some_list: Список цен
    :return: Строка с красивыми ценами
    """
    _char_list = []
    for _num in some_list:
        _string = str(_num).split('.')
        _string[1] = _string[1].ljust(2, '0')
        _price = f'{_string[0]} руб {_string[1]} коп'
        _char_list.append(_price)
    return ', '.join(_char_list)


print(f'Результат основного задания:\n{prices_in_string(numbers)}\n---------')

print('Доказываем, что при сортировке id элемента не меняется:')
print(f'id списка до сортировки = {id(numbers)}')
temp_num = numbers[0]
print(f'id 0-го числа списка {temp_num} до сортировки = {id(numbers[0])}\n-')
numbers.sort()
print(f'id списка после сортировки = {id(numbers)}')
position_of_temp_num = numbers.index(temp_num)
print(f'id {position_of_temp_num}-го числа списка {temp_num} после сортировки = {id(numbers[position_of_temp_num])}\n-')

print(f'Результат первого задания со звездочкой(сортировка не создавая новый список):\n{prices_in_string(numbers)}'
      f'\n---------')

# Создаем новый список и передаем ему элементы исходного в обратном порядке
reversed_list = []
for elem in reversed(numbers):
    reversed_list.append(elem)

print(f'Результат второго задания со звездочкой(сортировка в обратном порядке создав новый список):'
      f'\n{prices_in_string(reversed_list)}\n---------')

# Вычисление то 5 цен. Берем 5 первых цен из отсортированного списка и переворачиваем его для отображения по возрастанию
max_price = []
for index in range(5):
    max_price.append(reversed_list[index])
max_price.sort()
print(f'Результат третьего задания со звездочкой(вывести 5 топ цен):\n{prices_in_string(max_price)}\n---------')


# оставил кусок первоначального кода когда сделал первое задание и первое со звездочкой, чтоб показать,
# что дублирование - плохо смотрится. Поэтому вынес в функцию


# numb = 1.47
# list_1 = str(numb).split('.')
# if len(list_1[1]) < 2:
#     list_1[1] = list_1[1].zfill(2)
#     print(list_1)
# price = f'{list_1[0]} руб {list_1[1]} коп'
# print(price)
# char_list = []
# for num in numbers:
#     _string = str(num).split('.')
#     _string[1].zfill(2)
#     price = f'{_string[0]} руб {_string[1]} коп'
#     char_list.append(price)
# result = ', '.join(char_list)
# print(f'Результат основного задания:\n{result}\n------')
#
# char_list.clear()
# temp_num = numbers[0]
# print(f'id 0-го числа списка {temp_num} до сортировки = {id(numbers[0])}')
# numbers.sort()
# position_of_temp_num = numbers.index(temp_num)
# print(f'id {position_of_temp_num}-го числа списка {temp_num} после сортировки = {id(numbers[position_of_temp_num])}')
# for num in numbers:
#     _string = str(num).split('.')
#     _string[1].zfill(2)
#     price = f'{_string[0]} руб {_string[1]} коп'
#     char_list.append(price)
# result = ', '.join(char_list)
# print(f'Результат задания со звездочкой:\n{result}\n------')


