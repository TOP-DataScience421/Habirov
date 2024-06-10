from datetime import datetime

def logger(func):
    def wrapper(*args, **kwargs):
        # Получаем текущее время
        current_time = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
        
        # Выполняем функцию и получаем результат
        result = func(*args, **kwargs)
        
        # Открываем файл для добавления записи в конец
        with open('data/function_calls.log', 'a') as f:
            # Формируем строку для записи в журнал
            log_entry = f"{current_time} — {func.__name__}{args}{kwargs} -> {result}\n"
            
            # Записываем строку в файл
            f.write(log_entry)
        
        # Возвращаем результат выполнения функции
        return result
    
    return wrapper

# Пример использования
def div_round(num1, num2, *, digits=0):
    return round(num1 / num2, digits)

div_round = logger(div_round)

# Пример ручного теста: (cmd):
# D:\student\2023.05.28 > python -i 5.py
# >>> 
# >>> def div_round(num1, num2, *, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>> div_round(2, 3, digits=2)
# 0.67
# >>> ^Z