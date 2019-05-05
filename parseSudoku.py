from math import *

def parseSudoku(grid):
    rowsList = []
    N = len(grid)
    for x in range(N):
        for y in range(N):
            for i in range(N):
                if grid[y][x] != 0:
                    rowsList.append({"value": grid[y][x],"column": x + 1, "row": y + 1, "box": int(floor((y) / (N / 3)) * (N / 3) + floor((x) / (N / 3)) + 1)})
                    break
                else:
                    rowsList.append({"value": i + 1,"column": x + 1, "row": y + 1, "box": int(floor((y) / (N / 3)) * (N / 3) + floor((x) / (N / 3)) + 1)})

    def getConstraint(keysToCheck):
        constraints = []
        for x in range(N):
            for y in range(N):
                constraints.append({keysToCheck[0]: x + 1, keysToCheck[1]: y + 1})

        constraintsMatrix = {}
        for i in range(len(rowsList)):
            row = rowsList[i]
            constraintRow = []
            for x in range(len(constraints)):
                constraint = constraints[x]
                if constraint[keysToCheck[0]] == row[keysToCheck[0]] and constraint[keysToCheck[1]] == row[keysToCheck[1]]:
                    constraintRow.append(True)
                else:
                    constraintRow.append(False)
            constraintsMatrix[str(row)] = constraintRow
        return constraints, constraintsMatrix

    rowColumnConstraints, rowColumnConstraintsMatrix = getConstraint(["row", "column"])
    rowNumberConstraints, rowNumberConstraintsMatrix = getConstraint(["row", "value"])
    columnNumberConstraints, columnNumberConstraintsMatrix = getConstraint(["column", "value"])
    boxNumberConstraints, boxNumberConstraintsMatrix = getConstraint(["box", "value"])

    constraints = rowColumnConstraints + rowNumberConstraints + columnNumberConstraints + boxNumberConstraints

    allConstraintsMatrix = {}
    for i in range(len(rowsList)):
        rowString = str(rowsList[i])
        allConstraintsMatrix[rowString] = rowColumnConstraintsMatrix[rowString] + rowNumberConstraintsMatrix[rowString] + columnNumberConstraintsMatrix[rowString] + boxNumberConstraintsMatrix[rowString]

    X = {}
    Y = {}

    for x in range(len(rowsList)):
        rowString = str(rowsList[x])
        Y[rowString] = []
        row = allConstraintsMatrix[rowString]
        for y in range(len(row)):
            if str(constraints[y]) not in X:
                X[str(constraints[y])] = []
            if row[y] == True:
                Y[rowString].append(str(constraints[y]))
                X[str(constraints[y])].append(rowString)

    return X, Y
