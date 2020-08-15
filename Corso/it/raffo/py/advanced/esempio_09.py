'''
Created on 15 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

def calcolaQuadrato(n):
    return n*n


numeri = range(1,5)


result = map(calcolaQuadrato, numeri)
numeriQuadrati = set(result)
print(sorted(numeriQuadrati))


result = map(lambda x: x*x, numeri)
numeriQuadrati = set(result)
print(sorted(numeriQuadrati))
