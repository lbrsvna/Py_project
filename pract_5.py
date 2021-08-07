# Реализовать структуру «Рейтинг»,
# представляющую собой набор натуральных чисел,
# который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [8, 7, 5, 2]
print (f'Рейтинг фильма: {my_list}')
grade = int(input('Добавьте свою оценку:'))
for el in range(len(my_list)):
    if my_list [el] == grade:
        my_list.insert(el+1,grade)
        break
    elif my_list[0]< grade:
        my_list.insert (0,grade)
    elif my_list[-1]> grade:
        my_list.append(grade)
    elif my_list[el] > grade and my_list[el + 1] < grade:
        my_list.insert(el + 1, grade)
print(f'Рейтинг обновлён:{my_list}')