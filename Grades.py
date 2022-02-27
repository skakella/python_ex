

print ('Welcome to GPA Calc')
print('Please Enter all letter Grades, one per line')
print('Enter blank to designate the End.')

points = {'A+':4.0,'A':4.0,'A-':3.75,'B+':3.5,'B-':3.25,'C+':3.0,'C':3.0,'C-':2.75,'D+':2.5,'D-':3.25,
            'E+':3.0,'E':3.0,'E-':2.75,'F':0.5}

#Bprint(points)
done = False
total_points = 0
total_grades = 0


while not done:
    grade = input()
    if grade.strip() == '':
        done = True
    elif grade not in points:
        print("Invalid grade '{0}' is Entered. Grade is ignored. ".format(grade))
    else:
        total_grades+=1
        total_points+=points[grade]

if total_grades > 0:
    print('Your GPA is {0}'.format(total_points/total_grades))
else:
    print("No grades calculated")