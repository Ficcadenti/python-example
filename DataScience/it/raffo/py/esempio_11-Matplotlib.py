'''
Created on 18 ago 2020

@author: raffa
'''
from matplotlib.lines import lineStyles

if __name__ == '__main__':
    pass

import matplotlib as mlp
import matplotlib.pyplot as plt

''' per visualizzare i grafici in jupiter
%matplotlib inline
'''

plt.plot([5,3,4,5,6,7],[1,2,3,4,5,6],'ro')
plt.show()

x=[1,2,3,4,5,6]
y=[5,3,8,9,2,4]

plt.plot(x,y,linewidth=4.0, linestyle= '--')
plt.show()
