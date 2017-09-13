# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2
import numpy as np   

if __name__ == '__main__':
	img = cv2.imread("mk.png")   
	emptyImage = np.zeros(img.shape, np.uint8)  
  
	emptyImage2 = img.copy()  
	  
	emptyImage3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  

	cv2.imwrite("./mktest11.jpg", emptyImage)  
	cv2.imwrite("./mktest12.jpg", emptyImage2)  
	cv2.imwrite("./mktest13.png", emptyImage3) 

	# PNG格式  IMWRITE_PNG_COMPRESSION
	cv2.imwrite("./mktest14.png", emptyImage2,[int(cv2.IMWRITE_PNG_COMPRESSION), 0])

	# JPG格式  IMWRITE_JPEG_QUALITY
	cv2.imwrite("./mktest15.jpg", img,[int(cv2.IMWRITE_JPEG_QUALITY), 1])  