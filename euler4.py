# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def iterate(num):
    a = []; count= 0 
    for i in range(num, 100, -1):
        for j in range(i, 100, -1):
            count += 1
            if palindrome(i*j):
                a.append(i*j)
    return max(a), count           
                
    

def palindrome(n):
    temp=n
    sum = 0
    while n!=0:
        sum = sum*10 + n%10
        n = n//10
    if sum == temp:
        return True
    else:
        return False



print(iterate(999))

