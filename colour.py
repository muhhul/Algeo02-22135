import cv2
import numpy as np

def RGBtoHSV (imagename):
    #Membaca dan melakukan pre processing
    img = cv2.imread(imagename)
    height, width = img.shape[:2]
    R,G,B = cv2.split(img)

    #Normalisasi
    R = R / 255
    G = G / 255
    B = B / 255

    #Penampung nilai HSV
    h = []
    s = []
    v = []

    
    for y in (height):
        for x in (width):

            #Mencari variabel cmax,cmin,dan 
            cmax = max(R[x][y],G[x][y],B[x][y])
            cmin = max(R[x][y],G[x][y],B[x][y])
            delta = cmax - cmin  

            # Mengisi lit H, list S, list V dengan perhitungan
            h.append(hue(R[x][y],G[x][y],B[x][y],cmax,delta))
            s.append(saturation(R[x][y],G[x][y],B[x][y],cmax,delta))
            v.append(cmax)

    return h,s,v


def hue (r,g,b,cmax,delta):
    if(delta == 0):
        h = 0

    elif (cmax == r):
        h = 60 * (((g - b) / delta) % 6)

    elif (cmax == g):
        h = 60 * (((b - r) / delta) + 2)
    
    elif (cmax == b):
        h = 60 * (((r - g) / delta) + 4)

    return h

def saturation (cmax,delta):
    if (cmax == 0):
        s = 0

    elif (cmax != 0):
        s = delta / cmax

    return s

#konsepnta udah dapet
#sisa histogram
#sama similarity