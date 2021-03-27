from matplotlib import pyplot as plt
import numpy as np
import cv2

img_path = r"path/of/the/image"  #path of the image
img = cv2.imread(img_path)

#plt.imshow(img)
#plt.show()
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#plt.figure(figsize= (10,10))
#plt.imshow(image)
#plt.show()
image_small = cv2.pyrDown(img)
number_iter = 5
for _ in range(number_iter):
    image_small= cv2.bilateralFilter(image_small, d=9, sigmaColor=9, sigmaSpace=7)
image_rgb = cv2.pyrUp(image_small)
#plt.imshow(image_rgb)
#plt.show()
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
image_blur = cv2.medianBlur(image_gray, 7)
image_edge = cv2.adaptiveThreshold(image_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 2)
#plt.imshow(image_edge)
#plt.show()
image_edge = cv2.cvtColor(image_edge, cv2.COLOR_GRAY2RGB)
#plt.imshow(image_edge)
#plt.show()
# image_edge = cv2.cvtColor(image_edge, cv2.COLOR_GRAY2RGB)
array = cv2.bitwise_xor(image, image_edge)     #taking xor between image and image_edge to get ghost filter
plt.figure(figsize= (10,10))
plt.imshow(array)
plt.axis('off')
plt.show()  #real ghost filtered photo
