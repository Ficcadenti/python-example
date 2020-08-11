'''
Created on 11 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass



#metodi d'istanza, costruttore d'istanza __init__(self)
class Punto:
    def __init__(self,dimensione=None):
        self.dimensione=dimensione
    def setDimensione(self,dimensione):
        self.dimensione=dimensione
    def getDimensione(self):
        return self.dimensione
    
p1=Punto()
print(p1.getDimensione())
        