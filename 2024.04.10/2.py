number = int(input("Введите количество чисел: "))
total = 0

for i in range(number):
    number = int(input("Введите число: "))
    if number > 0:
        total += number

print("Сумма положительных чисел:", total)

#Пример ввода:
#Введите количество чисел: 5
#Введите число: 9
#Введите число: 2
#Введите число: 7
#Введите число: -6
#Введите число: 1

#Пример вывода:
#Сумма положительных чисел: 19