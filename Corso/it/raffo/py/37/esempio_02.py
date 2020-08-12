'''
Created on 12 ago 2020

@author: raffa
'''
from test.ann_module2 import __annotations__
from builtins import str

if __name__ == '__main__':
    pass

class MyClass:
    nome: str
    cognome: str
    
    def __init__(self,nome,cognome):
        self.nome=nome
        self.cognome=cognome
    

def myFunc(x: "parametro x") -> "ritorno":
    return x

def myFunc1(x:int ,s: str="python") -> str:
    print(x)
    return s;

a: int = 10
b: int = 20
print(a)
print(b)
print(__annotations__)

print(myFunc.__annotations__)
print(myFunc1.__annotations__)
res=myFunc1(10)
print(res)

mc=MyClass('Raffaele','Ficcadenti')
print(mc)
print(mc.nome)
print(mc.cognome)