# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


def multiples(n, t1, t2):
    sum = 0
    
    m=1
    while(t1*m < n):
        sum += t1*m
        m+=1
    
    m=1
    while(t2*m < n):
        sum += t2*m
        m+=1
    
    m=1
    while(t1*t2*m < n):
        sum -= t2*t1*m
        m+=1
    
    return sum
print(multiples(1000, 3, 5))


