class circle():
    
    # class object attribute
    pi = 3.14
    
    
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * circle.pi # coa can be referenced by both class name and self 
        
        
        ## method
    def get_circumference(self):
        print(self.radius * self.pi *2)


# instance
        
my_circle = circle(30)      # overiding the default value
my_circle.get_circumference()            
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)

## my_circle is an instance of the class circle
## using instance we can call attributes, method, class object attribute,and parameters

# we use self to use the variables which is not defined in the same method