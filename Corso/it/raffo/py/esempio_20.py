'''
Created on 11 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

def esterna():
    def interna(x, y):
        print(x ** y)
    return interna

def sum(a,b):
    print(a + b)
    
def prod(a,b):
    print(a * b)
    
def myFunc(f,x,y):
    f(x,y)
    
myFunc(sum, 10, 5)
myFunc(prod, 10, 5)

esterna()