'''
Created on 18 ago 2020

@author: raffa
'''
if __name__ == '__main__':
    pass

# importo il pacchetto pandas com pd
import pandas as pd

df1=pd.read_csv('../../../df.csv')
print(df1)

'''
df1=pd.read_csv('../../../df.csv',header=None)
print(df1)

df1=pd.read_csv('../../../df.csv',names=['v1','v2','v3','v4','v5'])
print(df1)

df1=pd.read_csv('../../../df.csv',usecols=[0])
print(df1)
'''

print(df1.head(2))
print(df1.tail(2))
print(df1.describe())

# import from web https://archive.ics.uci.edu/ml/index.php

vini=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data')
print(vini.head(5))
vini.to_csv('../../../vini.csv')
vini.to_excel('../../../vini.xlsx',sheet_name='Sheet_name_1')
