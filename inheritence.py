# base class

class animal():
    
    def __init__(self):
        self.age = 10
        print("animal created at age {}".format(self.age))
        
    def who_am_i(self):
        print("i am an animal")
        
    def eat(self):
        print("i am animal and eating")        
        
 # inheriting
class dog(animal):
    
    def __init__(self):
        animal.__init__(self)
        print("dog created")
        
    def eat(self):
        print("i am dog and eating")    
        
    def who_am_i(self):
        print("i am dog")   
    
    def bark(self):
        print("whoooof !!!")     
            
# object or instance

my_animal = animal()        # init's function willl be executed
my_dog = dog()              # init's function will be executed

my_dog.eat()
my_dog.who_am_i()
my_animal.who_am_i()
my_animal.eat()
my_dog.bark()




             
                