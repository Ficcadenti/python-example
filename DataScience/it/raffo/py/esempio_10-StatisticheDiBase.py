'''
Created on 18 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

# importo il pacchetto pandas con pd e numpy con np
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'Names': ['Simon', 'Kate', 'Francis', 'Laura', 'Mary', 'Julian', 'Rosie', 'Simon', 'Laura'],
                    'Height':[180, 165, 170, 164, 163, 175, 166, 180, 164],
                    'Weight':[85, 65, 68, 45, 43, 72, 46, 85, 45],
                    'Pref_food': ['steak', 'pizza', 'pasta', 'pizza', 'vegetables', 'steak', 'seafood', 'steak', 'pizza'],
                    'Sex': ['m','f','m','f','f','m','f', 'm', 'f']})


print(df1)
print(df1.describe().transpose())
print(df1.count())
print(df1['Height'].median())
print(df1['Height'].mean())
print(df1['Height'].min())
print(df1['Height'].max())
print(df1['Height'].std())
print(df1['Height'].skew())
print(df1['Height'].kurt())
print(df1['Height'].mode())