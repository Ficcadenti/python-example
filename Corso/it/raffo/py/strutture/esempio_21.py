'''
Created on 11 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

#LEGB

#local scope
def sum(x,y):
    c= x+y
    return c

#enclosed scope
def esterna(x):
    y=20
    def interna():
        print(x+y)
    interna()    

#global scope
b=100
def myFunc(x):
    print(x+b)
    

#local scope
print(sum(2,3))

#enclosed scope
esterna(10)

#global scope
myFunc(10)

#built-in scope
print('Python 3.6.1')