'''
Created on 18 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

# importo il pacchetto pandas con pd e numpy con np
import pandas as pd
import numpy as np

np.random.seed(5)
df1=pd.DataFrame(np.random.randn(10,5))
print(df1.keys())
print(df1.iloc[:2,1:3])
print(df1.describe())

np.random.seed(5)
df1=pd.DataFrame(np.random.randn(10,5))
print(df1.iloc[:2,1:3])
print(df1.describe())

# distribuzione binomiale 
df2= pd.DataFrame(np.random.binomial(100,0.5,(10,5)))
print(df2)

# distribuzione poisson 
df3= pd.DataFrame(np.random.poisson(100,(10,5)))
print(df3)

# distribuzione uniforme
df4= pd.DataFrame(np.random.uniform(1,100,(10,5)))
print(df4)