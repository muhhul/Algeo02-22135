import CBIR_colour
import cv2
import numpy as np
import math
import os
import time

#Mempersiapkan directory dataset
data_directory = "C:\\Users\\chris\\Documents\\Semester 3 Informatika\\Tubes Algeo 2\\Image"  
input_image = cv2.imread("451.jpg")
    
start_time = time.time()
sorted_indices, sorted_similarities,sorted_filenames = CBIR_colour.compareimage(input_image, data_directory)
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