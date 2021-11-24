# 🗺

grid = ['989', '191', '111']


def cavityMap(grid):
    for row in range(1, len(grid)-1):
        # print(row)
        for col in range(1, len(grid[row])-1):
            # this column
            curr = grid[row][col]
            # prev and next columns
            left = grid[row][col - 1]
            right = grid[row][col + 1]
            # above and below columns
            up = grid[row-1][col]
            down = grid[row+1][col]

            adjacents = [left, right, up, down]

            if all(el < curr for el in adjacents):
                # print('yay')
                abc = grid[row][:col]
                xyz = grid[row][col+1:]
                grid[row] = grid[row][:col] + 'X' + grid[row][col+1:]

    return(grid)


cavityMap(grid)
