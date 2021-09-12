# 👧👧👧

# so consecutive indices a[0],a[1],a[2]
# difference between them is equal to d

arr = [2, 2, 3, 4, 5]
d = 1


def beautifulTriplets(d, arr):
    possibles = 0

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] - arr[i] > d:
                break
            if arr[j] - arr[i] == d:
                for k in range(j, len(arr)):
                    if arr[k] - arr[j] > d:
                        break
                    if arr[k] - arr[j] == d:
                        possibles += 1

    return(possibles)


beautifulTriplets(d, arr)
