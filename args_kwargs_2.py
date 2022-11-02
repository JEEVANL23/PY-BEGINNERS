def myfunc(**kwargs):
    print(kwargs)
    if 'a' in kwargs:
        print('my fruit is {}'.format(kwargs))
    else:
        print('no fruit found')
        
myfunc(a = 'apple',b = 'banana')                
     
        