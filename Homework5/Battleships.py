def battleship(matrix):
    count = 0
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == ".":
                continue
            if i > 0 and matrix[i - 1][j] == "X":
                continue
            if j > 0 and matrix[i][j - 1] == "X":
                continue
            count += 1
    return count
matrix = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
print(battleship(matrix))
