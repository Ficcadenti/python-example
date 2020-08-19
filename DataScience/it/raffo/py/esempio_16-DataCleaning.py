'''
Created on 19 ago 2020

@author: raffa
'''
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import matplotlib as mlp
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pass

def ricodifica_gender(gender):
    if gender=='m':
        return 0
    elif gender == 'male':
        return 0
    elif gender == 'mm':
        return 0
    elif gender == 'ma':
        return 0
    else:
        return 1
    

        
studenti=pd.read_csv('../../../students2.csv')

print('**************** Analisi (Data cleaning) GIGO "spazzatura dentro, spazzatura fuori" *****************')

print(studenti)
print(studenti.dtypes)

print(studenti['gender'].value_counts())
print(studenti['mark1'].value_counts())
print(studenti['mark1'].value_counts(dropna=False))
print(studenti.dropna())
print(studenti.shape)
studenti.replace([224],[24],inplace=True)
studenti.replace([330],[30],inplace=True)
studenti['mark1'].fillna(studenti['mark1'].mean(),inplace=True)
studenti['mark2'].fillna(studenti['mark2'].mean(),inplace=True)
studenti['mark3'].fillna(studenti['mark3'].mean(),inplace=True)
studenti['gender_ricod']=studenti.gender.apply(ricodifica_gender)
studenti['fres_ricod']=studenti.fres.apply(lambda x: x.replace('negative','0'))
studenti['fres_ricod']=studenti.fres.apply(lambda x: x.replace('neg','0'))
studenti['fres_ricod']=studenti.fres.apply(lambda x: x.replace('positive','1'))
studenti['fres_ricod']=studenti.fres.apply(lambda x: x.replace('pos','1'))
print(studenti)
studenti.boxplot()
plt.show()