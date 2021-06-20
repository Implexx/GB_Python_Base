# Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов», задаем число
# 2 — получаем «2 процента». Вывести все склонения для проверки.

number = int(input('введите число процентов от 0 до 20 = '))

if number == 1:
    print(f'Вы ввели {number} процент')
elif number == 2 or number == 3 or number == 4:
    print(f'Вы ввели {number} процента')
elif number > 4 or number == 0:
    print(f'Вы ввели {number} процентов')

print('Для проверки вывод всех вариантов от 1 до 20:')
for number in range(21):
    if number == 1:
        print(f'{number} процент')
    elif number == 2 or number == 3 or number == 4:
        print(f'{number} процента')
    elif number > 4 or number == 0:
        print(f'{number} процентов')