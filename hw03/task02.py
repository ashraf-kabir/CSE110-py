x = int(input('Enter your marks:\n'))

if (x >= 90) and (x <= 100):
    print('A')

elif (x >= 80) and (x <= 89):
    print('B')

elif (x >= 70) and (x <= 79):
    print('C')

elif (x >= 60) and (x <= 69):
    print('D')

elif (x >= 50) and (x <= 59):
    print('E')

elif (x <= 50) and (x >= 0):
    print('F')

else:
    print('Invalid input')
