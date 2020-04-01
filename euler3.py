# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
import time, timeit, math


def factor(n):
    prime_list = []
    #replace with sqrt, works for large values
    # for i in range(2,int(math.sqrt(n))):
    #     if n % i == 0:
    #         if prime_factor(i):
    #             prime_list.append(i)


    # ALETERNATE ALGO:
    i=2    
    while n != 1:
        if prime_factor(i):
            if n % i == 0:
                n = n//i
                print('{} is a PRIME FACTOR'.format(i))
                prime_list.append(i)
                i=2
                continue
        i +=1
    
    return max(prime_list)

def prime_factor(i):
    for ii in range(2, int(math.sqrt(i) + 1)):
        if i % ii == 0:
            return False
    print('{} is a prime number'.format(i))
    return True

number = 286
start = time.time()
# print(factor(number))
end  = time.time()

print(end-start)



''' Instead of finding primes then checking if they are factors, chack if they are factors and then check for prime'''


mylist = []


star1 = time.time()
for i in range(2, int(math.sqrt(number) + 1)):
    if number % i == 0:         
        if prime_factor(i):             # Is i a prime?
            mylist.append(i)
            
        if prime_factor(number//i):     # number//i is also a factor, so is number//i a prime? 
            mylist.append(number//i)

print(max(mylist))

end1 = time.time()

print(end1-star1)



''' EULER METHOD


n=35742549198872617291353508656626642567*2
if n % 2==0:

    lastFactor=2
    n=n // 2
while n % 2==0:
    n=n // 2
else:
    lastFactor=1
    factor=3
    maxFactor= n


while n>1 and factor<=maxFactor:
    if n % factor==0:
        n=n // factor
        lastFactor=factor
while n % factor==0:
    n=n // factor
    maxFactor= n
    factor=factor+2
if n==1:
    print(lastFactor)
else:
    print(n)
    '''