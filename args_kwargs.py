from calendar import c
from tkinter import E


def myfunc(a,b):
    a = sum((a,b)) * 0.05
    print(a)


myfunc(6,4)



def fun(*args):
    a = sum(args) *0.06
    print(a)
    print(args)
    
a = int(input(" enter a :"))
b = int(input(" enter b :"))
c = int(input(" enter c :"))
d = int(input(" enter d :"))
e = int(input(" enter e :"))
    
fun(a,b,d,e)
fun(a,b,c)
fun(a,b,c,d,e)