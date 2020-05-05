MERGE SORT


'''
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 


'''








TOH









'''def hanoi(a, c, b, n):
	if n == 1:
		print("move from {} to {}".format(a, c))
	else:
		hanoi(a, b, c, n-1)
		hanoi(a, c, b, 1)
		hanoi(b, c, a, n-1)
	return
	
	
	
#hanoi('a', 'c', 'b', 3)



print("########################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$###################################################")


def gcd(m, n1):
	if(m==n1):
		print(m)
		return
	
	if m>n1:
		gcd(m-n1, n1)
	else:
		gcd(m, n1-m)
		

gcd(69,420)



print("########################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$###################################################")


def partB():
	flag1 = 0
	a =[]
	key = 2
	n2 = int(raw_input("Enter length of array"))
	for i in range(n):
		a.append(int(raw_input()))
	
	l1 = 0, h1 = n2-1, m1=0, m2
	
	while l1<=h1:
		m1= l1+h1 // 2
		
		ifa[m1] == key:
			m2=m1
			break
		elif a[m1] > key:
			h1 = m1-1
		else:
			l1 = m1+1		
	
	while a[m1] == key or a[m2] == key:
		if m1 == key:
			m1 -=m1
		if m2 == key:
			m2 -=m2
		
print(m1, m2, m2-m1)
	'''










TOPO SORT








'''

from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A recursive function used by topologicalSort 
    def topologicalSortUtil(self,v,visited,stack): 
  
        # Mark the current node as visited. 
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Push current vertex to stack which stores result 
        stack.insert(0,v) 
  
    # The function to do Topological Sort. It uses recursive  
    # topologicalSortUtil() 
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack =[] 
  
        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Print contents of the stack 
        print stack 
  
g= Graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
  
print "Following is a Topological Sort of the given graph"
g.topologicalSort() 

'''





DFS







'''
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
  
    # A function used by DFS 
    def DFSUtil(self, v, visited): 
  
        # Mark the current node as visited  
        # and print it 
        visited[v] = True
        print(v, end = ' ') 
  
        # Recur for all the vertices  
        # adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self, v): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        # Call the recursive helper function  
        # to print DFS traversal 
        self.DFSUtil(v, visited) 
  
# Driver code 
  
# Create a graph given  
# in the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print("Following is DFS from (starting from vertex 2)") 
g.DFS(2) 

'''






BFS





'''
from collections import defaultdict 
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        # Create a queue for BFS 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            print (s, end = " ") 
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
  
# Driver code 
  
# Create a graph given in 
# the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.BFS(2) 
'''







JOHNSON TROTTER






'''
import math

class Node:
	def __init__(self, val):
		self.val = val + 1
		self.dir = 'left'
		#self.pos = val
	
	def print_val(self):
		print(str(self.val) + " Pointing to " + str(self.dir))


def find_larg_mobile(arr):
	max_ind = None
	for i in range(0, len(arr)):
		if arr[i].dir == 'left' and i == 0:
			continue
		if arr[i].dir == 'right' and i == len(arr) - 1:
			continue
			
			
		if arr[i].dir == 'left' and arr[i].val > arr[i-1].val:
			if max_ind == None:
				max_ind = i
			elif arr[max_ind].val < arr[i].val:
				max_ind = i
				
		
		if arr[i].dir == 'right' and arr[i].val > arr[i+1].val:
			if max_ind == None:
				max_ind = i
			elif arr[max_ind].val < arr[i].val:
				max_ind = i
	return max_ind

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp
	
	return arr
			
def JT(n):
	#array = [Node(4, 'left'), Node(3, 'left'), Node(1, 'left'), Node(2, 'left')]
	array = []
	for i in range(0, n):
		array.append(Node(i))
		array[i].print_val()
	print("\n")
		
	#printing all perms
	for i in range(math.factorial(n) - 1):
		print(i+2)
		inx = find_larg_mobile(array)
		print(array[inx].val)
		#change big value dir
		if array[inx].val < n: 
			for i in range(0, n):
				if array[i].val > array[inx].val:
					if array[i].dir == 'left':
						array[i].dir = 'right'
					else:
						array[i].dir = 'left'
		HERE				
		if array[inx].dir == 'left':
			array = swap(array, inx, inx-1)  
			
		elif array[inx].dir == 'right':
			array = swap(array, inx, inx+1)
			
		#printing values each time
		for i in range(0, n):
			array[i].print_val()
		print("\n")
		
						
JT(6)
'''