def first(a):
    def sec():
        print("world")
    a()
    return sec    
    
    
@first
def third():
    print("hello")
    
    
third()        