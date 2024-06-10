def math_function_resolver(func, *args, res_to_str=False):
    """
    Вычисляет округленные значения для различных математических функций.

    Аргументы:
    func: callable
        Математическая функция, которую необходимо вычислить для значений x.
    args: tuple
        Значения x для математической функции.
    res_to_str: bool, optional
        Флаг, указывающий, нужно ли возвращать значения как строки (по умолчанию False).

    Возвращает:
    list
        Список с округленными значениями математической функции для переданных значений x.
        Значения могут быть целыми числами или строками в зависимости от значения res_to_str.
    """
    if res_to_str:
        return [str(round(func(x))) for x in args]
    else:
        return [round(func(x)) for x in args]

# Ручные тесты
print(math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10)))
print(math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10)))
print(math_function_resolver(lambda x: 2.72**x, *range(1, 10), res_to_str=True))

# Пример ручного теста:
# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# [2, 3, 4, 4, 4, 5, 6, 6, 6]
# >>>
# >>> math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
# [2, 1, 0, 0, 0, -1, -2, -2, -2]
# >>>
# >>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), res_to_str=True)
# ['3', '7', '20', '55', '149', '405', '1101', '2996', '8149']
