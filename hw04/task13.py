n = int(input('Enter a range:\n'))
sum = 0
for c in range(1, n+1):
    if (c%2!=0):
        sum+=c
print('Sum (of odd) is '+str(sum))