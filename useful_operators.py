from random import shuffle


for i in range(3,10):       # range(start,stop,step)
    print(i)
    


for k in range(0,100,2):
    print(k)    
    
    
    
list1 = [1,2,3]
list2 = ['a','b','c']

for i,j in zip(list1,list2):
    print(i)
    print(j)    
    
    
a = [1,2,3,4,5]
print(min(a))

from random import shuffle
c = [1,2,3,4,5,6]
shuffle(c)
print(c)   