seconds = int(input('Enter seconds:\n'))
mins = seconds / 60
remSec = seconds % 60
hours = mins / 60
remMins = mins % 60

print(str(int(hours)) + ' hours, ' + str(int(remMins)) + ' mins, ' + str(remSec) + ' seconds')
