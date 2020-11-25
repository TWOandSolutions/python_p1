# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 22:45:16 2020

@author: KevinKang from TWO & Solutions

All references linked in my Youtube channel as well as those as below:

"""

# Examples of linear, log originally 
# from pyplot in matplotlib.pyplot
# https://matplotlib.org/api/pyplot_api.html

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(41623451)

# interval (0, 1)
y = np.random.normal(loc=0.5, scale=0.5, size=1500)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()
plt.subplot

# linear plot
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

# logarithim plot
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

plt.subplots_adjust(top=1.15, bottom=0.01, left=0.15, right=1.5, hspace=0.50,
                    wspace=0.5)

plt.show()

#
# Source codes from https://www.earthdatascience.org
# Lesson 1. Work With Datetime Format in Python - Time Series Data
# https://earthpy.readthedocs.io/en/latest/earthpy-data-subsets.html

# Import necessary packages
# matplotlib: a plotting library and its numerical math extension NumPy
# seaborn: a Python data visualization library based on matplotlib
# pandas: the Python programming language for data manipulation and analysis
# earthpy: a collection of IPython notebook with examples of Earth Science 
#          related Python code - tutorials, modules, scripts, and tricks

from matplotlib.axes._axes import _log as matplotlib_axes_logger
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import earthpy as et

# In case error found as below:
#
# ModuleNotFoundError: No module named 'earthpy'
# 
# conda config --add channels conda-forge
# conda install earthpy
# - https://github.com/conda-forge/earthpy-feedstock

# Maneuvering data & time coversion from pandas to matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Dealing with error thrown by one of the plots
matplotlib_axes_logger.setLevel('ERROR')
import warnings
warnings.filterwarnings('ignore')


# Adjust font size and style of all plots in notebook with seaborn
sns.set(font_scale=1.5, style="whitegrid")


# Downloading the data directly from the 2013 Colorado Flood
data = et.data.get_data('colorado-flood')

# Set working directory
os.chdir(os.path.join(et.io.HOME, 'earth-analytics', "data"))


# Defining relative path to the data on your current directory
file_path = os.path.join("colorado-flood",
                         "precipitation",
                         "805325-precip-daily-2003-2013.csv")

# Import the file as a pandas dataframe
boulder_precip_2003_2013 = pd.read_csv(file_path)
boulder_precip_2003_2013.head()

boulder_precip_2003_2013.plot(x="DATE",
                              y="HPCP",
                              title="Daily Precipitation ")

# Plot time versus daily precipitation
plt.show()


# Look at the range of values in the data - specifically the HPCP column
# Hourly Precipitation (HPCP)
# - https://www1.ncdc.noaa.gov/pub/data/cdo/documentation/PRECIP_HLY_documentation.pdf
# - Couldn't access to it midnight, but try it daytime

# To acknowledge the specific version of the dataset used, please cite:
# Hourly Precipitation Data (HPD) Network, Version 1. [indicate subset used
# following decimal, e.g. Version 1.0] beta,
# NOAA National Centers for Environmental Information. [access date].

# unit in HPCP with 100th of an inch
# - https://github.com/gojiplus/get-weather-data/blob/master/noaaweb/noaaweb.py


boulder_precip_2003_2013["HPCP"].describe()

# Import data using datetime and no data value
# Sometime, no value data representing NaN or -9999 in other applications

boulder_precip_2003_2013 = pd.read_csv(file_path,
                                       # Make sure the dates import in datetime format
                                       parse_dates=['DATE'],
                                       # Set DATE as the index so you can subset data by time period
                                       index_col=['DATE'],
                                       # Mask no data values so they are not plotted / used in analysis
                                       na_values=['999.99'])


# View the data
boulder_precip_2003_2013.head()


# View summary statistics == Notice the DATE column is not included
boulder_precip_2003_2013.describe()

boulder_precip_2003_2013.plot(y="HPCP",
                              title="Hourly Precipitation")

# Plot time versus hourly precipitation 
plt.show()


# subset
# resampling

from matplotlib.dates import DateFormatter

# Place your code to plot your data here
flood_data = boulder_precip_2003_2013['2013-09-01':'2013-11-01']

f, ax = plt.subplots(figsize=(10, 6))

ax.scatter(x=flood_data.index.values,
           y=flood_data["HPCP"])

# Define the date format
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)
ax.set(title="Optional Challenge \n Precipitation Sept - Nov 2013 \n Optional Plot with Dates Formatted Cleanly")

# Plot selected date versus HPCP
# unit in HPCP with 100th of an inch 
plt.show()


















