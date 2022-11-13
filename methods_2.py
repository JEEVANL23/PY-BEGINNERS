class dogs():
    
    species = 'mammal'
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
        

        
    # methods    
    def bark(self,num):
        print("wooof!!! my name is {} andn my breed is {} and age is {}".format(self.name,self.breed,num))   # when we pass name in the beginning it gets connected to self.name so !!!!!

x  = input()
y = input()
z = int(input())
     
my_dog = dogs(breed = x, name = y)   
     
a = my_dog.breed
b = my_dog.name
d = my_dog.species  


print(a)        
print(b)
print(d)

my_dog.bark(z)