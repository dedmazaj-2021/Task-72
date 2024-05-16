from math import sqrt

def simple(number):
    if number % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(number)) + 1):
            if number % i == 0:
                return False
        else:
            return True

def factorization(number):
    i = 2
    factorization_set = set()
    while i*i <= number:
        while number % i == 0:
            factorization_set.add(i)
            number = number / i
        i = i + 1
    if number > 1:
        factorization_set.add(number)
    return factorization_set

def Euler_function(number):
    B = factorization(number)
    for j in B:
        number = number * (j - 1)/j
    return int(number)
    
Sum = 0

for i in range(2, 1000001):
    if simple(i):
        Z = i - 1
        Sum += Z
    else:
        Z = Euler_function(i)
        Sum += Z

print(Sum)



        
    

