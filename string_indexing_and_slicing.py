my_string = 'hello world'
print(my_string)

# indexing

c = my_string[0]
print(c)

print(my_string[1])
                        # indexing starts from 0
d = my_string[-2]       # negative index starts from 0
print(d)


# slicing

e = my_string[2:]
print(e)

f = my_string[:3] # prints only till 2nd index
print(f)

g = my_string[1:5]
print(g)

h = my_string[1:6:2]            # JUMPING IN STEP SIZE OF 2 = 0 to 2, 1 to 3 like same oder depending on index
print(h)


# reversing the string 

i = my_string[::-1]
print(i)