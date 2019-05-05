from parseSudoku import parseSudoku
from exact import solve

def solveSudoku(grid):  
    X, Y = parseSudoku(grid)
    finalSudoku = []
    solution = solve(X, Y)
    for x in range(9):
        finalSudoku.append([])
        for y in range(9):
            for i in range(81):
                if(eval(solution[i])["column"] == y + 1 and eval(solution[i])["row"] == x + 1):
                    finalSudoku[x].append(eval(solution[i])["value"])

    return finalSudoku