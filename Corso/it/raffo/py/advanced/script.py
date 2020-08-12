'''
Created on 12 ago 2020

@author: raffa
'''

import it.raffo.py.advanced.modulo_01 as m_01
if __name__ == '__main__':
    pass

obj=m_01.AClass()

print(obj.b)
print(obj.c)

obj.bFunc()
obj.cFunc()

#MRO
obj.xFunc()
