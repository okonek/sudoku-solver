from PIL import Image
import cv2
import numpy
import sys
import os
import pytesseract
from main import solveSudoku
from append import writeOnImage

fileDir = os.path.dirname(os.path.abspath(__file__))

sudokuIndex = ""
if len(sys.argv) > 1:
    sudokuIndex = str(sys.argv[1])

sudokuSrc = fileDir + "/sources/sudoku"+sudokuIndex+".png"
resizedSrc = fileDir + "/sudoku-resized.png"

sudokuSourceImage = Image.open(sudokuSrc)
sudokuResized = sudokuSourceImage.resize((1600, 1600), Image.NEAREST)
sudokuResized.save(resizedSrc)

image = cv2.imread(resizedSrc)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)
outerBox = cv2.bitwise_not(thresh)

cellDiemensions = int(1600 / 9)

def crop_image(img,tol=0):
    mask = img>tol
    return img[numpy.ix_(mask.any(1),mask.any(0))]

sudokuGrid = []

for x in range(9):
    sudokuGrid.append([])
    for y in range(9):
        sudokuGrid[x].append(0)

for x in range(9):
    for y in range(9):
        cropped = outerBox[cellDiemensions * y + 20:cellDiemensions * (y + 1) - 20, cellDiemensions * x + 20: cellDiemensions * (x + 1) - 20]
        cropped = crop_image(cropped, 10)
        if len(cropped) > 0:
            sudokuGrid[y][x] = int(pytesseract.image_to_string(Image.fromarray(cropped), config="-c tessedit_char_whitelist=123456789 --oem 0 --psm 13"))
        else:
            sudokuGrid[y][x] = 0
        

writeOnImage(solveSudoku(sudokuGrid), sudokuGrid, sudokuIndex)
os.remove(resizedSrc)

