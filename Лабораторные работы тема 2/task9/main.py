salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение






def right_number(a,b,c):
    d = 0
    while c > 1:
        a = a + a * b
        c -= 1
        d = d + a
    return d
need_money = right_number(spend,increase,months) - (salary * months) + 6000

print(round(need_money))

a = 6000
b = 0.03
c = 10
d = 0

