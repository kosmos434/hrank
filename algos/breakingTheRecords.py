# 🏀


scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]


def breakingRecords(scores):
    bestScore = [scores[0]]
    worstScore = [scores[0]]
    bestWorstTally = [0, 0]
    # Write your code here
    for index, item in enumerate(scores):
        if index == 0:
            continue  # just skip the first score
        if item > bestScore[0] and item not in bestScore:
            print(item)
            bestWorstTally[0] += 1
            bestScore[0] = item
            # print(f'new best of {item}')
        if item < worstScore[0] and item not in worstScore:
            bestWorstTally[1] += 1
            worstScore[0] = item
            # print(f'new worst of {item}')
    # print(bestWorstTally)
    # print(bestScore)
    # print(worstScore)
    return bestWorstTally


breakingRecords(scores)
