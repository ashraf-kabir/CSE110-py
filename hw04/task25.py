num = int(input('Enter a number:\n'))
factorCount = 0
for i in range(1, num+1):
    if num % i == 0:
        factorCount += 1
print(factorCount)