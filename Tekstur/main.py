import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

image = cv2.imread(r"dataset\0.jpg")
image2 = cv2.imread(r"dataset\1999.jpg")


input_matrix = np.array([[0, 0, 1],
                          [1, 2, 3],
                          [2, 3, 2]])

def rgbtogray(img):
    r,g,b = img[:,:,0],img[:,:,1],img[:,:,2]
    gray = 0.29*r + 0.587*g + 0.114*b
    return gray
imgGray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imgGray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
#imgGray1 = rgbtogray(image)
#imgGray2 = rgbtogray(image2)

def tekstur(imgGray):
    matrixFrameWork = [[0 for i in range(256)] for j in range(256)]
    #imgGray = [[int(elem)+1 for elem in baris] for baris in imgGray3]
    for i in range(len(imgGray)):
        for j in range(len(imgGray[0])-1):
            isi1 = imgGray[i][j]
            isi2 = imgGray[i][j+1]
            matrixFrameWork[isi1][isi2] = matrixFrameWork[isi1][isi2] + 1

    transposeFrameWwork = [[row[i] for row in matrixFrameWork] for i in range(len(matrixFrameWork))]

    totalValue = 0
    matrixGLCM = [[0 for i in range(256)] for j in range(256)]
    for i in range(len(matrixFrameWork)):
        for j in range(len(matrixFrameWork[0])):
            matrixGLCM[i][j] = matrixFrameWork[i][j] + transposeFrameWwork[i][j]
            totalValue = totalValue + matrixGLCM[i][j]

    glcmNorm = [[0 for i in range(256)] for j in range(256)]
    for i in range(len(matrixFrameWork)):
        for j in range(len(matrixFrameWork[0])):
            glcmNorm[i][j] = matrixGLCM[i][j]/totalValue


    contrast = 0
    dissimilarity = 0
    homogeneity = 0
    entropy = 0
    for i in range(len(matrixFrameWork)):
        for j in range(len(matrixFrameWork[0])):
            contrast = contrast + glcmNorm[i][j] * (i-j) *(i-j)
            dissimilarity = dissimilarity + glcmNorm[i][j] * abs(i-j)
            homogeneity = homogeneity + glcmNorm[i][j] / (1 + (i-j) *(i-j))
            if(glcmNorm[i][j]>0):
                entropy = entropy + glcmNorm[i][j] * math.log10(glcmNorm[i][j])
    entropy = entropy * (-1)
    array = [contrast,homogeneity,entropy]
    return array

arr1 = tekstur(imgGray1)
arr2 = tekstur(imgGray2)

print(arr1)
print(arr2)

hasil = (arr1[0]*arr2[0] + arr1[1]*arr2[1] + arr1[2]*arr2[2])/ (math.sqrt(arr1[0]*arr1[0] + arr1[1]*arr1[1] + arr1[2]*arr1[2]) * math.sqrt(arr2[0]*arr2[0] + arr2[1]*arr2[1] + arr2[2]*arr2[2]))
print(hasil)