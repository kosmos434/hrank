# I hate this one 😡

arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
n = 10


def insertionSort1(n, arr):
    separator = " "
    stored = arr[-1]
    for i in range(n-1, 0, -1):
        curr = i-1
        if arr[curr] > stored:
            arr[curr+1] = arr[curr]
            print(separator.join(map(str, arr)))

            if curr == 0:
                arr[curr] = stored
                print(separator.join(map(str, arr)))
                break

        else:
            arr[curr+1] = stored
            print(separator.join(map(str, arr)))
            break


insertionSort1(n, arr)
