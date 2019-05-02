num = int(input('Enter a number:\n'))
count = 0
reverse = 0
while (num>0):
    reminder = num%10
    reverse = reminder
    num = num//10
    count += 1
    print(reverse, sep='', end=', ', flush=True)
print('\n')
print(count)

x = 10 ** (count - 1)

print(x)