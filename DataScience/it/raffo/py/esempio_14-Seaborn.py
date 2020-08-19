'''
Created on 19 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

import matplotlib as mlp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

churns=pd.read_csv('../../../churn_miss.csv')
print(churns)

#sns.barplot(x='gender', y='lasttrans', data=churns, palette='rainbow')
#sns.kdeplot(churns.age)
#sns.stripplot(x='label',y='age',data=churns, hue='gender', jitter=True, dodge=True, palette='Set2')
#sns.set_style('dark')
#sns.heatmap(churns.isnull(),yticklabels=False)

voli= sns.load_dataset('flights')
#sns.heatmap(voli.corr(),annot=True)
vl=voli.pivot_table(values='passengers',index='month', columns='year')
#sns.heatmap(vl)
#sns.clustermap(vl,cmap='magma')

iris= sns.load_dataset('iris')
sns.pairplot(iris)
plt.show();