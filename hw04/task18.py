num = int(input('Enter a number:\n'))
c = 0

while (num > 0):
    num = num//10   
    c += 1
print('Total digit is ' + str(c))