# list comprehensive - the method of creating a list quickly


# using string

my_list = input('enter name ')

new_list = [l for l in my_list]
print(new_list)


# using integer

num = [x for x in range(0,11)]
print(num)


# squaring the number
n = int(input('enter the total range of number to be squared'))
a = [n**2 for n in range(0,n)]
print(a)


m = [f if f%2 == 0  else 'ODD' for f in range(0,11)]
print(m)