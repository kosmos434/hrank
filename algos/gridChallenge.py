# 💪

grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']


def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))

    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            if ord(grid[i][j]) < ord(grid[i-1][j]):
                return("NO")
    return("YES")


gridChallenge(grid)
