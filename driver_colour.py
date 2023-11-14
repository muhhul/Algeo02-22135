import new_cbir
import cv2
import numpy as np
import math
import os
import time

#Mempersiapkan directory dataset
data_directory = "C:\\Users\\chris\\Documents\\Semester 3 Informatika\\Tubes Algeo 2\\Image" 

#Read input image
input_image = cv2.imread("63.jpg")

#Memulai proses compare image
start_time = time.time()
sorted_indices, sorted_similarities = new_cbir.compareimage(input_image, data_directory)
end_time = time.time()

#Mencatat waktu
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
 
#Mendapatkan 5 terbaik 
top_5_indices = sorted_indices[:10]

for i in range(len(top_5_indices)):
    dataset_image = cv2.imread(os.path.join(data_directory, os.listdir(data_directory)[top_5_indices[i]]))
    print(f"Image {top_5_indices[i]} - Similarity: {sorted_similarities[i]}")
    cv2.imshow(f"Image {top_5_indices[i]} - Similarity: {sorted_similarities[i]}", dataset_image)

cv2.waitKey(0)
cv2.destroyAllWindows()