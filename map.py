def sq(num):
    return num**2



n = int(input('enter total numbers to be squared ; '))
my_list = []

for i in range(0,n):
    my_list.appned(i)
for i in map(sq,my_list):
    print(i)

a = list(map(sq,my_list))
print(a)    