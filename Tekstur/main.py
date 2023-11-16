import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
import os
from PIL import Image
from pathlib import Path
import time
import concurrent.futures
import joblib
import multiprocessing as mp

def read_img(imgpath):
    img = cv2.imread(imgpath)
    img = rgbtogray1(img)
    return img

def rgbtogray(listimg):
    for img in listimg:
        r,g,b = img[:,:,0],img[:,:,1],img[:,:,2]
        gray = 0.299*r + 0.587*g + 0.114*b
    return gray

    
def rgbtogray1(img):
    r, g, b = cv2.split(img)
    gray = 0.299*r + 0.587*g + 0.114*b
    gray = gray.astype(int)
    return gray

def tekstur(imgGray):
    matrixFrameWork = np.array([[0 for p in range(256)] for q in range(256)])
    for i in range(len(imgGray)):
        for j in range(len(imgGray[0])-1):
            isi1 = imgGray[i][j]
            isi2 = imgGray[i][j+1]
            if(isi1>=256):
                isi1=255
            if(isi2>=256):
                isi2=255
            matrixFrameWork[isi1][isi2] = matrixFrameWork[isi1][isi2] + 1

    transposeFrameWwork = matrixFrameWork.transpose()

    matrixGLCM = matrixFrameWork+transposeFrameWwork
    totalValue = matrixGLCM.sum()

    # for i in range(len(matrixFrameWork)):
    #     for j in range(len(matrixFrameWork[0])):
    #         matrixGLCM[i][j] = matrixFrameWork[i][j] + transposeFrameWwork[i][j]
    #         totalValue = totalValue + matrixGLCM[i][j]

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


image = cv2.imread(r"Algeo\Tubes\Tubes2\dataset\2222.jpg")
image = cv2.resize(image,(0,0),fx=0.5,fy=0.5)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)

imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)

imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray1 = rgbtogray1(image)
imgGray9 = rgbtogray1(image)



imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)
imgGray1 = tekstur(imgGray9)

# folder = "Algeo/Tubes/Tubes2/dataset"
# semua_file = [os.path.join(folder,file)for file in os.listdir(folder)if file.lower().endswith(('.png','.jpg','.jpeg'))]


# if __name__=='__main__':
#     num_processes = os.cpu_count()
#     #images8 = joblib.Parallel(n_jobs=num_processes)(joblib.delayed(read_img)(img)for img in semua_file)
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         images8 = list(executor.map(read_img,semua_file))
#     array = np.array(images8)
    # i = 0
    # total = 0
    # arrr1 = []
    # arrr2 = []
    # arrr3 = []
    # arrr4 = []
    # for file in semua_file:
    #     print(i)
    #     image2 = cv2.imread(os.path.join(folder,file))
    #     # imgGray2 = rgbtogray(image2)
    #     if(i%4==0):
    #         arrr1.append(image2)
    #     if(i%4==1):
    #         arrr2.append(image2)
    #     if(i%4==2):
    #         arrr3.append(image2)
    #     if(i%4==3):
    #         arrr4.append(image2)
        

    #     # arr2 = tekstur(imgGray2)

    #     # hasil = (arr1[0]*arr2[0] + arr1[1]*arr2[1] + arr1[2]*arr2[2])/(np.sqrt(arr1[0]*arr1[0] + arr1[1]*arr1[1] + arr1[2]*arr1[2]) * np.sqrt(arr2[0]*arr2[0] + arr2[1]*arr2[1] + arr2[2]*arr2[2]))
    #     # if(hasil>0.6):
    #     #     total = total + 1
    #     i = i+1
    # p1 = mp.Process(target=rgbtogray,args=(arrr1,))
    # p2 = mp.Process(target=rgbtogray,args=(arrr2,))
    # p3 = mp.Process(target=rgbtogray,args=(arrr3,))
    # p4 = mp.Process(target=rgbtogray,args=(arrr4,))
    # p4.start()
    # p3.start()
    # p1.start()
    # p2.start()
