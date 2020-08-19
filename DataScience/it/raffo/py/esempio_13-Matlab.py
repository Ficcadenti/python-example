'''
Created on 19 ago 2020

@author: raffa
'''

import matplotlib as mlp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

if __name__ == '__main__':
    pass

col=['c1','c2','c3','c4']
df1=pd.DataFrame(np.random.rand(10,4),columns=col)

print(df1)
'''
df1.plot(kind='bar',stacked=True)
df1.hist()
df1['c1'].hist()
df1.boxplot(return_type='axes')
plt.savefig('graph1.png',dpi=600)
'''

df2=np.random.rand(100)
df3=np.random.rand(100)
plt.style.use('dark_background')
plt.hist(df2,color='red',alpha=0.3,bins=15)
plt.hist(df3,color='blue',alpha=0.6,bins=15)
print(plt.style.available)
plt.show();

