sum = 0
count = 0
for i in range(1, 11):
    x = int(input('Enter number:\n'))
    if (x%4==0):
        sum+=x
        count += 1
print('Sum is ' +str(sum))
avg = sum/count
print('Average is '+str(avg))