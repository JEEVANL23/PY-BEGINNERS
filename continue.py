string = input()

for letter in string:
    if letter == 'a' :
        continue
    print(letter) # it will not print A
        
        
        # it will go to top of the current loop and 
        # it will not terminate the current loop, 
        # it will not execute rest of the code below it in the current loop