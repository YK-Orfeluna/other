# -*- coding: utf-8 -*-
from goma import *

if __name__ == "__main__" :
	arr = [1, 2, 3, 4, 5]
	r = rms(arr)
	print("rms = %s" %r)

	db = rms2db(r)
	print("%s dB" %db)

	m = mapping(5, 0, 10, 0, 100)
	print("map_pro = %s" %m)

	src = cv2.VideoCapture(0)
	ret, frame = src.read()
	if ret == True :
		af = affine(frame, 45)
		af = cv2.resize(af, (af.shape[1]/3, af.shape[0]/3))
		cv2.imshow("Affine", af)
		cv2.waitKey(0)
		src.release()
		cv2.destroyAllWindows()
	exit()