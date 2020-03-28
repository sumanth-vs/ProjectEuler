# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

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
    for ii in range(2, i//2):
        if i % ii == 0:
            return False
    print('{} is a prime number'.format(i))
    return True


print(factor(600851475143))
