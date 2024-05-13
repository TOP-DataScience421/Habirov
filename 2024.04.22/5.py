def central_tendency(first: float, second: float, *numbers: float) -> dict[str, float]:
    numbers = (first, second) + numbers  # Добавляем первые два числа к остальным
    n = len(numbers)
    sorted_numbers = sorted(numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]

    arithmetic_mean = sum(numbers) / n
    geometric_mean = 1
    for num in numbers:
        geometric_mean *= num
    geometric_mean **= (1 / n)
    harmonic_mean = n / sum(1 / num for num in numbers)
    
    return {'median': median, 'arithmetic': arithmetic_mean, 'geometric': geometric_mean, 'harmonic': harmonic_mean}

print(central_tendency(1, 2, 3, 4))
sample = [1, 2, 3, 4, 5]
print(central_tendency(*sample))

# Пример ручного теста:
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.2133638394006434, 'harmonic': 1.9200000000000004}
# >>>
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}