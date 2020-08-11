'''
Created on 9 ago 2020

@author: raffa
'''
import sys

if __name__ == '__main__':
    pass

x=20
print('id   : ',id(20))
print('type : ', type(x))
print(sys.getrefcount(x))

y='python'
print(y.upper())
print(y)