# .format()


m = "this is a string{}".format(' used in python string ')
print(m)


n = 'the {} {} {}'.format('fox', 'brown', 'quick')
print(n)


n = 'the {2} {1} {0}'.format('fox', 'brown', 'quick')   # insert the index vavle inside the barckets to get that string first
print(n)


n = 'the {c} {b} {a}'.format(a='fox', b='brown', c='quick') # we can perform variable assignment also
print(n)


# f-strings

k = ' jeevan'
print(f'hello {k} ')


l = "jeevan"
d = 5
print(f'{l} is {d} years old')