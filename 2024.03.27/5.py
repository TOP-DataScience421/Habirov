milescomp = int(input("Введите целую часть числа миль: "))
milespart = int(input("Введите дробную часть числа миль: "))

result = float(milescomp) + float(milespart) / 10
kilometers = result * 1.61

kilometers_rounded = round(kilometers, 1)

print(f"{milescomp}.{milespart} миль = {kilometers_rounded:.1f} км")

#Пример ввода:
#Введите целую часть числа миль: 15
#Введите дробную часть числа миль: 7

#Пример вывода:
#Вывод = (15.7 миль = 25.3 км)