class car:
    def __init__(self):
        pass
    
    def start(self,name):
        self.name = name
        pass
    
    def cost(self,num):
        self.num = num
# inherited from class car , no need of initializing constructor for derieved class
class innova(car):
    def start(name):
        print('hello i am {}'.format(name))
        
    def cost(num):
        print('my cost is {}'.format(num))        
# overridden the start method
class swift:
    def __init__(self,name):
        self.name = name
        pass
    
    def start(name):
        print('i am {}'.format(name))
        
        
        
# creating the objects / instances of the classess        
my_innova = innova
my_swift = swift


# calling the method of the classess
my_innova.start('innova')
my_innova.cost(1000)

my_swift.start('swift')        