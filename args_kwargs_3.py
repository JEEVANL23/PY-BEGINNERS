def myfun(*args,**kwargs):
    print('i will like {} {} '.format(args[1],kwargs['food']))
    print(args)
    print(kwargs)
    
myfun(10,15,20,fruit = 'apple', food = 'egg', desert = 'pastrey')    



