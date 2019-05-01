sum = 0
for c in range(1, 601):
    if (c%7==0) and (c%9==0):
        sum = sum + c

print(sum)