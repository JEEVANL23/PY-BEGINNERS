def splice(mystring):
    if len(mystring)%2 ==0:
        return 'even'
    else:
        return 'odd'
    
names = ['andy','james','bond','jeevan','kumar']
a = list(map(splice,names))
print(a)    