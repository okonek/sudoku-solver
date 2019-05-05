import copy

def solve(X, Y, solution = []):
    if len(list(X.keys())) == 0:
        return solution
    else:
        c = min(X, key = lambda a : len(X[a]))
        if len(X[c]) > 0:
            rows = X[c]
            for row in rows:
                solution.append(row)
                for column in copy.deepcopy(Y[row]):
                    for rowToRemove in copy.deepcopy(X[column]):
                        Y.pop(rowToRemove)
                        for i in range(len(X.keys())):
                            if rowToRemove in list(X.values())[i]:
                                X[list(X.keys())[i]].remove(rowToRemove)
                    
                    X.pop(column)
                    for i in range(len(list(Y.keys()))):
                        if column in list(Y.values())[i]:
                            Y[list(Y.keys())[i]].remove(column)                    
                    
                finalSolution = solve(X, Y, solution)
                if type(finalSolution) is list:
                    return finalSolution
            
                

