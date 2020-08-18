'''
Created on 18 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass



x=10

try:
    y=int(input('Inserisci un numero : '))
    r=x/y
except Exception as e:
    print(str(e).capitalize())
finally:
    print('Eseguo comunque !!!!')