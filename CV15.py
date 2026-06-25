
import cv2
import numpy as np
img1 = cv2.imread("C:/Users/vanib/Downloads/download (1).jpg")
img2 = cv2.imread("C:/Users/vanib/Downloads/download.jpg") # Define corresponding points
pts1 = np.array([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.array([[100, 100], [300, 100], [100, 300], [300, 300]])
H = cv2.getPerspectiveTransform(np.float32(pts1), np.float32(pts2))
dst = cv2.warpPerspective(img1, H, (1000, 1000))# Display images
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
