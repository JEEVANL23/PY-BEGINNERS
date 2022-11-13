class sample():     # creation of the class
    print('jeevan')

my_sample = sample()        # my_sample is instance of class sample







class dogs():
    
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        
        # expect boolean
        self.spots = spots

x  = input()
y = input()
z = input()   
     
my_dog = dogs(breed = x, name = y,spots = z)   
     
a = my_dog.breed
b = my_dog.name
c = my_dog.spots       

print(a)        
print(b)
print(c)