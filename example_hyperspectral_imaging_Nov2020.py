# -*- coding: utf-8 -*-
"""
Spyder Editor operated by Kevin Kang, TWO & Solutions

This is a temporary script file.
"""

import rasterio # reading geo-referenced dataset
import os
import matplotlib.pyplot as plt
from rasterio.plot import show

# os.getcwd()
# os.chdir("E:/data/")

# fp =r'EO1H0360292016308110KF_B230_L1GST.TIF'
# img = rasterio.open(fp)
# show(img)

import rasterio as rs
dataset030 = rs.open('EO1H0360292016308110KF_B030_L1GST.TIF')
dataset080 = rs.open('EO1H0360292016308110KF_B080_L1GST.TIF')
dataset115 = rs.open('EO1H0360292016308110KF_B115_L1GST.TIF')

# dataset.count: Number of bands
# dataset.height, dataset.width: Image resolution 
# 
# dataset.crs:
# Coordinate Reference System (CRS)
# European Petroleum Survey Group (EPSG)
#
# EPSG Projection 32612 - WGS 84 / UTM zone 12N
# https://spatialreference.org/ref/epsg/wgs-84-utm-zone-12n/
#
show(dataset030)
print (dataset030.count)
print (dataset030.height, dataset030.width)
print (dataset030.crs)


# from osgeo import gdal
# import matplotlib.pyplot as plt
