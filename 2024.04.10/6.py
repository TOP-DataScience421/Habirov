ticket_number = input("Введите номер билета: ")

if len(ticket_number) != 6:
    print("Ошибка: номер билета должен содержать шесть цифр!")
else:
    digits = [int(digit) for digit in ticket_number]

    first_half_sum = sum(digits[:3])
    second_half_sum = sum(digits[3:])

    if first_half_sum == second_half_sum:
        print("да")
    else:
        print("нет")

#Пример ввода 1:
#183534

#Пример вывода 1:
#да

#Пример ввода 2:
#401367

#Пример вывода 2:
#нет