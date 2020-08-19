'''
Created on 19 ago 2020

@author: raffa
'''

import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib as mlp
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pass


studenti=pd.read_csv('../../../students2.csv')

print('**************** Analisi (Data cleaning) GIGO "spazzatura dentro, spazzatura fuori" *****************')

np.random.rand(12345)
df = pd.DataFrame(np.random.randint(200, size=(10, 6)))
print(df)
df_norm=(df-df.min())/(df.max()-df.min())
print(df_norm)

print(preprocessing.scale(df))
df_scaler=preprocessing.MinMaxScaler(feature_range=(0,1))
df_scaled=df_scaler.fit_transform(df)
print(df_scaled)

df_norm.boxplot(return_type='axes')
#plt.boxplot(df_scaled)
plt.show()