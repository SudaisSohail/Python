import math as m
import timeit


def fib_rec(n) -> int:
    if n == 1 or n == 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)

def fib_formula(n):
    return round((pow(1 + m.sqrt(5), n) - pow((1 - m.sqrt(5)), n)) / (pow(2, n) * m.sqrt(5)))

print(timeit.timeit("fib_rec(25)", number=10, globals=globals()))
print(timeit.timeit("fib_formula(50)", number=1000, globals=globals()))
    
    





    
        

