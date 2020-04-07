# # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# # Find the sum of all the primes below two million.
import math
import timeit, time

def is_prime(i):
    for ii in range(2, int(math.sqrt(i)+1)):
        if i%ii == 0:
            return False
    return True

'''

def prime_sum(n):
    odd_numbers = [(2*x +1) for x in range(1, n//2)]
    sum = 0
    for i in odd_numbers:
        if is_prime(i):
            sum += i
    return sum+2

n = 200
start = time.time()
print(prime_sum(n))
end = time.time()
print(end-start)
'''



''' USE THE SCRATCH METHOD''' # DOES NOT WORK
'''
import time, timeit



num = int(input())
array = [x for x in range(2, num)]

def scratcher(array, num):
    for i in array:
        if i*i < num:
            remove(i*i, array)
            for j in range(i+1, num//i + 1):
                remove(i*j, array)

    return array




def remove(num_to_remove, array):
    try:
        array.remove(num_to_remove)
    except:
        pass



start = time.time()
print(sum(scratcher(array, num)))
end = time.time()
print(end-start)Yj]]

'''

n = 200000
prime_array = [2, 3]
for i in range(6, n, 6):
    if is_prime(i-1):
        prime_array.append(i-1)
    if is_prime(i+1):
        prime_array.append(i+1)

print((prime_array))







