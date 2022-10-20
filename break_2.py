x = 0
n = int(input('enter the total number '))
m = int(input('enter the number at which loop should be terminated '))

while x < n:
    if x == m:
        break
    print(x)
    x += 1