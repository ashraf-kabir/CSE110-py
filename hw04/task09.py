sum1 = 0
sum2 = 0
for c in range(1, 601):
    if (c%7==0):
        sum1 = sum1 + c
    elif (c%9==0):
        sum2 = sum2 + c
print(sum1)
print(sum2)