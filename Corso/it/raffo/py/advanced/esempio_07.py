'''
Created on 15 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

from functools import reduce

def moltiplica_elementi(elemento1, elemento2):
    return elemento1 * elemento2

def somma_elementi(elemento1, elemento2):
    return elemento1 + elemento2

lista = [1, 2, 3, 4, 5]

risultato = reduce(moltiplica_elementi, lista)
print(risultato)

risultato = reduce(somma_elementi, lista)
print(risultato)