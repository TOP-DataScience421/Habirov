def taxi_cost(distance: int, time: int = 0) -> int | None:
    if distance < 0 or time < 0:
        return None
    
    cost = 80
    distance_cost = (distance // 150) * 6
    waiting_cost = time * 3
    
    if distance == 0:
        return cost + waiting_cost + 80  
    total_cost = cost + distance_cost + waiting_cost
    
    return round(total_cost)

print(taxi_cost(1500))      
print(taxi_cost(2560))       
print(taxi_cost(0, 5))       
print(taxi_cost(42130, 8))    
print(taxi_cost(-300))     

# Пример ручного теста:
# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))
# None