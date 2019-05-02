num = int(input('Enter a number:\n'))
reverse = 0
while (num>0):
    reminder = num%10
    reverse = reminder
    num = num//10
    print(reverse, sep='', end=', ', flush=True)