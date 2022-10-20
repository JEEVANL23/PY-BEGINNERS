# for loop

num = [1,2,3]

for i in num:
    print(i)
    print("hello")
    
 
 

n = int(input('enter the total numbers to be in the list '))    
a = []
for i in range(0,n):
    a.append(int(input()))
    
key = int(input("enter key to be found in the list "))
for k in a:
    if key == k:
        print('found')
        
    else:
        print("not found")        
    