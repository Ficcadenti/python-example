'''
Created on 19 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
if __name__ == '__main__':
    pass

print('**************** Analisi (Data cleaning) GIGO "spazzatura dentro, spazzatura fuori" *****************')


df = pd.DataFrame({'Names': ['Simon', 'Kate', 'Francis', 'Laura', 'Mary', 'Julian', 'Rosie', 'Simon', 'Laura'],
                    'Height':[180, 165, 170, 164, 163, 175, 166, 180, 164],
                    'Weight':[85, 65, 68, 45, 43, 72, 46, 85, 45],
                    'Pref_food': ['steak', 'pizza', 'pasta', 'pizza', 'vegetables', 'steak', 'seafood', 'steak', 'pizza'],
                    'Sex': ['m','f','m','f','f','m','f', 'm', 'f']})

print(df)

df_dummy = pd.get_dummies(df['Sex'], prefix = 'Sex')
print(df_dummy)

df=df.join(df_dummy)
print(df)

del df['Sex']
print(df)
