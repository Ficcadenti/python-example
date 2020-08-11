'''
Created on 11 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

def lista_dif(l1,l2=[1,2,3,4,5]):
    l=[]
    for x in l1:
        if not x in l2:
            l.append(x)
    return l

a=[12,3,4,5]
b=[3,7,6,0]
print(lista_dif(a,b))
print(lista_dif(a))
