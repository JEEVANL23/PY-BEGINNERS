def even(num):
    return num%2 == 0


mynum = [1,2,3,4,5,6]

for i in filter(even,mynum):
    print(i)