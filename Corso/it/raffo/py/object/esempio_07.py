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
    def __init__(self,valore=None,dimensione=None):
        self.valore=valore
        super().__init__(dimensione)
    
a=AClass(20,3)
print(a.valore)


a.printDimensione()