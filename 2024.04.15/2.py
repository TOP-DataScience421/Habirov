fruits = []

while True:
    fruit = input().strip()
    if fruit == "": 
        break
    fruits.append(fruit)

if len(fruits) == 1:
    print(fruits[0])
elif len(fruits) == 2:
    print(f"{fruits[0]} и {fruits[1]}")
else:
    result = ", ".join(fruits[:-1])  
    result += f" и {fruits[-1]}" 
    print(result)

# Пример ввода 1:
#     яблоко

# Пример вывода 1:
#     яблоко

# Пример ввода 2:
#     яблоко
#     груша

# Пример вывода 2:
#     яблоко и груша

# Пример ввода 3:
#     яблоко
#     груша
#     апельсин

# Пример вывода 3:
#     яблоко, груша и апельсин

# Пример ввода 4:
#     яблоко
#     груша
#     апельсин
#     лимон

# Пример вывода 4:
#     яблоко, груша, апельсин и лимон