import math


def grid(dimension):
    number_of_routes = nCr(dimension**2, dimension)
    return number_of_routes


def nCr(n, r):
    prod = 1
    for i in range(n, n-r, -1):
        prod *= i

    return float(prod/math.factorial(r))


# print(nCr(4, 2))

dimension = 20
answer = grid(dimension)
print(f'{answer:.0f}')

