list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
un=set(list_)

sum_ = sum(un)
len_ = len(un)

print(sum_)
print(len_)
print(round(sum_ / len_, 5))