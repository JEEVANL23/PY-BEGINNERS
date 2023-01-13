x = 'global scope'
def fun1():
    x = 'enclosed scope'
    
    def fun2():
        x = "local scope"
        print(x)
        
    print(x)
    
    fun2()
    
fun1()

print(x)