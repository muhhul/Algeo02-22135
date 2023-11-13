import cv2
import numpy as np
import math
import os
import time

def RGBtoHSVHistogram(image, bins=8):
    # Normalization
    image = image / 255.0

    r, g, b = cv2.split(image)

    hist = np.zeros((bins, bins, bins), dtype=int)

    cmax = np.maximum.reduce([r, g, b])
    cmin = np.minimum.reduce([r, g, b])
    delta = cmax - cmin

    # Handle zero division
    delta[delta == 0] = 1.0

    h = np.zeros_like(cmax)
    h[cmax == r] = 60 * ((g[cmax == r] - b[cmax == r]) / delta[cmax == r] % 6)
    h[cmax == g] = 60 * ((b[cmax == g] - r[cmax == g]) / delta[cmax == g] + 2)
    h[cmax == b] = 60 * ((r[cmax == b] - g[cmax == b]) / delta[cmax == b] + 4)

    s = np.where(cmax == 0, 0, delta / np.where(cmax == 0, 1, cmax))
    v = cmax

    # Normalize to bin size
    h = np.minimum((h / (360 / bins)).astype(int), bins - 1)
    s = np.minimum((s * bins).astype(int), bins - 1)
    v = np.minimum((v * bins).astype(int), bins - 1)

    # Calculate histogram
    hist[h, s, v] = np.sum(hist[h, s, v] + 1, axis=(0, 1))

    # Normalize histogram
    total = np.sum(hist)
    hist = hist / total

    return hist.flatten()


def cosine_similarity(histogram1, histogram2):
    dot = np.dot(histogram1,histogram2)
    norm1 = np.linalg.norm(histogram1)
    norm2 = np.linalg.norm(histogram2)

    if (norm1 * norm2 != 0):
        similarity = dot / (norm1 * norm2)
    else:
        similarity = 0

    return similarity

def compareimage(input_image, data_directory, bins=8):
    histogram_input = RGBtoHSVHistogram(input_image, bins)

    sim = []
    list_of_files = os.listdir(data_directory)

    for filename in list_of_files:
        dataset_image = cv2.imread(os.path.join(data_directory, filename))
        dataset_hist = RGBtoHSVHistogram(dataset_image, bins)

        similarity = cosine_similarity(histogram_input, dataset_hist)
        sim.append(similarity * 100)

    sorted_indices = np.argsort(sim)[::-1]
    sorted_similarities = np.sort(sim)[::-1]

    return sorted_indices, sorted_similarities

def run():
    data_directory = "C:\\Users\\chris\\Documents\\Semester 3 Informatika\\Tubes Algeo 2\\Image"  
    input_image = cv2.imread("0.jpg")
    start_time = time.time()
    sorted_indices, sorted_similarities = compareimage(input_image, data_directory,bins=8)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
 
    top_5_indices = sorted_indices[:5]

    for i in range(len(top_5_indices)):
        dataset_image = cv2.imread(os.path.join(data_directory, os.listdir(data_directory)[top_5_indices[i]]))
        print(f"Image {top_5_indices[i]} - Similarity: {sorted_similarities[i]}")
        cv2.imshow(f"Image {top_5_indices[i]} - Similarity: {sorted_similarities[i]}", dataset_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()