"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков:
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
 get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово
можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""
import random


origin_nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
origin_adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
origin_adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n=1, flag=1):
    """
    Функция создает желаемое количество шуток из заданных наборов слов
    :param n: 1<=n<=5 количество шуток
    :param flag: flag=0 для запрета повтора слов
    :return: list с полученными шутками
    """
    nouns = origin_nouns.copy()
    adverbs = origin_adverbs.copy()
    adjectives = origin_adjectives.copy()
    count_nouns = len(nouns)
    count_adv = len(adverbs)
    count_adj = len(adjectives)
    jokes = []
    # если флаг не блокирует повтор
    if flag == 1:
        # цикл по количеству шуток
        for i in range(n):
            # формируем список шуток беря рандомное слово из трех списков слов
            jokes.append(f'{nouns[random.randint(1, count_nouns - 1)]} {adverbs[random.randint(1, count_adv - 1)]} '
                         f'{adjectives[random.randint(1, count_adj - 1)]}')
        return jokes
    # флаг !=1, то заблокировать повтор
    else:
        # при запрете на повтор слова из списка не может быть количество шуток больше чем самый короткий список
        if n > min(count_nouns, count_adv, count_adj):
            return 'Вы ввели слишком большое значение шуток, при заблокированном повторе слов'
        for i in range(n):
            if i < n - 1:
                random_noun = nouns[random.randint(1, count_nouns - 1)]
                nouns.remove(random_noun)
                random_adv = adverbs[random.randint(1, count_adv - 1)]
                adverbs.remove(random_adv)
                random_adj = adjectives[random.randint(1, count_adj - 1)]
                adjectives.remove(random_adj)
                jokes.append(f'{random_noun} {random_adv} {random_adj}')
                count_nouns -= 1
                count_adv -= 1
                count_adj -= 1
            else:
                jokes.append(f'{nouns[0]} {adverbs[0]} {adjectives[0]}')
                nouns.clear()
                adverbs.clear()
                adjectives.clear()
        return jokes


print('Тест с включенным флагом на запрет повторов:\n', get_jokes(5, 0))
print('Тест с выключенным флагом:\n', get_jokes(7))
