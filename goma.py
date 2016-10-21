# -*- coding: utf-8 -*-

import numpy as np
import cv2
import sympy

"""二乗平均平方根を求める"""
def rms(arr, rnd=False, ndigits=0) :
	# arrはnumpy形式の1次元配列かリスト形式
	rms = np.sqrt(np.mean(np.square(arr)))
	if rnd == True :				# rndがTrueの時，四捨五入（桁はndigistで指定）
		rms = round(rms, ndigits)
	elif rnd != True and rnd != False :
		print("rnd is only True or False")
		exit()
	return rms
	
"""アフィン返還による画像回転"""
def affine(frame, angle=0.0, scale=1.0) :
	# angleは画像frameを回転させたい角度（dgree）
	# scaleは拡大比率
	if angle != 0.0 :
		h, w, c = frame.shape
		rotation_matrix = cv2.getRotationMatrix2D((w * 0.5, h * 0.5), angle, scale)		# 回転変換行列の算出(第一引数は画像回転軸（ここでは画像中心）		
		img_rot = cv2.warpAffine(frame, rotation_matrix, (w, h), flags=cv2.INTER_CUBIC)	# アフィン変換
		return img_rot
	else :
		print("Rotation Angle is 0.0!")
		print("Set Angle or Not Use This Function")
		exit()

"""pre_min-pre_maxの範囲の値xをnow_min-now_maxの範囲で置き換える（Processingのmap関数と同じ）"""
def map_pro(x, pre_min, pre_max, now_min, now_max) :
	a, b = sympy.symbols("a, b")
	f = sympy.solve([pre_max * a + b - now_max, pre_min * a + b - now_min], [a, b])
	y = f[a] * x + f[b]
	return y

def explanation() :
	n = "need library: "
	print("rms(arr, rnd=False, ndigist=0)")
	print("arr is list or ndarray(ndim=1), return value is used round(return, ndigist) when rnd=True")
	print(n + "Numpy")

	print("affine(frame, angle=0.0, scale=0.0)")
	print("frame is target image, angle is rotation degrees, scale is image magnification")
	print(n + "Numpy & OpenCV")

	print("map_pro(x, pre_min, pre_max, now_min, now_max)")
	print("this function is same as map() in Processing")
	print("x(pre_min~pre_max) change to return(now_min~now_max")
	print(n + "Sympy")

if __name__ == "__main__" :
	explanation()
	arr = [1, 2, 3, 4, 5]
	r = rms(arr)
	print("rms = %s" %r)

	m = map_pro(5, 0, 10, 0, 100)
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