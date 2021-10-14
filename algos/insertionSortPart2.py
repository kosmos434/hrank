#

n = 6
arr = [1, 4, 3, 5, 6, 2]


def insertionSort2(n, arr):
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] > arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
        print(*arr)


insertionSort2(n, arr)
