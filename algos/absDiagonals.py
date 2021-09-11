# abs diagonal 🤡🤡

def absDiag(arr):
    x = 0
    y = 0

    # first diagonal added
    for i in range(len(arr)):
        x += arr[i][i]

    # second diagonal added
    decrement = (len(arr) - 1)
    for i in range(len(arr)):
        y += arr[i][decrement]
        decrement -= 1

    # return the abs of differences
    print(x)
    print(y)
    print(abs(x - y))


    # a 3x3 array
A = [[11, 12, 2], [15, 6, 10], [10, 8, 5]]

absDiag(A)
