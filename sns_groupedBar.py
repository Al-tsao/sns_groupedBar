#Standard

import numpy as np

import pandas as pd

from numpy.random import randn

from pandas import Series, DataFrame

#Stats

from scipy import stats

#Matplotlib

import matplotlib as mpl

import matplotlib.pyplot as plt

#Seaborn

import seaborn as sns

#Draw

sns.set() #設定繪圖改為seaborn繪製

df = pd.DataFrame({"Price": [7,1,5,6,3,10,5,8],
                    "Product": ['C1','C2','C1','C2','C1','C2','C1','C2'],
                  "Day": [1,1,2,2,3,3,4,4]})

sns.barplot(x ="Day", y = 'Price', data = df, hue = "Product")  #color:制定bar的顏色；linewidth: 邊線粗細；label: 顯示圖表，要搭配legend()使用

plt.xlabel('this is x')

plt.ylabel('this is y')

plt.title('this is a demo')

plt.legend()

plt.show() #繪圖