'''
Created on 18 ago 2020

@author: raffa
'''

from dataclasses import dataclass

if __name__ == '__main__':
    pass

@dataclass(init=True, repr=True, order=True, frozen=False)
class gatto():
        nome:str
        eta:int
        colore:str
        razza:str
        
        def verso(self):
            print('miao')
            
        def fusa(self):
            print('grrrrr')
        
@dataclass(init=True, repr=True, order=True, frozen=False)
class persiano(gatto):
    carattere:str
            
        
    
mia=gatto('mia',1,'grigio','normale')
print(mia)            
print(mia.nome)

mia.verso()
mia.fusa()

p=persiano('mia',1,'grigio','normale','coccolone')
print(p)
p.verso()
mia.fusa()