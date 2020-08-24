
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import  StandardScaler

print('Machine Learning - Regressione Logistica !!!!')

df = pd.read_csv('../../../../pid.csv')
columns = ["","pregnant","glucose","pressure","triceps","insulin","mass","pedigree","age","diabetes"]
df.columns=columns

cl=df['diabetes']
df.drop('diabetes',axis=1,inplace=True)
print(df.head(5))
print(df.shape)

df_sc=StandardScaler().fit_transform(df)
x_train,y_train, x_test,y_test = train_test_split(df_sc,cl,test_size=0.3, random_state=12345)

lr=LogisticRegression()
lr.fit(x_train, y_train)
