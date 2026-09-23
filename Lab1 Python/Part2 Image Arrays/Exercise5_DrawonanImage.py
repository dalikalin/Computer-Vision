# Exercise 5: Draw on an Image
# 1. Objective: Learn how to draw shapes on an image.
# 2. Instructions:
# o Load an image.
# o Draw a red rectangle and a blue circle on the image using cv2.rectangle() and cv2.circle().
# o Display and/or save the modified image.
import cv2
img = cv2.imread("drstrange.jpg")
# Draw a red rectangle
cv2.rectangle(img, (50, 50), (300, 200), (0, 0, 255), 3)
# Draw a blue circle
cv2.circle(img, (400, 200), 50, (255, 0, 0), 3)
cv2.imshow("drawdrstrange", img)
cv2.imwrite("drawdrstrange.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()