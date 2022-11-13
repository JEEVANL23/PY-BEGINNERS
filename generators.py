def cubes(n):
    for x in range(n):
        yield x**3
        
print(list(cubes(5)))        