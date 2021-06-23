"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"
"""


def num_translate(eng_num):
    eng_rus_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                    'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if eng_num in eng_rus_dict:
        return eng_rus_dict[str(eng_num)]
    else:
        return None


print(num_translate('on'))
print(num_translate('one'))
