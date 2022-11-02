from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
    

mylist = [' ','O',' ']
shuffle_list(mylist)


def player_guess():
    guess = ' '
    
    while guess not in ['0','1','2']:
        guess = input("pick a number : 0,1,2")
    print(int(guess))    
    
player_guess()    

my_indx = player_guess()
print(my_indx)



def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("correct")
    else:
        print("wrong gueess")
        print(mylist)    
        
        
my_list = [' ','O',' ']
mixed_list = shuffle_list(mylist)
guess = player_guess()

check_guess(mixed_list,guess)
