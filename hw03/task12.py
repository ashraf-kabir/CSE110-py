grade1 = float(input('Enter the grade of CSE110:\n'))
grade2 = float(input('Enter the grade of ENG091:\n'))
grade3 = float(input('Enter the grade of MAT110:\n'))
grade4 = float(input('Enter the grade of PHY111:\n'))

credit1 = 3.0
credit2 = 0.0
credit3 = 3.0
credit4 = 3.0

GPA = (grade1*credit1 + grade2*credit2 + grade3*credit3 + grade4*credit4)/(credit1+credit2+credit3+credit4)

print('Your GPA is ' + str(GPA))