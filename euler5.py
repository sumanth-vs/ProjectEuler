# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def evenly_divisible(n):
    lcm = 1
    for i in range(2, n):
        lcm = (lcm*i)//gcd(lcm, i)
    return lcm

def gcd(a, b):
    if a == 0 : 
        return b  
    return gcd(b%a, a)

print(evenly_divisible(20))



