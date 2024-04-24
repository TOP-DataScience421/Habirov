start_position = input("Введите координаты первой клетки (например, a1): ")
end_position = input("Введите координаты второй клетки (например, b2): ")

start_letter, start_number = start_position[0], int(start_position[1])
end_letter, end_number = end_position[0], int(end_position[1])

if start_letter == end_letter or start_number == end_number:
    print("да")
else:
    print("нет")

#Пример ввода 1:
#d4
#e4
#Пример вывода 1: да

#Пример ввода 2:
#a2
#c4
#Пример вывода 2: нет