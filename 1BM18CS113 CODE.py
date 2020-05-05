import time, timeit

# find proper position to insert element using Binary Search
def BS(array, val, s, e): 
    if s == e: 
        if array[s] > val: 
            return s 
        else: 
            return s+1
  

    if s > e: 
        return s 
  
    mid = (s+e)//2
    if array[mid] < val: 
        return BS(array, val, mid+1, e) 
    elif array[mid] > val: 
        return BS(array, val, s, mid-1) 
    else: 
        return mid 

#regular Insertion Sort, but using Binary Search to find the right place to insert
def InsertionSort(array): 
    for i in range(1, len(array)): 
        val = array[i] 
        j = BS(array, val, 0, i-1) 
        array = array[:j] + [val] + array[j:i] + array[i+1:] 
    return array 



array = [x for x in range(10000, 0, -1)]
# array = [200, -5, 69, 9, 8, 34, 67, -2, 0, 20, -9]
print('**********************************************************\n\n')
print('array before sorting:\n',array, '\n\n')
print("Sorted array:") 
start = time.time()
print(InsertionSort(array))
end = time.time()

print('\n\nTIME TAKEN:', end-start)



