'''
Created on 19 ago 2020

@author: raffa
'''
import matplotlib as mlp
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pass

a=[1,2,3,4,5]
b=[5,3,7,6,5]
c=[1,5,3,2,0]
d=[1,2,16,3,5]
e=[3,7,5,3,1]
f=[7,9,0,1,2]
x=[1,2,3,4]
y=[5,3,8,9]

col=['yellow','red','green','orange']
lab=['yellow','red','green','orange']
exp=[0.5,0,0,0.6]

plt.pie(x,colors=col,labels=lab,explode=exp)
plt.show()

plt.scatter(x,y)
plt.show()
