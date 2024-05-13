def strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    if not (has_lower and has_upper):
        return False
    
    digit_count = sum(char.isdigit() for char in password)
    if digit_count < 2:
        return False
    
    has_special = any(not char.isalnum() for char in password)
    if not has_special:
        return False
    
    return True

def main():
    user_password = input("Введите пароль: ")
    print(strong_password(user_password))

if __name__ == "__main__":
    main()

# Пример ручного теста:
# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('password')
# False