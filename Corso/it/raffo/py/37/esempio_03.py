'''
Created on 12 ago 2020

@author: raffa
'''
from dataclasses import dataclass

if __name__ == '__main__':
    pass


@dataclass(init=True, repr=True, order=True, frozen=False)
class MyClass:
    nome: str
    cognome: str
    
    
obj=MyClass('Raffaele','Ficcadenti')
obj1=MyClass('Raffaele','Ficcadenti')
obj2=obj;

print(obj)
print(obj)


    
if(obj==obj1):
    print('le due istanze sono uguali !!!')
    
print(obj<obj1)
print(obj2==obj1)