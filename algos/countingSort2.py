# 🔢


arr = [1, 1, 3, 2, 1]

# so tally up occourences
# and print that number of occourences


def countingSort(arr):
    printList = []
    listofzeros = [0] * 100
    for i in arr:
        listofzeros[i] += 1

    for i in range(len(listofzeros)):
        if listofzeros[i]:
            for j in range(listofzeros[i]):
                printList.append(i)

    return(printList)


countingSort(arr)
