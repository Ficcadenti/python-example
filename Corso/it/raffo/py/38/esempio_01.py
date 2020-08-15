'''
Created on 13 ago 2020

@author: raffa
'''
from test.ann_module2 import __annotations__

if __name__ == '__main__':
    pass

def somma(a,b):
    return a+b

def saluta(nome = (n := 'Valeria')):
    print('Ciao ',nome)
    print('Ciao ',n.upper())

(x:=somma(5,3))
print(x)

if x:=somma(10,3)  > 6:
    print('x maggiore di 6')
    
l=[1,2,3,4,5,6]
while x:=len(l) !=0:
    print(x,l.pop())
    

saluta()
saluta('Raffaele')
