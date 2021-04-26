#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 04:05:23 2021

@author: erenozbek
"""

import pandas as pd
import numpy as np

def linear_regress(y, x):
    
    y = np.array(y)
    x = np.array(x)
    
    beta = np.linalg.inv(x.T@x) @ x.T @ y
    e = y - (x @ beta)
    sigmasq = (e.T @ e) / (x.shape[0] - x.shape[1])
    var = np.diag(np.multiply(sigmasq, np.linalg.inv(x.T@x)))
    SE = np.sqrt(var)
    z = 1.96
    upper = beta + SE * z
    lower = beta - SE * z
    CI = [lower, upper]
    
    output = {'beta': beta, 'Confidence Interval': CI, 'SE': SE}
    print('Here are the results')
    print(output)
    return output