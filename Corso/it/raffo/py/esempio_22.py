'''
Created on 11 ago 2020

@author: raffa
'''
from _ast import Nonlocal

if __name__ == '__main__':
    pass

x=100
def stampa():
    x=1
    print(x)
    
def stampa2():
    global x
    x=1
    print(x)
    
def esterna():
    y=20
    def interna():
        nonlocal y
        y=50
        print(y)
    interna()
    print(y)
    
    
stampa()
print(x)
stampa2()
print(x)

esterna()