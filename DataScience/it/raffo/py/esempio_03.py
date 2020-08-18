'''
Created on 18 ago 2020

@author: raffa
'''

import pprint

if __name__ == '__main__':
    pass

# funzioni

# built-in
pp=pprint.PrettyPrinter(indent=4)
pp.pprint(dir(__builtins__))

test1=['obj1','obj2','obj3']
pp.pprint(dir(test1))

# definite utente

def somma(a,b):
    '''
    la funziona ritorna la somma 
    di a + b
    '''
    return a+b

print(somma(10,10))

x=0;
while x<somma(1,5):
    print(x)
    x+=1;