n = int(input('Enter the range:\n'))

y = 0
for c in range(1, n+1):
    y = y + (c*c*c)
print(y)