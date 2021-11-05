# 🔢

arr = [4, 5, 3, 7, 2]


def quickSort(arr):
    left = []
    right = []
    pivot = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > pivot:
            right.append(arr[i])
        if arr[i] < pivot:
            left.append(arr[i])

    return(left + [pivot] + right)


quickSort(arr)
