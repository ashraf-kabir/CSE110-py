n = int(input('Enter starting number:\n'))
m = int(input('Enter ending number:\n'))

primeC = 0
perfectC = 0
i = n
while(n<=m):
    sum = 0
    factorC = 0

    for div in range(1, div<n):
        if (n%div==0):
            sum+=div
            factorC+=1
    

    if factorC==2:z
        primeC+=1
    if sum==n:
        perfectC+=1
print(primeC)
print(perfectC)
