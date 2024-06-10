def repeat(repeats=2):
    # Внешний декоратор repeat принимает количество повторений repeats и возвращает внутренний декоратор decorator
    def decorator(func):
        # Внутренний декоратор decorator принимает функцию func и возвращает обертку wrap
        def wrap(*args, **kwargs):
            # Обертка wrap вызывает декорируемую функцию func repeats раз
            for _ in range(repeats):
                func(*args, **kwargs)
        return wrap
    return decorator

# Пример использования декоратора
@repeat(4)  # Применяем декоратор repeat к функции testing_function с аргументом repeats=4
def testing_function():
    print('python')

#пример ручного теста
#>>> @repeat(num_times=4)
#... def testing_function():
#...     print('python')
#...
#>>> testing_function()
#python
#python
#python
#python