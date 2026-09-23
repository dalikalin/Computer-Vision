# Exercise 4: Resize an Image
# 1. Objective: Learn how to resize an image using OpenCV.
# 2. Instructions:
# o Load an image.
# o Resize it to half of its original dimensions using cv2.resize().
# o Display and/or save the resized image
import cv2
img = cv2.imread("drstrange.jpg")
h, w = img.shape[:2]
resized = cv2.resize(img,(w // 2, h // 2))
cv2.imshow("Resized Image", resized)
cv2.imwrite("resizeddrstrange.jpg", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()