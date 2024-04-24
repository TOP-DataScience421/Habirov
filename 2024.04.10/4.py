number = int(input("Введите число: "))

start = 10 ** (number - 1)
if number == 1:
    start = 2  
end = 10 ** number - 1

prime_count = 0

current_number = start
while current_number <= end:
    prime = True
    if current_number < 2:
        prime = False
    else:
        variabl = 2
        while variabl * variabl <= current_number:
            if current_number % variabl == 0:
                prime = False
                break
            variabl += 1

    if prime:
        prime_count += 1

    current_number += 1

print("Количество простых чисел среди всех значных чисел:", prime_count)

#Пример ввода: 3

#Пример вывода: 143