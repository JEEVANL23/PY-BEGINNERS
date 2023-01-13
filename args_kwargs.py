from calendar import c
from tkinter import E


def myfunc(a,b):
    a = sum((a,b)) * 0.05
    print(a)


myfunc(6,4)



def fun(*args):
    a = sum(args) * 2
    print(a)
    print(args)
    
fun(1,2,3,4)
fun(5,6,7)
fun(8,9,10,11,12,13)