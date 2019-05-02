n = int(input('Enter starting number:\n'))
m = int(input('Enter ending number:\n'))

primeC = 0
perfectC = 0
i = n
for i in range(n<=m+1):
    sum = 0
    factorC = 0
    d = 1
    for d in range(1, d<n):
        if (n%d==0):
            sum+=d
            factorC+=1
    

    if factorC==2:
        primeC+=1
    if sum==n:
        perfectC+=1
print(primeC)
print(perfectC)
