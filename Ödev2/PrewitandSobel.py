import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./Images/img.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)



#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely


#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewitx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewity = cv2.filter2D(img_gaussian, -1, kernely)

#robert
robertx = np.array([[0,1],[-1,0]])
roberty = np.array([[1,0],[0,-1]])
img_robertx = cv2.filter2D(img_gaussian, -1, robertx)
img_roberty = cv2.filter2D(img_gaussian, -1, roberty)


cv2.imshow("Original Image", img)
cv2.imshow("Sobel", img_sobel)
cv2.imshow("Prewit", img_prewitx + img_prewity)
cv2.imshow("Robert",img_robertx+img_roberty)


cv2.waitKey(0)
cv2.destroyAllWindows()