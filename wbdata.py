#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 02:11:33 2021

@author: erenozbek
"""

import wbdata
import pandas as pd
import numpy as np
import linear


tur = [i['id'] for i in wbdata.get_country(country_id=("TUR"))]
variables = {"SP.URB.TOTL.IN.ZS": "Urban population (% of total population)", 
             "NY.GDP.PCAP.CD": "GDP per capita (current US$)"}
df = wbdata.get_dataframe(variables, country=tur, convert_date=True)
df.dropna(inplace=True)
df.to_csv('RegDataHW02.csv')

independent = df.iloc[:,0]
dependent = df.iloc[:,1:]

linear.linear_regress(independent, dependent)






