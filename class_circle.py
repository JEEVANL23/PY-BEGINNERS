# abstract class

class formula():
    def __init__(self,l,b,h):
        self.l = l
        self.b = b
        self.h = h
        
    # abstract method    
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    def volume(self):
        pass
    
    
class rect(formula):
    
    def area(self):
        print(self.l  * self.b)
        
    def perimeter(self):
        print(2 * (self.l + self.b))
        
        
class cuboid(rect):
    
    def volume(self):
        print(self.b * self.h * self.b)            
        
        
        
my_formula = formula(2,3,4)

my_rect = rect(2,3,4)
my_cube = cuboid(2,3,4)


my_rect.area()
my_rect.perimeter()

my_cube.volume()
my_cube.area()
my_cube.perimeter()