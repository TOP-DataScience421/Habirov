input_str = input().strip()

if input_str.startswith("0b"):
    input_str = input_str[2:]
elif input_str.startswith("b"):
    input_str = input_str[1:]

binary = True
for char in input_str:
    if char != '0' and char != '1':
        binary = False
        break

if binary:
    print("да")
else:
    print("нет")

# Пример ввода:
# 1b0101

# Пример вывода:
# нет

# Пример ввода:
# 0101

# Пример вывода:
# нет