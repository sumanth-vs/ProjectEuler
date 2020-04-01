# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''
def fibo(n):

    if n==0:
        return 0
    if n==1:
        return 1

    return fibo(n-1) + fibo(n-2)

i=3
sum = 0
while fibo(i) < (4 * (10**6)):
    term = fibo(i)
    if(term %2 == 0):
        sum += term
    i +=1
print(sum)

'''

# Better Implementation -- Reading the overview of Project Euler INCOMPLETE



target = 5


def Fibonacci(target):

    sum = 0
    a, b = 1, 1

    while b < target:
        sum += b
        h = a+b
        a = b
        b = h
    return sum

print(Fibonacci(target))