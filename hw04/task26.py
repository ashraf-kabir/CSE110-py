num = int(input('Enter a number:\n'))
primeCount = 0

for i in range(2, num):
    if (num % i == 0):
        primeCount += 1

if primeCount == 0:
    print('Your input is a PRIME number')
else:
    print('Your input is NOT A PRIME number')