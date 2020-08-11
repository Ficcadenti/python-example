'''
Created on 11 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass


class Punto:
    def setDimensione(self,dimensione):
        self.dimensione=dimensione
    def getDimensione(self):
        if hasattr(self, 'dimensione'):
            return self.dimensione
        else:
            return None
p1=Punto()
p2=Punto()

p1.setDimensione(3)
p1.setDimensione(2)
print(p1.getDimensione())
print(p2.getDimensione())