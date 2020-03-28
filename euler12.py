import math



def triangle_number(req_number_of_factors):
    num = 0
    for i in range(10000, 100000):
        #print(i)
        num = i*(i+1)//2
        if num_of_factors(num, req_number_of_factors):
            return num


def num_of_factors(num, req_number_of_factors):
    count = 2
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i==0:
            count += 2
    #print(count)
    if count > req_number_of_factors:
        return True
    return False



req_number_of_factors = 500
print(triangle_number(req_number_of_factors))