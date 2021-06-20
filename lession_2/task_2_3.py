"""
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее,
чем может сначала показаться.
"""

origin_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# подсчитываем сколько чисел встречается в списке
count = 0
for elem in origin_list:
    if not elem.isalpha():
        count += 1
# print(count)

index = 0

# прогоняем цикл столько раз, сколько встретилось чисел
while count > 0:
    # перебираем список
    for i in range(index, len(origin_list)):
        # если это цифра без знаков
        if not origin_list[i].isalpha() and origin_list[i].isdigit():
            # запонляем нолями
            origin_list[i] = origin_list[i].zfill(2)
            # вставляем в начальный список кавычки спереди и сзади найденного числа
            origin_list.insert(i, '"')
            origin_list.insert(i + 2, '"')
            # ведем подсчет индекса когда встретилось число, следующий цикл начинаем со следующего элемента
            index = index + i + 3
            break
        # если это число со знаками спереди
        if not origin_list[i].isalpha() and not origin_list[i].isdigit():
            temp = ''
            # отделяем знак и добавляем к числу ноли, затем объединяем знак и число с нолями
            for _char in origin_list[i]:
                if not _char.isdigit():
                    temp += _char
                else:
                    origin_list[i] = temp + _char.zfill(2)
            origin_list.insert(i, '"')
            origin_list.insert(i + 2, '"')
            index = index + i + 3
            break
    count -= 1

print('Список после преобразований получился:')
print(origin_list)

# Собираем строку из списка с пробелами
_string = ''
for index in range(len(origin_list)):
    if origin_list[index].isalpha():
        _string += origin_list[index] + ' '
    elif not origin_list[index].isalpha() and origin_list[index] != '"':
        _string += origin_list[index - 1] + origin_list[index] + origin_list[index + 1] + ' '

print('итоговая строка получилась:')
print(_string)
