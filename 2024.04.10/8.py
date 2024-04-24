number = int(input("Введите число n: "))

fibonacci_sequence = [1, 1]

while len(fibonacci_sequence) < number:
    next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_fib)

print(' '.join(map(str, fibonacci_sequence[:number])))

#Пример ввода: 17

#Пример вывода: 
#1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597