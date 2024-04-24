numerator = int(input("Введите числитель: "))
denominator = int(input("Введите знаменатель: "))

if numerator % denominator == 0:
    print(f"{numerator} делится на {denominator} нацело")
    print(f"частное: {numerator // denominator}")
else:
    print(f"{numerator} не делится на {denominator} нацело")
    print(f"неполное частное: {numerator // denominator}")
    print(f"остаток: {numerator % denominator}")


#Пример ввода 1:
#Ввведите целое число - делимое: 10
#Введите целое число - делитель: 5

#Пример вывода 1:
#10 делится на 5 нацело
#частное: 2

#Пример ввода 2:
#Ввведите целое число - делимое: 18
#Введите целое число - делитель: 5

#Пример вывода 2:
#18 не делится на  нацело
#неполное частное: 3
#остаток: 3