# mini max sum time 🤠

arr = [7, 69, 2, 221, 8974]


def miniMaxSum(arr):
    arr.sort()
    nmin = sum(arr[:4])
    # Write your code here
    nmax = sum(arr[1:])
    print(nmin, nmax)


miniMaxSum(arr)
