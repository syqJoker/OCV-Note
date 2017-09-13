# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# 形态学处理
import cv2
import numpy as np  

img = cv2.imread("../mk.png",0) 

# 定义结构元素
# 形态学处理的核心就是定义结构元素
# 在OpenCV-Python中，可以使用其自带的getStructuringElement函数，也可以直接使用NumPy的ndarray来定义一个结构元素。

# 首先来看用getStructuringElement函数定义一个结构元素：
# element = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

# 也可以用NumPy来定义结构元素，如下：
# NpKernel = np.uint8(np.zeros((5,5)))  
# for i in range(5):  
#     NpKernel[2, i] = 1 #感谢chenpingjun1990的提醒，现在是正确的  
#     NpKernel[i, 2] = 1  

# 腐蚀和膨胀
#OpenCV定义的结构元素  
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))  
  
#腐蚀图像  
eroded = cv2.erode(img,kernel)  
#显示腐蚀后的图像  
cv2.imwrite("./test41.jpg", eroded)
  
#膨胀图像  
dilated = cv2.dilate(img,kernel)  
#显示膨胀后的图像  
cv2.imwrite("./test42.jpg", dilated)  
  
#NumPy定义的结构元素  
NpKernel = np.uint8(np.ones((3,3)))  
Nperoded = cv2.erode(img,NpKernel)  
#显示腐蚀后的图像  
cv2.imwrite("./test43.jpg", Nperoded)

Npdilate = cv2.dilate(img,NpKernel)  
#显示腐蚀后的图像  
cv2.imwrite("./test44.jpg", Npdilate)
