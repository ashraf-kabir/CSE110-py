mark = float(input('Enter the mark of quiz:\n'))
currentScale = float(input('Enter the current scale:\n'))
targetScale = float(input('Enter the target scale:\n'))

z = (mark*targetScale)/currentScale

print('The target scale mark is '+str(z))