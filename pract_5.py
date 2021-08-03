# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

receipts = int(input("Введите количество выручки:"))
costs = int(input("Введите количество издержек:"))
if receipts > costs:
    profit = receipts - costs
    rent = profit / receipts
    print(f"Фирма работает с прибылью. Рентабельность составляет: {rent: .2f}")
    staff = int(input("Введите количество сотрудников:"))
    print(f"Прибыль фирмы в расчете на одного сотрудника: {profit / staff: .2f}")
else: print("Фирма работает в убыток")
