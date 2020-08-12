'''
Created on 12 ago 2020

@author: raffa
'''

class BClass:
    b=10
    def bFunc(self):
        print('Sono in bFunc')
        
    def xFunc(self):
        print('Sono in BClass.xFunc()')

class CClass:
    c=20
    def cFunc(self):
        print('Sono in cFunc')
    
    def xFunc(self):
        print('Sono in CClass.xFunc()')

class AClass(BClass,CClass):
    pass