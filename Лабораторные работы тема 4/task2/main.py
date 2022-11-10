def get_count_char(str_):
    dict = []

    split = str_.lower()
    split = list(split)
    for letter in split:
        if letter.isalpha():
            dict.extend(letter)

    new_dict = {i: dict.count(i) for i in dict}
    return new_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
