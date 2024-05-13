def countable_nouns(number: int, forms: tuple[str, str, str]) -> str:
    if number % 10 == 1 and number % 100 != 11:
        return forms[0]
    elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
        return forms[1]
    else:
        return forms[2]

print(countable_nouns(1, ("год", "года", "лет")))   
print(countable_nouns(2, ("год", "года", "лет")))   
print(countable_nouns(10, ("год", "года", "лет")))  
print(countable_nouns(12, ("год", "года", "лет"))) 
print(countable_nouns(22, ("год", "года", "лет")))

# Пример ручного теста:
# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'