def numbers_strip(numbers: list[float], n: int = 1, copy: bool = False) -> list[float]:
    if copy:
        numbers = numbers.copy()
    
    for _ in range(n):
        numbers.remove(min(numbers))
        numbers.remove(max(numbers))
    
    return numbers

sample = [1, 2, 3, 4]
sample_stripped = numbers_strip(sample)
print(sample_stripped) 

sample = [10, 20, 30, 40, 50]
sample_stripped = numbers_strip(sample, 2, copy=True)
print(sample_stripped)  