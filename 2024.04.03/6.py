start_position = input("Введите клетку 1 ")
end_position = input("Введите клетку 2 ")


letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
number = ['1', '2', '3', '4', '5', '6', '7', '8']

movea1 = letter.index(start_position[0]) + 1
moveb1 = number.index(start_position[1]) + 1

movea2 = letter.index(end_position[0]) + 1
moveb2 = number.index(end_position[1]) + 1


course_a = abs(movea1 - movea2)
course_b= abs(moveb1 - moveb2)

if course_a <= 1 and course_b <= 1:
    print('да')
else:
    print('нет')

#Пример ввода 1:
#Введите клетку 1 g3
#Введите клетку 2 f2
#Пример вывода 1: да

#Пример ввода 2:
#Введите клетку 1 c6
#Введите клетку 2 d4
#Пример ввода 2: нет