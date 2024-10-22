# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 22:45:16 2020

@author: KevinKang from TWO & Solutions
"""

# on *Console*
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import sklearn

from sklearn.metrics import mean_squared_error
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# from goodness-of-fit as rmse


# On *Terminal* 
# conda install sklearn
# conda install scikit-learn
# pip install -U scikit-learn scipy matplotlib
#
# Please not to be confused for input commands between Console and Terminal
# Python is different from either IDL, MATLAB, or R language 


# Preparing simulated and observed data
data_sim = np.array([3.5, -0.6, 3, 7, 10, 4, 5.5, 8, 1.8, 7.5])
data_obs = np.array([3, 0.2, 3, 8, 12, 3.5, 5, 9, 1.0, 8.5]).reshape((-1, 1))
#data_sim = np.random.randint(0,100,size=10)
#data_obs = np.random.randint(0,100,size=10)

# Calculating determination of coefficient
model = LinearRegression().fit(data_obs, data_sim)
plt.scatter(data_sim, data_obs,  color='black')
print ("R2: " +str(r2_score(data_obs, data_sim)))
print ("intercept:", model.intercept_)
print ("slope: ", model.coef_)


# Preparing simulated and observed data
data_sim = np.array([3.5, -0.6, 3, 7, 10, 4, 5.5, 8, 1.8, 7.5])
data_obs = np.array([3, 0.2, 3, 8, 12, 3.5, 5, 9, 1.0, 8.5])

# Calculate RMSE, MBE, MAE, and Index of Agreement 
print ("RMSE:" +str(np.sqrt(mean_squared_error(data_sim, data_obs))))
print ("MBE: " +str(np.mean(data_sim-data_obs)))
print ("MAE: " +str(np.mean(abs(data_sim-data_obs))))
ia = (1 -(np.sum((data_obs-data_sim)**2))/(np.sum((np.abs(data_sim-np.mean(data_obs))+np.abs(data_obs-np.mean(data_obs)))**2)))
print ("Ia: " +str(ia))

# Plotting
plt.scatter(data_sim, data_obs,  color='black')
print ("R2: " +str(r2_score(data_obs, data_sim)))
print ("intercept:", model.intercept_)
print ("slope: ", model.coef_)


# Calculate pearson, spearman, kendall  
scipy.stats.pearsonr(data_obs, data_sim)     # Pearson's r
scipy.stats.spearmanr(data_obs, data_sim)    # Spearman's rho
scipy.stats.kendalltau(data_obs, data_sim)   # Keindall's tau

print (scipy.stats.pearsonr(data_obs, data_sim)[0])     # Pearson's r
print (scipy.stats.spearmanr(data_obs, data_sim)[0])    # Spearman's rho
print (scipy.stats.kendalltau(data_obs, data_sim)[0])   # Keindall's tau    

#plt.plot(data_obs, data_sim, color='blue', linewidth=3)
#plt.xticks(())
#plt.yticks(()) 
#plt.show()   







