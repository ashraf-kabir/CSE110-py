num = int(input('Enter a number:\n'))
count = 0
m = 0
temp = num

while (temp>0):
    temp = temp // 10
    count += 1
prod = 10 ** (count - 1)
x = prod

while (num>0):
    m = num / int(prod)
    num %= int(prod)
    prod = prod//10
    print(int(m), sep='', end=', ', flush=True)
print('\n')
print(count)
print(x)
