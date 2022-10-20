n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
print(a)

total = 0
for n in a:
    total = total + n
    print(total) # displays each number's addition result
print(total)   # displays total result     

