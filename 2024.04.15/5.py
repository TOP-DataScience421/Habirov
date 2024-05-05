scores_letters = {
    'а': 1, 'в': 1, 'е': 1, 'и': 1, 'н': 1, 'о': 1, 'р': 1, 'с': 1, 'т': 1,
    'д': 2, 'к': 2, 'л': 2, 'м': 2, 'п': 2, 'у': 2,
    'б': 3, 'г': 3, 'ь': 3, 'я': 3,
    'й': 4, 'ы': 4,
    'ж': 5, 'з': 5, 'х': 5, 'ц': 5, 'ч': 5,
    'ф': 8, 'ш': 8, 'э': 8, 'ю': 8,
    'щ': 10,
    'ъ': 15
}

word = input().strip().lower()  

total_score = 0
for char in word:
    if char in scores_letters:
        total_score += scores_letters[char] 
    else:
        print("! invalid character in input !")  
        exit(1)  

print(total_score)  

# Пример ввода:
# синхрофазотрон

# Пример вывода:
# 29