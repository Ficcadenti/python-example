'''
Created on 11 ago 2020

@author: raffa
'''

#classi
#attributi di classe
if __name__ == '__main__':
    pass

class Punto:
    x=10
    y=20
    def pippo(self):
        print('pippo')
        
    def metodo(self,s):
        print(id(self))
        print(s)
    

p1=Punto()
p2=Punto()
print(type(Punto))

p1.x=100
print(f"P1: {p1.x},{p1.y}")
print(f"P2: {p2.x},{p2.y}")
print(f"Punto: {Punto.x},{Punto.y}")

p1.metodo('ciao')
p2.metodo('ciao')
p1.pippo()
