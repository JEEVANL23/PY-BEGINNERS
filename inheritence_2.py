class base():
    
    def __init__(self):
        pass        
    def new(self):
        print("hello")
              
class derieved(base):
         
    def __init__(self):
        base.__init__(self)
        print("world")
        
        
        
my_base = base()
my_base.new()
my_der = derieved()
my_der.new()
