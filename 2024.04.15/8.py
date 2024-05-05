list = input().split('; ')
i = 0


while i < len(list):
    value = 1
    
    for key in range(i+1, len(list)):
        if list[i] == list[key]:
            # breakpoint()
            list[key] = ''.join(list[key].partition('.')[0] + '_' + str(value) + '.' + list[key].partition('.')[2])
            value += 1
    i += 1
   
list = sorted(list)
for elem in list:
    print(elem)

# Пример ввода:
# 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz

# Пример вывода:
# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main.py
# src.tar.gz
# src_2.tar.gz
