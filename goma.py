# -*- coding: utf-8 -*-

import sys, time, math
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
		sys.exit("rnd is only True or False")
	return rms

"""rmsをdBに変換する"""
def rms2db(rms) :
	db = 20.0 * math.log10(rms)
	return db

"""t(ms)待機"""
def delay(t) :
	t /= 1000.0
	time.sleep(t)

def framerate(fps) :							# Config of framerate
	ms = round(1000.0 / fps, 0)					# Between-time of frame(mill-second)
	s = ms / 1000.0								# Between-time of frame(second)
	time.sleep(s)
	
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
def mapping(x, pre_min, pre_max, now_min, now_max) :
	a, b = sympy.symbols("a, b")
	f = sympy.solve([pre_max * a + b - now_max, pre_min * a + b - now_min], [a, b])
	y = f[a] * x + f[b]
	return y

def se(x, axis=None) :
	s = np.std(x, ddof=1)		# 不偏分散を求める
	n = len(x)					# データサイズ
	se = s / np.sqrt(n)			# 標準誤差
	return se


if __name__ == "__main__" :
	print(se(arr))



