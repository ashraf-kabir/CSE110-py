n = float(input('Enter number:\n'))
max = n
sum = n

for i in range(1, 19):
    m = float(input('Enter number:\n'))
    if (m > max):
        max = m
    sum += m
avg = sum / 20.0

print('Average '+str(avg))
print('Max '+str(max))