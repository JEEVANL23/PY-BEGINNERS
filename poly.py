class dog():
    def __init__(self):
        pass
        
    def speak(self,name):
        self.name = name
        print(self.name + " says woof") 
        
class cat():
    
    def __init__(self):
        pass
        
    def speak(self,name):
        self.name = name
        print(self.name + " says meow ")
            
nick = dog()
felix = cat()

nick.speak("nick")
felix.speak("felix")
