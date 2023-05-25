def gradingStudents(grades):
    for i,j in enumerate(grades):
        if j >= 38 and j%5 >= 3: 
            grades[i] = (j//5)*5 + 5
    return grades
