# abstract class with inheritence an polymorphism

class animal():
    
    def __init__(self,name):
        self.name = name
                
    def speak(self):
        raise ("derieved class implement this abstract method ")

class dog(animal):
    
    def speak(self):
        print(" wooof !!! and my name is {}".format(self.name))


class cat(animal):
    
    def speak(self):
        print(" meow !!! and my name is {}".format(self.name))

my_animal = animal("fred")
my_dog = dog('joe')
my_dog.speak()
my_cat = cat('sam')
my_cat.speak()
