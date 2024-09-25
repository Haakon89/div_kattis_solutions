test_cases=int(input())
for i in range(test_cases):
    grades_combined=0
    students_grades=input().split(" ")
    for grades in students_grades:    
        if grades == students_grades[0]:
            continue
        else:
            grades_combined+=int(grades)
    counter=0
    grade_average=grades_combined/float(students_grades[0])
    for grades in students_grades:
        if grades == students_grades[0]:
            continue
        elif int(grades)<=int(grade_average):
            continue
        else:
            counter+=1
    print(f"{'{:.3f}'.format(float(counter/int(students_grades[0])*100))}%")
                    


