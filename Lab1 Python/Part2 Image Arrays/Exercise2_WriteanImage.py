# Exercise 2: Write an Image
# 1. Objective: Save an image to your computer using OpenCV.
# 2. Instructions:
# o Load an image (you can use the one from Exercise 1).
# o Save it with a new name using cv2.imwrite().
# o Verify that the image is saved correctly in the specified directory.
import cv2
img = cv2.imread("drstrange.jpg")
cv2.imwrite("newdrstrange.jpg", img)
print("Saved!")