import cv2
import numpy as np
import math

def RGBtoHSV(imagename):
    #Membaca dan melakukan pre processing
    img = cv2.imread(imagename)
    height, width = img.shape[:2]
    hsv = np.zeros((height, width, 3), dtype=np.float32)


    for y in range(height):
        for x in range(width):
            #Nilai dari RGB harus dinormalisasi dengan mengubah nilai range [0, 255] menjadi [0, 1]
            r, g, b = img[y, x] / 255.0

            cmax = max(r, g, b)
            cmin = min(r, g, b)
            delta = cmax - cmin

            h = hue(r, g, b, cmax, delta)
            s = saturation(cmax, delta)
            v = cmax

            hsv[y, x] = np.array([h, s, v])
            
    return hsv

def hue(r, g, b, cmax, delta):
    if delta == 0:
        h = 0
    elif cmax == r:
        h = 60 * (((g - b) / delta) % 6)
    elif cmax == g:
        h = 60 * (((b - r) / delta) + 2)
    elif cmax == b:
        h = 60 * (((r - g) / delta) + 4)
    return h

def saturation(cmax, delta):
    if cmax == 0:
        s = 0
    elif cmax != 0:
        s = delta / cmax
    return s

def compute_histogram(image):
    bins = [8, 8, 8]
    hist, _ = np.histogram(image, bins=bins, range=[0, 256])
    hist = hist / np.sum(hist)  # Normalisasi histogram
    return hist


def split_image_to_blocks(image, n):
    height, width, _ = image.shape
    block_size_x = width // n
    block_size_y = height // n
    blocks = []
    
    for i in range(0, height - block_size_y + 1, block_size_y):
        for j in range(0, width - block_size_x + 1, block_size_x):
            block = image[i:i + block_size_y, j:j + block_size_x]
            blocks.append(block)
    
    return blocks

def calculate_similarity(block1, block2):
    hist1 = compute_histogram(block1)
    hist2 = compute_histogram(block2)
    similarity = np.dot(hist1, hist2) / (np.linalg.norm(hist1) * np.linalg.norm(hist2))
    return similarity

def CBIR_similarity(image1, image2):
    hsv_image1 = RGBtoHSV(image1)
    hsv_image2 = RGBtoHSV(image2)
    
    blocks_image1 = split_image_to_blocks(hsv_image1, 3)
    blocks_image2 = split_image_to_blocks(hsv_image2, 3)
    
    similarities = []
    for i in range(len(blocks_image1)):
        sim = calculate_similarity(blocks_image1[i], blocks_image2[i])
        similarities.append(sim)
    
    average_similarity = sum(similarities) / len(similarities)
    return average_similarity
