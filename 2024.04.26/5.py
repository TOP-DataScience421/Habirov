def logger(func_obj: 'function') -> 'function':
    """Функция-декоратор. Выводит в консоль следующие параметры декорируемой функции:
    <название функции>(<*значения произвольного кол-ва позиционных аргументов через запятую>, <ключ = значение произвольного кол-ва ключевых элементов>) (-> <возвращаемое значение декорируемой функции>) ИЛИ ( .. <Названиие и описание любого перехваченного внутри декорируемой функции исключения>"""
   
    # Функция-обертка
    def wrapper(*args, **kwargs) -> 'any':
        # Вносим название декорируемой функции в строку для вывода - logger_str
        logger_str = str(func_obj.__name__) + '('
        n = 0
        
        # Сначала итеррируемся по позиционным и/или позиционно ключевым параметрам
        for n in range(0, func_obj.__code__.co_posonlyargcount): 
            # Пытаемся записать значения переданных аргументов в logger_str
            try:
                logger_str += str(args[n]) + ', '
            # Если вылетает исключение IndexError, значит следующие аргументы имеют стандартные значения, дописываем в logger_str стандартные значения
            except IndexError:
                logger_str += str(func_obj.__defaults__[n]) + ', '
        # Далее итеррируемся по ключевым аргументам
        for k in range(0, func_obj.__code__.co_kwonlyargcount): 
            # Записываем название ключа для текущей итеррации в переменную для удобства
            l_key = func_obj.__code__.co_varnames[k + n + 1]
            # Пытаемся записать значения переданных ключевых элементов в logger_str
            try:
                logger_str += str(l_key) + ' = ' + str(kwargs[l_key]) + ', '
            # Если вылетает исключение KeyError, значит следующие аргументы имеют стандартные значения
            except KeyError:
                logger_str += str(l_key) + ' = ' + str(func_obj.__kwdefaults__[l_key]) + ', '
        # Чтобы не усложнять код выше, вырезаем лишние символы после всех итерраций
        logger_str = logger_str.rstrip(', ') + ')'
        
        # Пытаемся вызвать декоррируемую функцию с произвольным набором аргументов
        try:
            logger_str += ' -> ' + str(func_obj(*args, **kwargs))
        # В случае врозникновения любого исключения, дописываем его название и описание в logger_str
        except Exception as exception:
            logger_str += ' .. ' + str(type(exception)).strip("<>class' ") + ': ' + str(exception)
        
        # Выводим в консоль получившуюся строку logger_str
        print(logger_str)
    
    return wrapper
            

# Тестовая функция. Для простоты тестов написана в файле а не в консоли            
def divider(a: float | int = 1, b: float | int = 2, /, *, to_str = False, to_print = False) -> float | str | None:

    if to_str:
        c = str(a / b)
    else:
        c = a / b
        
    if to_print:
        print(c)
    else:
        return float(c)

divider = logger(divider)

# Пример ручного теста:
# >>> def div_round(num1, num2, *, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>> 
# >>> 
# >>> div_round(1, 3, digits=2)
# div_round(1, 3, digits=2) -> 0.33
# 0.33
# >>> div_round(7, 2)
# div_round(7, 2, digits=0) -> 4.0
# 4.0
# >>> div_round(5, 0)
# div_round(5, 0, digits=0) .. ZeroDivisionError: division by zero
# >>> 

