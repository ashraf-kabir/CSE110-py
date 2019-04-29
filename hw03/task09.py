num1 = float(input('Enter the first number:\n'))
num2 = float(input('Enter the second number:\n'))
num3 = float(input('Enter the third number:\n'))

if (num1 > num2) and (num1 > num3):
    print('First number ('+ str(num1) + ') is the largest')
elif (num2 > num1) and (num2 > num3):
    print('Second number ('+ str(num2) + ') is the largest')
else:
    print('Third number ('+ str(num3) + ') is the largest')