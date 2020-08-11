'''
Created on 11 ago 2020

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

class AClass(BClass):
    pass


m1=AClass(1)
m2=BClass()

print(isinstance(m1, AClass))
print(isinstance(m1, BClass))

print(isinstance(m2, AClass))
print(isinstance(m2, BClass))

print(m1.getDimensione())
print(m2.getDimensione())