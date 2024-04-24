telegram_text = input("Введите текст телеграммы: ")

count_symbols = sum(1 for char in telegram_text if char.isalnum())

sum_kopecks = count_symbols * 30

rubles = sum_kopecks // 100
kopecks = sum_kopecks % 100

print(f"{rubles} руб. {kopecks} коп.")

#Пример ввода: грузите апельсины бочках братья карамазовы

#Пример вывода: 11 руб. 40 коп.