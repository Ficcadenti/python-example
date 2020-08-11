'''
Created on 11 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

def outer(x,y):
    def sum(a,b):
        return a+b
    print(sum(x,y))
 
 
def outer_1():
    def inner(a,b):
        print(a+b)
    return inner  

outer(10,5)

f=outer_1()
f(20,5)