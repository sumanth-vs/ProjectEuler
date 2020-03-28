# The sum of the squares of the first ten natural numbers is,

# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,

# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_square(n):
    sum_of_s = n*(n+1)*(2*n + 1)/6
    s_of_sum = (n*(n+1)/2)**2
    return s_of_sum - sum_of_s

n=100
print(sum_square(n))
