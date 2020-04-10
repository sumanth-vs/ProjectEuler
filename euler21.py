'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''
import math


def sumOfProperDivisors(number):
    proper_divisors = [1]
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i ==0 :
            proper_divisors.append(i)
            proper_divisors.append(number//i)

    # Removing duplicates that occur if two factors are the same(perfect sqares, eg 16 has 4, 4, so sum will be wrongly 19)
    proper_divisors = list(dict.fromkeys(proper_divisors))
    return sum(proper_divisors)


# print(properDivisors(220))

def checkProperDivisors(number):
    req_sum = []
    for i in range(number):
        n1 = sumOfProperDivisors(i)
        if sumOfProperDivisors(n1) == i and n1 != i:
            req_sum.append(i)
            req_sum.append(n1)
    return req_sum


number = 10001
list_of_amicable_numbers = list(dict.fromkeys(checkProperDivisors(number)))



print(list_of_amicable_numbers)
print(sum(list_of_amicable_numbers))