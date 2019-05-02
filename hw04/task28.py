num = int(input('Enter a number:\n'))
factCount = 0

for i in range(1, num+1):
    if (num % i == 0):
        factCount += i
print('The sum of all factors is '+str(factCount))