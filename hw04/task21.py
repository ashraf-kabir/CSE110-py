num = int(input('Enter a number:\n'))
count, m, temp = 0, 0, num
while (temp>0):
    temp = temp // 10
    count += 1
prod = 10 ** (count - 1)
x = prod
result = ''
while (num>0):
    m = num / int(prod)
    num %= int(prod)
    prod = prod//10
    print(int(m), sep='', end=', ', flush=True)
print('\n')
print(count)
print(x)
