n = float(input('Enter number:\n'))
sum = n
avg = 0
max = n
min = n
for i in range(1, 10):
    m = float(input('Enter number:\n'))
    if (m>max):
        max = m
    elif (m<min):
        min = m
    sum+=m
avg = sum / 10.0
print('Sum is ' + str(sum))
print('Average is '+ str(avg))
print('Maximum number is '+str(max))
print('Minimum number is '+ str(min))