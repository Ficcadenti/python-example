'''
Created on 18 ago 2020

@author: raffa
'''
from matplotlib.lines import lineStyles
from openpyxl.chart import marker

if __name__ == '__main__':
    pass

import matplotlib as mlp
import matplotlib.pyplot as plt

''' per visualizzare i grafici in jupiter
%matplotlib inline
'''
'''
plt.plot([5,3,4,5,6,7],[1,2,3,4,5,6],'ro')
plt.show()
'''

x=[1,2,3,4,5,6]
y=[5,3,8,9,2,4]


help(plt.plot)

#plt.plot(x,y,linewidth=2.0, ls= '-', marker='o',markersize=10,markerfacecolor='white')

a=[1,2,3,4,5]
b=[5,3,7,6,5]
c=[1,5,3,2,0]
d=[1,2,16,3,5]
e=[3,7,5,3,1]
f=[7,9,0,1,2]

plt.subplot(2,2,1)
plt.plot(a,b,'b*')

plt.subplot(2,2,2)
plt.plot(c,d,'g^')

plt.subplot(2,2,3)
plt.plot(e,f,'ro')

plt.subplot(2,2,4)
plt.plot(x,y,linewidth=2.0, ls= '-', marker='o',markersize=10,markerfacecolor='white')
plt.title("Grafico 1",color='purple')
plt.xlabel("Asse x",color='blue')
plt.ylabel("Asse y",color='green')
plt.grid(True)
plt.legend(['Primo','Secondo','Terzo'],loc=2)
plt.show()

