num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

total = 0
if num1 > 0:
    total += num1
if num2 > 0:
    total += num2
if num3 > 0:
    total += num3

print(total)

#Пример ввода:
#5
#-6
#5
#Пример вывода: 10