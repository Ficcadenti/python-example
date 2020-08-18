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
print('********')
print(df1.describe())
print('********')
print(df1.dtypes)
print('********')
print(df1.shape)
print('********')
print(df1.info())
print('********')
df1.set_index('Names')
print(df1)


print('********')
df1.sort_values(by='Weight',inplace=True)
print(df1)
print(df1.keys())

print('********')
print(df1[:3])
print(df1[3:])


print('******** .loc')
df2= pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])

print(df2)
print(df2.keys())
print(df2.loc['viper'])
print('******** .iloc')
print(df2.iloc[:,:])
print('******** .iloc')
print(df2.iloc[0,0])

print(df2[df2.max_speed>1])
print(df2[df2['shield']==2])

print(df1[df1.Height>170])
print(df1[df1['Sex']=='m'])

df1["new_col"]=df1.Height/100
print(df1)

g1=df1.groupby('Sex')
print(g1.groups)

g2=df1.groupby('Pref_food')
print(g2.groups)

print(g1.describe())
print(g2.describe())

df_dummy = pd.get_dummies(df1['Sex'],prefix='Sex')

print(df_dummy)

df1=df1.join(df_dummy)
print(df1)

del df1['new_col']
print(df1)

print(df1.duplicated())

df2=df1.drop_duplicates()
print(df2)
s1=df2.stack()
print(s1)
print(s1.unstack())

print(pd.melt(df2))

print(df1.T)

print(df1.sample(3))

np.random.seed(1)
print(df1.sample(2))

np.random.seed(1)
print(df1.sample(2))
print(df1.sample(frac=0.5))


# dati mancanti
df_missing=pd.read_csv('../../../df_missing.csv')
print(df_missing)
print(df_missing.shape)
print(pd.isnull(df_missing))
print(pd.notnull(df_missing))


print(df_missing.dropna().shape)

print(df_missing.dropna())
print(df_missing.dropna(axis=1, how='any'))

print(df_missing)
print(df_missing.fillna(0))
print(df_missing.fillna('missing'))
print(df_missing.fillna(df_missing.mean()))

print(df_missing['C'].fillna(df_missing['C'].mean()))

print(df_missing['C'].fillna(method='ffill'))

print(df_missing['C'].fillna(method='backfill'))


