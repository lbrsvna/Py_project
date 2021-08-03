#Пользователь вводит время в секундах.
#Переведите время в часы, минуты, секунды
#и выведите в формате чч:мм:сс.
#Используйте форматирование строк.

b = 24
time = int(input('Введите время в секундах:'))

hours = int(time // 3600)

if hours > b:
    print("Неверное значение")
if hours == b:
     hours=0

residue = time % 3600
minutes = residue // 60
seconds = residue % 60

print(f"Ваше время в формате: %02d: %02d: %02d" % (hours, minutes, seconds))