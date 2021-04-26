#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 04:34:43 2021

@author: erenozbek
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("../KocPython2021/RegDataHW02.csv")

x = df.iloc[:, 1] 
y = df.iloc[:, 2]

fig = plt.plot(x, y)
#fig.set_axis_labels("Urban population (% of total population", " GDP per capita growth (annual %)")
plt.title("Data Relationship")
plt.savefig("Regression.png")
plt.show()