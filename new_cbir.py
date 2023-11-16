import cv2
import numpy as np
import math
import os
import time

def calculate_histogram(image):
    # Melakukan normlisasi image dengan membaginya dengan 255
    image = image.astype(np.float32) / 255.0
    hsv_image = np.zeros_like(image, dtype=np.float32)
    # Mencari cmax,cmin,dan delta
    Cmax = np.max(image, axis=2)
    Cmin = np.min(image, axis=2)
    delta = Cmax - Cmin

    # Menghitung H atau Hue
    hsv_image[..., 0] = np.where(delta == 0, 0,np.where(Cmax == image[..., 2], 60 * ((image[..., 1] - image[..., 0]) / (delta + 1e-5) % 6),np.where(Cmax == image[..., 1], 60 * ((image[..., 0] - image[..., 2]) / (delta + 1e-5) + 2),60 * ((image[..., 2] - image[..., 1]) / (delta + 1e-5) + 4))))

    # Menghitung S atau Saturation
    hsv_image[..., 1] = np.where(Cmax == 0, 0, delta / (Cmax + 1e-5))

    # Menghitung V atau Value
    hsv_image[..., 2] = Cmax

    # Scaling H untuk menyamai format OpenCV
    hsv_image[..., 0] *= 0.5

    # Mengkonversi ke bentuk uint8
    hsv_image = (hsv_image * 255).astype(np.uint8)

    # Membuat Histogram dengan memanfaatkan OpenCV
    hist = cv2.calcHist([hsv_image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])

    #Melakukan normalisasi histogram
    hist = cv2.normalize(hist, hist).flatten()

    return hist


def calculate_block_histograms(image, block_size):
    # Calculate the dimensions of the image
    height, width, _ = image.shape

    block_histograms = []
    
    # Iterate through the image in block_size steps
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            # Define the block region
            block = image[y:y+block_size, x:x+block_size]
            
            # Calculate histogram for this block
            block_hist = calculate_histogram(block)
            block_histograms.append(block_hist)
    
    return block_histograms


def cosine_similarity(histogram1, histogram2):
    # Sesuai rumus cosine similarity, Untuk menghitung dot product dari vektor histogram image 1 dan vektor histogram image 2 
    dot = np.dot(histogram1, histogram2)

    # Melakukan perkalian panjang vektor histogram 1 dan panjang vektor histogram 2
    norm1 = np.linalg.norm(histogram1)
    norm2 = np.linalg.norm(histogram2)

    # Menghandle jika pembaginya adalah 0
    if (norm1 * norm2 != 0):
        similarity = dot / (norm1 * norm2)
    else:   
        similarity = 0

    return similarity

def compareimage_with_blocks(input_image, data_directory, block_size):
    # Calculate histogram for the entire input image
    histogram_input = calculate_histogram(input_image)
    
    # Calculate block-wise histograms for the input image
    block_histograms_input = calculate_block_histograms(input_image, block_size)

    sim = []
    filenames = []

    # Obtain the list of files in the data directory
    list_of_files = os.listdir(data_directory)

    # Iterate through all files in the directory
    for filename in list_of_files:
        dataset_image = cv2.imread(os.path.join(data_directory, filename))

        # Calculate histogram for the dataset image
        dataset_hist = calculate_histogram(dataset_image)
        
        # Calculate block-wise histograms for the dataset image
        block_histograms_dataset = calculate_block_histograms(dataset_image, block_size)

        # Compute similarity based on overall histogram
        similarity = cosine_similarity(histogram_input, dataset_hist)

        # Calculate similarity based on block-wise histograms
        block_similarities = []
        for block_hist_input in block_histograms_input:
            block_sim = []
            for block_hist_dataset in block_histograms_dataset:
                block_sim.append(cosine_similarity(block_hist_input, block_hist_dataset))
            block_similarities.append(max(block_sim))

        # Take the average of block similarities
        block_similarity_avg = sum(block_similarities) / len(block_similarities)
        
        # Combine overall and block-wise similarity (you can adjust weights or use other strategies)
        combined_similarity = 0.6 * similarity + 0.4 * block_similarity_avg
        
        sim.append(combined_similarity * 100)
        filenames.append(filename)

    # Sorting based on similarity scores
    sorted_indices = np.argsort(sim)[::-1]
    sorted_similarities = np.sort(sim)[::-1]
    sorted_filenames = [filenames[i] for i in sorted_indices]

    return sorted_indices, sorted_similarities, sorted_filenames


# Melakukan running program yakni driver_colour
def run():
    data_directory = "C:\\Users\\chris\\Documents\\Semester 3 Informatika\\Tubes Algeo 2\\Image"  
    input_image = cv2.imread("451.jpg")
    
    start_time = time.time()
    sorted_indices, sorted_similarities,sorted_filenames = compareimage_with_blocks(input_image, data_directory,4)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
 
    top_5_indices = sorted_indices[:5]

    for i in range(len(top_5_indices)):
        dataset_image = cv2.imread(os.path.join(data_directory, os.listdir(data_directory)[top_5_indices[i]]))
        print(f"Image {sorted_filenames[i]} - Similarity: {sorted_similarities[i]}")
        cv2.imshow(f"Image {sorted_filenames[i]} - Similarity: {sorted_similarities[i]}", dataset_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()