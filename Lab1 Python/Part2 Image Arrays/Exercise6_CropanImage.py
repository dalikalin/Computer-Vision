# Exercise 6: Crop an Image
# 1. Objective: Learn how to crop a region of interest (ROI) from an image.
# 2. Instructions:
# o Load an image.
# o Crop a rectangular region from the image using NumPy slicing.
# o Display and/or save the cropped region
import cv2
img = cv2.imread("drstrange.jpg")
cropped = img[50:250, 100:300]
cv2.imshow("croppeddrstrange", cropped)
cv2.imwrite("croppeddrstrange.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()