import CBIR_colour
import cv2
import numpy as np
import math
import os
import time

#baca gambar file input
img = cv2.imread("0.jpg")
img = cv2.resize(img,(0,0),fx = 0.5, fy = 0.5)
hist1 = CBIR_colour.RGBtoHSV(img,bins=8)

path = "C:\\Users\\chris\\Documents\\Semester 3 Informatika\\Tubes Algeo 2\\Image"
daftar_file = os.listdir(path)

sim = []
for nama_file in daftar_file:
    start_time = time.time()

    img2 = cv2.imread(os.path.join(path,nama_file))
    img2 = cv2.resize(img2,(0,0), fx = 0.5, fy = 0.5)
    hist2 = CBIR_colour.RGBtoHSV(img2,bins=8)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Waktu eksekusi: ",elapsed_time)
    sim.append(((CBIR_colour.calculate_similarity(hist1,hist2)))* 100)


simsort = sorted(sim,reverse=True)
for i in range(len(sim)):
    if(simsort[i] < 40):
        break
    for j in range(len(sim)):
        if (simsort[i] == sim[j]):
            print(f"Tingkat kecocokan ke-{i+1} adalah gambar ke {j+1} yang bernama {daftar_file[j]} dengan persentase {simsort[i]} %")