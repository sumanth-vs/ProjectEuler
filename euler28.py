def spiral(number):
    
    summ = 1
    mul = 2
    count = 0

    for i in range(3, number**2, mul):
        print(mul)
        summ += i
        count += 1
        if count == 4:
            count = 0
            mul += 2

    return summ

# print(spiral(5))
number  = 5
for i in range(3, number**2):
    for j in range(4):
        sum += j