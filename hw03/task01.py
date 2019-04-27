x = int(input('Enter your marks:\n'))

if (x >= 0) and (x < 50):
    print('You shall not pass')

elif (x >= 50) and (x <= 100):
    print('Pass')

elif (x < 0) or (x > 100):
    print('Wrong input')
