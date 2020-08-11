'''
Created on 11 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

#decorartori di funzione
def myDecorator(f):
    def decorator(x):
        print('Ho decorato')
        f(x)
    return decorator


@myDecorator
def myFunc(x):
    print("la funzione myFunc con parametro '"+str(x)+"'\n")
    

#myFunc=myDecorator(myFunc)
myFunc('Ciao')
