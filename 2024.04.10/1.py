numbers = []

while True:
    user_input = input("Введите число: ")
    number = int(user_input)
    if number % 7 == 0:
        numbers.append(number)
    else:
        break

result = " ".join(map(str, reversed(numbers)))
print(result)

#Пример ввода:
#Введите число: 7
#Введите число: 14
#Введите число: 28
#Введите число: 5

#Пример вывода:28 14 7