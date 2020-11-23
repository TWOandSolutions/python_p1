# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 22:45:16 2020

@author: KevinKang from TWO & Solutions
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
from sklearn.metrics import mean_squared_error
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# from goodness-of-fit as rmse


# Preparing simulated and observed data
data_sim = np.array([3, -0.5, 2, 7, 10, 4, 5.5, 8, 1.8, 7.5])
#data_obs = np.array([2.5, 0.0, 2, 8, 12, 3.5, 5, 9, 1.0, 8.5]).reshape((-1, 1))
data_obs = np.array([2.5, 0.0, 2, 8, 12, 3.5, 5, 9, 1.0, 8.5])

#data_sim = np.random.randint(0,100,size=10)
#data_obs = np.random.randint(0,100,size=10)
model = LinearRegression().fit(data_obs, data_sim)

# Calculate RMSE, MBE, MAE, and Index of Agreement 
print ("RMSE:" +str(np.sqrt(mean_squared_error(data_sim, data_obs))))
print ("MBE: " +str(np.mean(data_sim-data_obs)))
print ("MAE: " +str(np.mean(abs(data_sim-data_obs))))
ia = (1 -(np.sum((data_obs-data_sim)**2))/(np.sum((np.abs(data_sim-np.mean(data_obs))+np.abs(data_obs-np.mean(data_obs)))**2)))
print ("Ia: " +str(ia))

plt.scatter(data_sim, data_obs,  color='black')
print ("R2: " +str(r2_score(data_obs, data_sim)))
print ("intercept:", model.intercept_)
print ("slope: ", model.coef_)

scipy.stats.pearsonr(data_obs, data_sim)     # Pearson's r
scipy.stats.spearmanr(data_obs, data_sim)    # Spearman's rho
scipy.stats.kendalltau(data_obs, data_sim)   # Keindall's tau

scipy.stats.pearsonr(data_obs, data_sim)[0]     # Pearson's r
scipy.stats.spearmanr(data_obs, data_sim)[0]    # Spearman's rho
scipy.stats.kendalltau(data_obs, data_sim)[0]   # Keindall's tau    

#plt.plot(data_obs, data_sim, color='blue', linewidth=3)
#plt.xticks(())
#plt.yticks(()) 
#plt.show()   







