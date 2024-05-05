# Считываем два списка из входных данных
list = list(map(int, input().strip().split()))
part = list(map(int, input().strip().split()))

# Проверка, является ли sublist подсписком main_list
is_sublist = False

# Если sublist пустой, он считается подсписком любого списка
if not part:
    is_sublist = True
else:
    # Проходим по main_list и ищем начало подсписка
    for i in range(len(list) - len(part) + 1):
        # Проверяем, совпадает ли срез main_list с sublist
        if list[i:i + len(part)] == part:
            is_sublist = True
            break

# Выводим результат
print("да" if is_sublist else "нет")

# Пример ввода 1:
# 1 2 3 4
# 1 2

# Пример вывода 1:
# да

# Пример ввода 2:
# 1 2 3 4
# 2 4

# Пример вывода 2:
# нет