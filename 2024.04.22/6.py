def orth_triangle(*, cathetus1: float = None, cathetus2: float = None, hypotenuse: float = None) -> float:
    if sum(arg is not None for arg in (cathetus1, cathetus2, hypotenuse)) != 2:
        return None
    
    if any(arg is not None and arg <= 0 for arg in (cathetus1, cathetus2, hypotenuse)):
        return None
    
    if hypotenuse is not None:
        if cathetus1 is not None and cathetus2 is not None:
            if hypotenuse <= min(cathetus1, cathetus2):
                return None
        elif cathetus1 is not None:
            if hypotenuse <= cathetus1:
                return None
        elif cathetus2 is not None:
            if hypotenuse <= cathetus2:
                return None
    elif cathetus1 is not None and cathetus2 is not None:
        if cathetus1 <= 0 or cathetus2 <= 0:
            return None
    
    if hypotenuse is not None and cathetus1 is not None:
        return (hypotenuse**2 - cathetus1**2)**0.5
    elif hypotenuse is not None and cathetus2 is not None:
        return (hypotenuse**2 - cathetus2**2)**0.5
    elif cathetus1 is not None and cathetus2 is not None:
        return (cathetus1**2 + cathetus2**2)**0.5

print(orth_triangle(cathetus1=3, hypotenuse=5))  
print(orth_triangle(cathetus1=8, cathetus2=15))  
print(orth_triangle(cathetus2=9, hypotenuse=3)) 

# Пример ручного теста:
# >>> orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None