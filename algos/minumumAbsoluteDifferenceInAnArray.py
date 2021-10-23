# 🚗🚗

arr = [3, -7, 0]


def minimumAbsoluteDifference(arr):
    absMin = []
    arr = sorted(arr)
    for i in range(1, len(arr)):
        # print(arr[i-1], arr[i])
        absMin.append(abs(arr[i-1] - arr[i]))
    return min(absMin)


minimumAbsoluteDifference(arr)
