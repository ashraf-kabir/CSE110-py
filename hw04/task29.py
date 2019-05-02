n = int(input('Enter a number:\n'))
sum = 0
for i in range(1,n):
    if (n%i==0):
        sum += i
if n == sum:
    print('Your input is a PERFECT number')
else:
    print('Your input is NOT A PERFECT number')