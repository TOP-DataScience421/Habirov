number = int(input("Введите число: "))
divisor = 1  
sqrt_number = int(number**0.5)  

for i in range(2, sqrt_number + 1):  
    if number % i == 0:
        divisor += i
        if i != number // i:  
            divisor += number // i

print("Сумма всех делителей числа:", divisor)