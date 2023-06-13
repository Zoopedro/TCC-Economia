# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:58:12 2023

@author: e-pedro.soares
"""

import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from datetime import datetime
from linearmodels.panel import PanelOLS
import statsmodels.api as sm

data = pd.read_excel('Base.xlsx')

data = data[['porcent_acertos_pt', 'porcent_acertos_mat', 'Time_tra', 'tratamento']]

data['Time_tra'] = pd.to_datetime(data['Time_tra'])


def convert_month(month):
    if month == 5:
        return 0
    elif month == 12:
        return 1
    else:
        return month
    
data['Time_tra'] = data['Time_tra'].dt.month.apply(convert_month)

data['timeXtrat'] = data['Time_tra'] * data['tratamento']

ols_pt = ols('porcent_acertos_pt ~ tratamento + Time_tra + timeXtrat', data=data).fit()
print(ols_pt.summary())

ols_mat = ols('porcent_acertos_mat ~ tratamento + Time_tra + timeXtrat', data=data).fit()
print(ols_mat.summary())
