n = int(input('Enter the range:\n'))

y = 0
for c in range(1, n+1):
    if (c%2==0):
        y = y - (c*c)
    else:
        y = y + (c*c)
print(y)