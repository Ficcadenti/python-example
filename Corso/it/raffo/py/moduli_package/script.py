'''
Created on 12 ago 2020

@author: raffa
'''
import it.raffo.py.moduli_package.modulo_01 as m_01
from it.raffo.py.moduli_package.modulo_02 import somma
from it.raffo.py.moduli_package.modulo_02 import somma as f1

if __name__ == '__main__':
    pass

cR=m_01.ContoCorrente('Raffaele Ficcadenti','RF00001',42000)
cV=m_01.ContoCorrente('Valeria Greco','VG00001',75000)
cR.descrizione()
cV.descrizione()

m_01.GestoreContiCorrenti.bonifico(cR,cV,400)
cR.descrizione()
cV.descrizione()

print(type(m_01))
print(type(f1))

print(type(somma))

print(f1(10,2))
print(somma(10,2))

print(f1(10,2))


