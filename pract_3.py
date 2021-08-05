# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {0 : 'зима', 1 : 'весна', 2 : 'лето', 3 : 'осень'}
number = int(input("Введите номер месяца: "))
if number ==1 or number == 12 or number == 2:
        print(seasons_dict.get(0))
        print(seasons_list[0])
elif number == 3 or number == 4 or number ==5:
    print(seasons_dict.get(1))
    print(seasons_list[1])
elif number == 6 or number == 7 or number == 8:
    print(seasons_dict.get(2))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(3))
    print(seasons_list[3])
else:
        print("Введено неверное значение")
