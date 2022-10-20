n = int(input())
a = []
for  i in range(0,n):
    a.append(int(input()))
print(a)

for num in a:
    if num % 2 == 0:
        print(num)
    else:
        print('odd number')    
       