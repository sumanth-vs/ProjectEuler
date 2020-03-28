import math
from euler16 import sum_of_digits


def sum_of_factorial(n):
    facorial = math.factorial(n)
    return sum_of_digits(facorial)


num = 100
print(sum_of_factorial(num))