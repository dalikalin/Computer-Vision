# Exercise 7: Calculate average pixel values from a folder of images
# 1. Objective: Calculate average pixel values from all images from a folder.
# 2. Instructions:
# o Read all images from a folder using:
# for filename in os.listdir(folder_path):
# file_path = os.path.join(folder_path, filename)…
# o Resize them to a specific size (128 x 128 or 256 x 256 for examples).
# o Calculate the pixel-wise average values from all three channels so there will be only one channel remaining.
# o Display and save the results.
import cv2
import os
import numpy as np

# Folder containing the images to average, and the size to resize each one to
folder_path = "images"
target_size = (128, 128)

# "Bucket" to add every resized image into, and a counter for how many were added.
# float64 is used instead of the normal image type so the running total
# doesn't overflow past 255 while images are being summed.
accumulator = np.zeros((128, 128, 3), dtype=np.float64)
count = 0

# Go through every file in the folder one at a time
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)   # build the full path to the file
    image = cv2.imread(file_path)                      # load the image
    resized_img = cv2.resize(image, target_size)        # resize so every image matches in size

    accumulator = accumulator + resized_img   # add this image's pixel values into the bucket
    count = count + 1                          # keep track of how many images we've added

print("Total images added:", count)

# Divide the summed pixel values by the number of images to get the average
avg_color = accumulator / count

# Average the 3 color channels (Blue, Green, Red) together into 1 channel per pixel
avg_single_channel = avg_color.mean(axis=2)

# Convert back from decimal numbers to whole numbers (0-255) so it's a valid image
avg_uint8 = avg_single_channel.astype(np.uint8)

# Show the result in a window
cv2.imshow("Average Image", avg_uint8)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the result to disk
cv2.imwrite("averageimage.jpg", avg_uint8)
print("Saved average image!")