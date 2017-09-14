# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2
import numpy as np  

img = cv2.imread("../t.jpeg",0) 
img = cv2.GaussianBlur(img,(3,3),0)  
canny = cv2.Canny(img, 50, 150)  
  
cv2.imwrite('Canny.jpg', canny)