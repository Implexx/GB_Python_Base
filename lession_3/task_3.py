"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
 thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?
"""

names = ("Иван", "Мария", "Петр", "Илья", "Максим", 'Алена', 'Иннокентий')


def thesaurus(employees):
    """
    Функция для создания словаря с первыми буквами имен и именами, начинающимися на эту букву
    :param employees: list or tuple - список имен
    :return: dict - вида {"М": ["Мария"]}
    """
    name_dict = {}
    # перебираем каждое имя в списке
    for name in employees:
        temp_list = [name]
        char = name[0]
        # сравниваем первую букву выбранного имени со всеми именами в списке. Если совпадает, группируем
        for i in range(len(employees)):
            if employees[i][0] == char and employees[i] not in temp_list:
                temp_list.append(employees[i])
        # после группировки заносим в словарь ключ Имя, значение Список имен
        name_dict.update({char: temp_list})
    # Сортируем словарь по ключам по алфавиту
    sorted_dict = {}
    sorted_keys = sorted(name_dict, key=name_dict.get)
    for i in sorted_keys:
        sorted_dict[i] = name_dict[i]
    return sorted_dict


print(thesaurus(names))

