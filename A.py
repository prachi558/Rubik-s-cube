import numpy as np
import cv2


def avg(x):
		z=[]
		y=[]
		avg=[]
		for j in range(0, len(x)):
			y.extend(x[j])
		avg = np.average(y, axis = 0)
		return avg