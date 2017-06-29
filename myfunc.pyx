# -*- coding: utf-8 -*-

import time, math
import cython

import numpy as np
cimport numpy as np
DTYPE = np.float64
ctypedef np.float64_t DTYPE_t

def mapping(double value, double fromLow, double fromHigh, double toLow, double toHigh) :
	cdef double a, b, out
	a = (toLow-toHigh) / (fromLow-fromHigh)
	b = toLow - fromLow * a
	out = a * value + b
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

def rms(np.ndarray[DTYPE_t, ndim=1] arr) :
	cdef double rms = np.sqrt(np.mean(np.square(arr)))
	return rms

cdef double tw = 20.0
def rms2db(double rms) :
	global tw
	cdef double db = tw * math.log10(rms)
	return db

def se(np.ndarray[DTYPE_t, ndim=1] x) :
	cdef double s = np.std(x, ddof=1)
	cdef int n = len(x)
	cdef double se = s / np.sqrt(n)
	return se