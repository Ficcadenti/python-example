'''
Created on 12 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

x=10
y=11

try:
    for i in range(50):
        print(i)
        raise IndexError('Errore nel loop')
except IndexError as e:
    print(e.args)
    raise
finally:
    print('Finally !!!')