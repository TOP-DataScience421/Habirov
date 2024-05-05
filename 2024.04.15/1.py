# Считываем адрес электронной почты из стандартного ввода
email = input().strip()

# Инициализируем переменные
at_found = False
dot_found = False
correct = False

# Проходим по символам электронной почты
for i, char in enumerate(email):
    if char == '@':
        at_found = True  # Найден символ '@'
        at_position = i  # Запоминаем позицию '@'
    elif char == '.' and at_found:
        # Проверяем, чтобы символ '.' находился после '@'
        dot_found = True
        if at_found and i > at_position:
            # Проверяем, что после '@' идет "gmail.com"
            domain = email[at_position + 1:]  # Берём часть строки после '@'
            if domain == "gmail.com":
                correct = True  # Адрес считается корректным
            break

# Выводим результат
if correct:
    print("да")
else:
    print("нет")