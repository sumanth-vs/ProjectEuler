def sum_of_digits(n):
    sum = 0
    while(n > 0):
        sum += n%10
        n //= 10
    return sum


def power_sum(index):
    n = 2**index
    return sum_of_digits(n)


index = 1000
print(power_sum(index))