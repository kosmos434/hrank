# grade time 🎓

# every student gets a grade 0-100
# less than 40 is failing

# rules are:
# if less than 3 from next 5er (85, 90, 95), then round up to that 5er
# BUT if less than 38: no rounding ya dingus

# SO grade = 84 becomes 85
# grade = 29 = 29
# grade = 57 = 57  <-- diff must be less than 3 to round up


grades = [73, 67, 38, 33]


def gradingStudents(grades):
    graded = []
    for i in grades:
        graded.append(grader(i))
    return(graded)


def grader(grade):
    mod = grade % 5
    # return num if less than 40
    if grade < 38:
        return grade
    if mod < 3:
        return grade
    if mod >= 3:
        return grade + (5-mod)


gradingStudents(grades)
