sum = 0
oddCount = 0
for i in range(1, 11):
    x = int(input('Enter number:\n'))
    if (x%2!=0):
        sum+=x
        oddCount += 1
print('Sum is ' +str(sum))
avg = sum/oddCount
print('Average is '+str(avg))