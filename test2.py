# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2
import numpy as np

def salt(img, n):
	for k in range(n):
		i = int(np.random.random() * img.shape[1])
		j = int(np.random.random() * img.shape[0])
		if img.ndim == 2:
			img[j,i] = 0
		elif img.ndim == 3:
			img[j,i,0] = 0
			img[j,i,1] = 0
			img[j,i,2] = 0
	return img

def test2(img):
	for k in range(n):
		i = int(np.random.random() * img.shape[1])
		j = int(np.random.random() * img.shape[0])
		if img.ndim == 2:
			img[j,i] = 0
		elif img.ndim == 3:
			img[j,i,0] = 0
			img[j,i,1] = 0
			img[j,i,2] = 0
	return img

if __name__ == '__main__':
	img = cv2.imread('mk.png')
	saltImage = salt(img,800)
	cv2.imwrite("./test21.jpg", saltImage)  