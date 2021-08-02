# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369

number= int(input("Введите любое число:"))
number_2 = int(str(number) + str(number))
number_3 = int(str(number) + str(number) + str(number))
sum = int(number + number_2 + number_3)
print(f'Сумма чисел равна: {sum}')