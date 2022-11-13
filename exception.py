def ask_for_int():
    while True:
    
        try:
            res = int(input("enter the number \n"))
            print("the number you entered is ", res)
        except:
            print("thats not a number")
            
        else:
            print("yes thank you")
            break    
              
        finally:
            print("end of try/except/finally")    
        
ask_for_int()

