# with parameters or arguments

def sample():
    print("hello world")
    
sample()        # calling the function to perform its operation    


# with paranmeters

def sam(name):
    print('jeevan' + name)
    print(f'hello {name}')

sam('kumar')
    
# with return keyword

def add_fn(n1,n2):
    return n1+n2

b = int(input())
c = int(input())
a = add_fn(b,c)
print(a)