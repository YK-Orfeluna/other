# -*- coding: utf-8 -*-

import time, math
import cython


def mapping(double value, double fromLow, double fromHigh, double toLow, double toHigh) :
	cdef double a = (toLow-toHigh) / (fromLow-fromHigh)
	cdef double b = y1 - x1*a
	cdef double out = a*z + b
	return out

cdef double thouthand = 1000.0
def delay(double t) :
	global thouthand
	t /= thouthand
	time.sleep(t)

cdef int zero = 0
def framerate(int fps) :
	global thouthand, zero
	cdef int ms = round(thouthand / fps, zero)
	time.sleep(ms)

# def rms(arr) :
# 	rms = np.sqrt(np.mean(np.square(arr)))
# 	return rms

cdef double tw = 20.0
def rms2db(double rms) :
	global tw
	cdef double db = tw * math.log10(rms)
	return db
