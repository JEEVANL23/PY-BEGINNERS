# declaration

my_dict = {'1': "hello", '2': "world", '3': "this", '4': "is", '5': "python", '6': "program"}
print(my_dict['1'])

# dict holding different data type

my_dict_1 = {'k1': "hello", 'k2': [1,2,3,'a','b','c'], 'k3':{'insidekey':100},'k4':['a','b','c']}
print(my_dict_1['k3']['insidekey'])     # nested dict
print(my_dict_1['k2'][1])               # inside list

my_dict_3 = my_dict_1['k2']
print(my_dict_3)


f = my_dict_1['k4'][2].upper()
print(f)

# adding new element
a = {'11':'1234567', '13':'123456', '15':'12345'}
a['16'] = '1234'
print(a)

a['11'] = 'new value'
print(a)