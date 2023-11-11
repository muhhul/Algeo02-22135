import cv2
import numpy as np
import math
import os
import time

def RGBtoHSV(image, bins=8):
    # Normalization
    image = image / 255.0

    r, g, b = image[:, :, 0], image[:, :, 1], image[:, :, 2]

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


def calculate_similarity(histogram1, histogram2):
    dot = np.dot(histogram1,histogram2)
    norm1 = np.sqrt(np.dot(histogram1, histogram1))
    norm2 = np.sqrt(np.dot(histogram2, histogram2))

    if (norm1 * norm2 != 0):
        similarity = dot / (norm1 * norm2)
    else:
        similarity = 0

    return similarity