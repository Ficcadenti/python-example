'''
Created on 11 ago 2020

@author: raffa
'''
from _testbuffer import staticarray
from builtins import staticmethod

if __name__ == '__main__':
    pass

class MyClass():
    counter=0
    def __init__(self):
        MyClass.counter+=1
    
    @classmethod
    def istanze(cls):
        print(cls.counter)  
        
    @staticmethod
    def somma(a,b):
        return (a+b)  

c1=MyClass()
c2=MyClass()
c3=MyClass()


c1.istanze()
c2.istanze()
c3.istanze()

print(MyClass.somma(10,20))
