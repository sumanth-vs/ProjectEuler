def collatz(num):

    count_array = []

    for i in range(1, num+1):
        n = i
        count = 1
        
        while(n != 1):
            if n % 2 == 0:
                n /= 2
            else:
                n = 3*n + 1
            count += 1
        
        count_array.append(count)
    
    return count_array


num = 1000000
count_array = collatz(num)

print(count_array.index(max(count_array))+1)



'''
3, 10, 5, 16, 8, 4, 2, 1

'''