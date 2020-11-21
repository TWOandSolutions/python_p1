# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 22:45:16 2020

@author: KevinKang from TWO & Solutions
"""

from sklearn.metrics import mean_squared_error
import numpy as np
# from goodness-of-fit as rmse


data_sim = np.array([3, -0.5, 2, 7])
data_obs = np.array([2.5, 0.0, 2, 8])

#data_sim = np.random.randint(0,100,size=10)
#data_obs = np.random.randint(0,100,size=10)

print ("RMSE:" +str(np.sqrt(mean_squared_error(data_sim, data_obs))))
print ("MBE: " +str(np.mean(data_sim-data_obs)))
print ("MAE: " +str(np.mean(abs(data_sim-data_obs))))
ia = (1 -(np.sum((data_obs-data_sim)**2))/(np.sum((np.abs(data_sim-np.mean(data_obs))+np.abs(data_obs-np.mean(data_obs)))**2)))
print ("Ia: " +str(ia))
    

