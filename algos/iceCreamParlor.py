# 🍨

m = 4
arr = [2, 2, 4, 3]


def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            # print(arr[i], arr[j])
            if arr[i] + arr[j] == m:
                return([i+1, j+1])  # 1 indexed


icecreamParlor(m, arr)
