"""
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными,
 начинающимися с заглавной буквы. Например:
 num_translate_adv("One")
"Один"
 num_translate_adv("two")
"два"
"""


def num_translate_adv(eng_num):
    eng_rus_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                    'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    flag = 0
    if eng_num.istitle():
        flag += 1
        eng_num = eng_num.lower()
    if eng_num in eng_rus_dict:
        if flag == 0:
            return eng_rus_dict[str(eng_num)]
        else:
            return eng_rus_dict[str(eng_num)].capitalize()
    else:
        return None


print(num_translate_adv('on'))
print(num_translate_adv('one'))
print(num_translate_adv('One'))

