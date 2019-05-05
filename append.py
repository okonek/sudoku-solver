import cv2
import os

fileDir = os.path.dirname(os.path.abspath(__file__))


def writeOnImage(sudokuSolution, sudokuUnsolved, additionalName = ""):
    image = cv2.imread(fileDir + "/sudoku-resized.png")
    cv2.imwrite(fileDir + "/outputs/sudoku" + additionalName + "-out.png", image)
    image = cv2.imread(fileDir + "/outputs/sudoku" + additionalName + "-out.png")
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 6
    fontColor = (0,0,0)
    lineType = 10

    cellDiemensions = int(1600 / 9)

    for x in range(9):
        for y in range(9):
            if sudokuSolution[y][x] != sudokuUnsolved[y][x]:
                bottomLeftCornerOfText = (cellDiemensions * x + 30,cellDiemensions * (y + 1) - 20)
                cv2.putText(image, str(sudokuSolution[y][x]), bottomLeftCornerOfText, font, fontScale, fontColor, lineType)



    cv2.imwrite(fileDir + "/outputs/sudoku" + additionalName + "-out.png", image)