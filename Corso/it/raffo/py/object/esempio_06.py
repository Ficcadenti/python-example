'''
Created on 12 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

class BClass():
    def __init__(self,dimensione=None):
        self.dimensione=dimensione
    def setDimensione(self,dimensione):
        self.dimensione=dimensione
    def getDimensione(self):
        return self.dimensione
    def printDimensione(self):
        print("BClass : "+str(self.dimensione))
        
class AClass(BClass):
    def printDimensione(self):
        print("AClass : "+str(self.dimensione))
        
a=AClass(2)
b=BClass(3)

a.printDimensione()