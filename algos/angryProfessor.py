# 👨‍🏫💢

'''
Function Description

Complete the angryProfessor function in the editor below. It must return YES if class is cancelled, or NO otherwise.

angryProfessor has the following parameter(s):

    int k: the threshold number of students
    int a[n]: the arrival times of the 

    students

Returns

    string: either YES or NO

'''

k = 2
a = [-1, 0, 1, 2]


def angryProfessor(k, a):

    presentStudents = 0
    for i in a:
        if i <= 0:
            presentStudents = presentStudents + 1
    if presentStudents >= k:
        return("NO")  # as in "NO, class is not cancelled"
    else:
        return("YES")


angryProfessor(k, a)
