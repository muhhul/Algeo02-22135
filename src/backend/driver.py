import numpy as np
import matplotlib.pyplot as plt
import cv2
import csv
import math
import os
import pandas as pd
from PIL import Image
from pathlib import Path
import multiprocessing as mp
    
def rgbtogray1(img):
    r, g, b = cv2.split(img)
    gray = 0.299*r + 0.587*g + 0.114*b
    gray = gray.astype(int)
    return gray

def tekstur(imgGray4):
    imgGray = rgbtogray1(imgGray4)
    matrixFrameWork = np.zeros((256, 256), dtype=np.int32)
    for i in range(len(imgGray)):
        for j in range(len(imgGray[0])-1):
            matrixFrameWork[imgGray[i][j]][imgGray[i][j+1]] = matrixFrameWork[imgGray[i][j]][imgGray[i][j+1]] + 1

    # transposeFrameWwork = matrixFrameWork.transpose()

    # matrixGLCM = matrixFrameWork+transposeFrameWwork
    # totalValue = matrixGLCM.sum()

    # glcmNorm = [[0 for i in range(256)] for j in range(256)]
    # for i in range(len(matrixFrameWork)):
    #     for j in range(len(matrixFrameWork[0])):
    #         glcmNorm[i][j] = matrixGLCM[i][j]/totalValue


    contrast = np.sum(np.square(np.arange(256)[:, np.newaxis] - np.arange(256)[np.newaxis, :]) * matrixFrameWork)
    homogeneity = -np.sum(matrixFrameWork * np.log(matrixFrameWork + np.finfo(float).eps))
    entropy = np.sum(matrixFrameWork / (1 + np.abs(np.arange(256)[:, np.newaxis] - np.arange(256)[np.newaxis, :])))
    # for i in range(len(matrixFrameWork)):
    #     for j in range(len(matrixFrameWork[0])):
    #         contrast = contrast + glcmNorm[i][j] * (i-j) *(i-j)
    #         dissimilarity = dissimilarity + glcmNorm[i][j] * abs(i-j)
    #         homogeneity = homogeneity + glcmNorm[i][j] / (1 + (i-j) *(i-j))
    #         if(glcmNorm[i][j]>0):
    #             entropy = entropy + glcmNorm[i][j] * math.log10(glcmNorm[i][j])
    # entropy = entropy * (-1)
    array = [contrast,homogeneity,entropy]
    return array

def compare(img1,img2):
    hasilDot = np.dot(img1,img2)
    norm1 = np.linalg.norm(img1)
    norm2 = np.linalg.norm(img2)
    return hasilDot/(norm1*norm2)


# image = cv2.imread(r"Algeo\Tubes\Tubes2\dataset\0.jpg")
# imgGray9 = cv2.resize(image,(0,0),fx=0.5,fy=0.5)
# imgGray1 = tekstur(imgGray9)
# image1 = cv2.imread(r"Algeo\Tubes\Tubes2\white.jpg")
# imgGray8 = cv2.resize(image1,(0,0),fx=0.5,fy=0.5)
# arr2 = tekstur(imgGray8)
# print(imgGray1)
# arr1=imgGray1
# hasil = compare(arr1,arr2)
# print(hasil)


# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# imgGray1 = tekstur(imgGray9)
# dataset=[]
# filename = "halotes"
# sim = []
# sim.append(imgGray1)
# sim.append(filename)
# dataset.append(sim)
# filename = "halotessssss"
# sim = []
# sim.append(arr2)
# sim.append(filename)
# dataset.append(sim)
# print(dataset)
# print(dataset[0][0][0])



def teksturToChace(data_directory):
    list_of_files = os.listdir(data_directory)
    dataset=[]
    for filename in list_of_files:
        print(filename)
        sim = []
        dataset_image = cv2.imread(os.path.join(data_directory, filename))
        dataset_tekstur = tekstur(dataset_image)
        sim.append(dataset_tekstur)
        sim.append(filename)
        dataset.append(sim)
        print(dataset)
    return dataset

def arrToCSV(arr,pathCSV):
    with open(pathCSV,'w',newline='') as fileCSV:
        nameCSV = ['hasil','pathImg']
        write = csv.DictWriter(fileCSV,fieldnames=nameCSV)
        write.writeheader()
        for row in arr:
            write.writerow(row)

def csvToArr(pathCSV):
    dataset=[]
    df = pd.read_csv(pathCSV)
    df['hasil']=df['hasil'].apply(eval)
    for index,row in df.iterrows():
        sim=[]
        hasil,pathImg=row['hasil'],row['pathImg']
        sim.append(hasil)
        sim.append(pathImg)
        dataset.append(sim)
    return dataset

# data = "Algeo\Tubes\Tubes2\dataset"
# # arrData=teksturToChace(data)
# arrayObjects = []
# arrayObjects.append({
#     "hasil":imgGray1,
#     "pathImg":filename
# })
# pathCSV="Algeo\\Tubes\\Tubes2\\Algeo02-22135\\Tekstur\\data.csv"
# arrToCSV(arrayObjects,pathCSV)
# sim2 = csvToArr(pathCSV)
# print(sim2)
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
