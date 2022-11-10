money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение


money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0

while money_capital > 0:

    spend += (spend * increase * month) + (spend * month)
    money_capital = (money_capital + salary) - (spend)
    month += 1

print(month)
