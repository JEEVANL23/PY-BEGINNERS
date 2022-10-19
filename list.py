# defining a list
my_list = [1,2,3]
my_list_1 = ['string', 100 , 23.5]

print(len(my_list))
print(len(my_list_1))

my_list_2 = ['one', 'two', 'three']

print(my_list_2[0])         # list indexing
print(my_list_2[1:])        # list slicing




# list concatenation
my_list_3 = ['four', 'five', 'six']
my_list_4 = my_list_2 + my_list_3
print(my_list_4)

# indexing list when it is nested

a = [1,2,4,5,[3,6,9,12,15]]
bb  = a[2][1]
print(bb)


# list mutable
my_list_4[0] = "jeevan"
print(my_list_4)



# adding new element to list
my_list_4.append('seven')
print(my_list_4)




# poping an element from list
# .pop() removes only the las element in the list
my_list_4.pop()     # add index number to pop particular element
print(my_list_4)





# sorting the list 
new_list = [3,5,2,8,4,6,3,9,1,2]
print(new_list)
new_list.sort()
s = new_list
print(s)





# reversing a list
new_list.reverse()
p = new_list
print(p)