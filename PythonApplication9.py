import random
from sys import maxsize
  
def maxSubListSum(a,size): 
  
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
  
    for i in range(0,size): 
  
        max_ending_here += a[i] 
  
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
  
    print ("Sum is:" ,(max_so_far)) 
    
    subList = []
    for x in range(start,end+1):
        subList.append(a[x])
    
    print('Sub list is:' ,subList)            
  
#Creating list with random numbers
aList = []
for i in range(0, 10):
    x = random.randint(-10, 10)
    aList.append(x) 
print(aList)
maxSubListSum(aList,len(aList))
