# defining tuple and list

tup = (1,2,3,4)
my_list = [1,2,3]

# knowing the type 

print(type(tup))
print(type(my_list))

# length
print(len(tup))
print(len(my_list))

# different data types

tup1 = [1,2,'three','four']
print(tup1)

# slicing and indexing

a = tup1[1:]
print(a)

b = tup1[2]
print(b)

# counting 
c = ['a', 'b', 'a','d',1,2,3,2,1]
d = c.count('a')
print(d)

e = c.count(1)
print(e)


# indexing

f = c.index('a')
print(f)


my_list[0] = "new"
print(my_list)