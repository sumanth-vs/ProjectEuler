# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


def prime_factor(i):
    for ii in range(2, (i//2)+1):
        if i % ii == 0:
            return False
    #print('{} is a prime factor'.format(i))
    return True

count = 0;j=2
while count != 10001:
    if prime_factor(j):
        count +=1
        print(j)
    j+=1


#104743