# -*- coding: utf-8 -*-
"""
Spyder Editor operated by Kevin Kang, TWO & Solutions

This is a temporary script file.
"""





from spectral import *
# http://www.spectralpython.net/fileio.html

import numpy
import pylab

def bracket(x,n):
    return 0.5*(numpy.sign(x)+1)*(x**n)

L = 1

X = numpy.linspace(0,2,1000)

Y0 = bracket(X-L,0)
Y1 = bracket(X-L,1)
Y2 = bracket(X-L,2)

pylab.plot(X,Y0,label="^0")
pylab.plot(X,Y1,label="^1")
pylab.plot(X,Y2,label="^2")

pylab.legend()
pylab.show()
