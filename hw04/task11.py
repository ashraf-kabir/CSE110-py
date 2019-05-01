sum = 0
evenCount = 0
for i in range(1, 11):
    x = int(input('Enter number:\n'))
    if (x%2==0):
        sum+=x
        evenCount += 1
print('Sum is ' +str(sum))
avg = sum/evenCount
print('Average is '+str(avg))