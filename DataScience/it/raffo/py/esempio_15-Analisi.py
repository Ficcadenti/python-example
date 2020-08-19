'''
Created on 19 ago 2020

@author: raffa
'''
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

if __name__ == '__main__':
    pass

df_missing=pd.read_csv('../../../df_missing.csv')

print('**************** Analisi (Data cleaning) GIGO "spazzatura dentro, spazzatura fuori" *****************')

print(df_missing)
print(df_missing.dropna())
print(df_missing.dropna(axis=1,how='any'))
print(df_missing.fillna(0))
print(df_missing.fillna(df_missing.mean()))

#scikit-learn
print(df_missing.fillna(df_missing.mean()))


imp=SimpleImputer(missing_values=np.nan, strategy='median')
imp = imp.fit(df_missing.iloc[:, 1:4])

df_missing.iloc[:, 1:4] = imp.transform(df_missing.iloc[: , 1:4])

print(df_missing)
#print(imp.transform())
#help(SimpleImputer)

