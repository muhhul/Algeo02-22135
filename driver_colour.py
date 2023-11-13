import CBIR_colour
import cv2
import numpy as np
import math
import os
import time

#baca gambar file input
dataset_dir = "C:\\Users\\chris\\Documents\\Semester 3 Informatika\\Tubes Algeo 2\\Image"  
input_image = cv2.imread("73.jpg")
start_time = time.time()
sorted_indices, sorted_similarities =  CBIR_colour.compareimage(input_image, dataset_dir, bins = 8)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
 

top_5_indices = sorted_indices[:5]

for i in range(len(top_5_indices)):
    dataset_image = cv2.imread(os.path.join(dataset_dir, os.listdir(dataset_dir)[top_5_indices[i]]))
    print(f"Image {top_5_indices[i]} - Similarity: {sorted_similarities[i]:.2f}")
    cv2.imshow(f"Image {top_5_indices[i]} - Similarity: {sorted_similarities[i]:.2f}", dataset_image)
    
cv2.waitKey(0)
cv2.destroyAllWindows()