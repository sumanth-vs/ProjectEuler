import time, timeit

def pythagorean_triplets(req_sum_of_terms):#returns a, b, c : The pythagorean triplet for which a + b + c = req_sum_of_terms

    sum_of_terms = 0 # in the eucedian format(m, n)
    for m in range(2, req_sum_of_terms):
        for n in range(1, m):
            sum_of_terms = 2*m**2 + 2*m*n
            if sum_of_terms == req_sum_of_terms:
                return m**2 - n**2, 2*m*n, m**2 + n**2
            
    
    return -1, -1, -1


req_sum_of_terms = 1000

start = time.time()
a, b, c = pythagorean_triplets(req_sum_of_terms)
end = time.time()

print(a*b*c)
print(end-start)
